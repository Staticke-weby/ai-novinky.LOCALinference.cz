#!/usr/bin/env python3
"""Načte reddit cookies z profilů prohlížečů na bázi Chromia.

Podporuje Chrome, Chromium, Brave i vestavěný prohlížeč OpenCode. Chromium
od verze 130 ukládá cookies šifrované (AES-128-CBC, prefix `v10`/`v11`)
a k plaintextu přidává 32bajtový SHA-256 hostitele. Klíč leží v klíčence
(gnome-keyring, položky „… Safe Storage“); pro `v10` se používá historické
heslo `peanuts`. Databáze se čte z kopie, takže nevadí zámek běžícího prohlížeče.

Použití:
    from browser_cookies import reddit_cookies
    ck = reddit_cookies()          # dict name -> value
    python3 scripts/browser_cookies.py   # jen vypíše, co našel
"""
from __future__ import annotations

import hashlib
import os
import shutil
import sqlite3
import sys
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
HOME = Path.home()

# Pořadí, v jakém se profily zkouší. Dá se přebít proměnnou
# REDDIT_COOKIE_PROFILE (cesta k souboru Cookies).
PROFILE_GLOBS = [
    ".config/ai.opencode.desktop/Partitions/*/Cookies",   # prohlížeč OpenCode
    ".config/google-chrome/*/Cookies",
    ".config/chromium/*/Cookies",
    ".config/BraveSoftware/Brave-Browser/*/Cookies",
    ".config/OpenChamber/Partitions/*/Cookies",           # starý OpenChamber
]

CHROME_SCHEMA = "chrome_libsecret_os_crypt_password_v2"
PEANUTS = b"peanuts"


def _profile_dbs() -> list[Path]:
    override = os.environ.get("REDDIT_COOKIE_PROFILE")
    if override:
        return [Path(override).expanduser()]
    out: list[Path] = []
    for pattern in PROFILE_GLOBS:
        for p in sorted(HOME.glob(pattern)):
            if p.is_file() and p not in out:
                out.append(p)
    return out


def _copy_db(db: Path) -> str:
    """Zkopíruje DB i s WAL/SHM, aby se dalo číst za běhu prohlížeče."""
    tmpdir = tempfile.mkdtemp(prefix="cookies-")
    dst = os.path.join(tmpdir, "Cookies")
    shutil.copy(db, dst)
    for suffix in ("-wal", "-shm"):
        side = Path(str(db) + suffix)
        if side.exists():
            shutil.copy(side, dst + suffix)
    return dst


def _keyring_secrets() -> list[bytes]:
    """Vrátí všechny klíče „… Safe Storage“ z gnome-keyring (bez D-Busu prázdno)."""
    try:
        import dbus
    except Exception:
        return []
    try:
        bus = dbus.SessionBus()
        svc = bus.get_object("org.freedesktop.secrets", "/org/freedesktop/secrets")
        service = dbus.Interface(svc, "org.freedesktop.Secret.Service")
        _, session = service.OpenSession("plain", dbus.String("", variant_level=1))
        coll = service.ReadAlias("default")
        props = dbus.Interface(
            bus.get_object("org.freedesktop.secrets", coll),
            "org.freedesktop.DBus.Properties",
        )
        items = props.Get("org.freedesktop.Secret.Collection", "Items")
    except Exception as exc:
        print(f"  ! klíčenka nedostupná ({exc}) — zkusím jen nešifrované cookies", file=sys.stderr)
        return []

    secrets: list[bytes] = []
    for item_path in items:
        try:
            item = bus.get_object("org.freedesktop.secrets", item_path)
            iprops = dbus.Interface(item, "org.freedesktop.DBus.Properties")
            attrs = iprops.Get("org.freedesktop.Secret.Item", "Attributes")
            if str(attrs.get("xdg:schema", "")) != CHROME_SCHEMA:
                continue
            secret = dbus.Interface(item, "org.freedesktop.Secret.Item").GetSecret(session)
            secrets.append(bytes(secret[2]))
        except Exception:
            continue
    return secrets


def _derive_key(password: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha1", password, b"saltysalt", 1, 16)


def _decrypt(enc: bytes, host_key: str, keys: list[bytes]) -> str | None:
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    if enc[:3] not in (b"v10", b"v11"):
        # nešifrovaná hodnota (starší profily)
        try:
            return enc.decode()
        except UnicodeDecodeError:
            return None
    ciphertext = enc[3:]
    domain_hash = hashlib.sha256(host_key.encode()).digest()
    for key in keys:
        try:
            dec = Cipher(algorithms.AES(key), modes.CBC(b" " * 16)).decryptor()
            plain = dec.update(ciphertext) + dec.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            plain = unpadder.update(plain) + unpadder.finalize()
        except Exception:
            continue
        # Chrome ≥130 přidává na začátek SHA-256 hostitele.
        if plain[:32] == domain_hash:
            plain = plain[32:]
        try:
            return plain.decode()
        except UnicodeDecodeError:
            continue
    return None


def reddit_cookies() -> dict[str, str]:
    """Vrátí cookies z prvního profilu, který má reddit session (token_v2)."""
    keys = [_derive_key(s) for s in _keyring_secrets()]
    keys.append(_derive_key(PEANUTS))  # v10 bez klíčenky
    for db in _profile_dbs():
        try:
            tmp = _copy_db(db)
            con = sqlite3.connect(tmp)
            rows = con.execute(
                "select host_key,name,value,encrypted_value from cookies "
                "where host_key like '%reddit%'"
            ).fetchall()
            con.close()
        except Exception as exc:
            print(f"  ! nelze přečíst {db}: {exc}", file=sys.stderr)
            continue
        found: dict[str, str] = {}
        for host_key, name, value, enc in rows:
            if value:
                found[name] = value
            elif enc:
                dec = _decrypt(bytes(enc), host_key, keys)
                if dec is not None:
                    found[name] = dec
        if "token_v2" in found:
            print(f"  reddit cookies: {db} ({len(found)} cookies)", file=sys.stderr)
            return found
    return {}


if __name__ == "__main__":
    cookies = reddit_cookies()
    if not cookies:
        print("žádné reddit cookies nenalezeny", file=sys.stderr)
        raise SystemExit(5)
    print(f"{len(cookies)} cookies, token_v2: {'ano' if 'token_v2' in cookies else 'ne'}")
    for name in sorted(cookies):
        print(f"  {name}: {cookies[name][:12]}…")
