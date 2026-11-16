# 1wm0xb6

**Zpětná analýza desktopového buildu OpenAI: nový „Codex Cloud“ s Tailscale, proxy tajemstvími a identitami Azure za přepínačem funkce**

| | |
|---|---|
| Subreddit | r/OpenAI |
| Autor | — |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 61 / 10 |
| Článek | https://runtimewire.com/article/openai-is-preparing-a-new-codex-cloud-with-tailscale-and-azure-workload-identity |
| Diskuse | https://www.reddit.com/r/OpenAI/comments/1wm0xb6/openai_is_preparing_a_new_codex_cloud_with/ |

## Co odhalila analýza buildu

RuntimeWire (Ryan Merket) porovnal desktop buildy OpenAI **9922 (26.915.31945)** a **9275 (26.908.70816)** a našel **feature-gated novou cestu „Codex Cloud“** vedle položky „Cloud (Legacy)“:

- **Agentem vedené onboarding rozhovory**: agent prohlédne vybrané repozitáře a připraví **návrh prostředí** („Preparing / Prepared environment draft“) k revizi vývojářem.
- **Reusable Tailscale auth keys** (validace prefixem `tskey-auth-`) pro přístup do privátní sítě.
- **Proxy-delivered network secrets** s whitelistem povolených HTTPS domén a metod.
- **Identita úloh přes OpenID Connect**: Azure (Entra tenant ID + client ID aplikace) je **nejdál a je „připojitelná“**; AWS (IAM role ARN + region) a Google Cloud (poskytovatel identit úloh + e-mail servisního účtu) jsou označené jako **„zatím jen konfigurace“**.
- Runner i katalog prostředí jsou za **feature gate 375130565**; počet výskytů `cloudThreadPrototype` vzrostl z **8 v buildu 9275 na 31 v buildu 9922**.

Článek to staví proti Anthropicovu modelu **self-hosted Claude Code runnerů** a upozorňuje, že z klientského buildu nelze určit, zda existuje backend, ani termín spuštění. **OpenAI nebyla před publikací kontaktována.**

## Citace

> „Desktopový build 9922 odděluje "Cloud" od "Cloud (Legacy)" a připojuje agenta pro návrh prostředí k přístupu do privátní sítě, tajemstvím doručovaným přes proxy a cloudovým identitám za…“ (překlad) — RuntimeWire

> „Runner i přepracovaný katalog prostředí zůstávají za feature gate `375130565`. Ten kód dokládá aktivní vývoj, nikoli veřejnou dostupnost ani načasování spuštění.“ (překlad) — RuntimeWire

> „Prostě to vytváří vzdálený přístup k chatům v Codex. Tedy můžu pracovat z Macu venku, ale kódovat dál na svém hlavním PC, které má veškerý potřebný hardware pro testování a nasazování.“ (překlad) — u/reddit_is_geh

> „K čemu to přesně je, proč místo toho nepracují na vylepšení svých produktů?“ (překlad) — u/Toss4n

> „Zajímavá volba stacku – Tailscale pro bezpečné síťování dává smysl, pokud spravují distribuované inferenční uzly, a Azure workload identity řeší autentizaci bez rozlézání klíčů.“ (překlad) — u/Talreja-Adanna

## Hlavní linky diskuse

- **Užitečnost.** Část lidí vítá vzdálený přístup (práce z Macu proti domácímu PC), jiní nevidí přínos.
- **Enterprise zaměření.** Tailscale + proxy secrets + workload identity = klasický enterprise networking stack, tedy cíl na firemní Codex zákazníky.
- **Srovnání s OpenClaw** a s tím, jak by to dělaly Google/Microsoft/Amazon.

## Neověřené informace

- Celé zjištění je **reverse engineering binárky** — existence backendu, termín a rozsah nejsou potvrzené, OpenAI se nevyjádřila.
- Neověřená tvrzení komentujících („vlastní OpenClaw“, spekulace o distribuované inferenci).

## Proč to je důležité

Ukazuje **směr, kterým se agentní coding posouvá**: od lokálního běhu k řízeným cloudovým prostředím s privátní síťovou konektivitou, tajemstvími a cloudovými identitami — tedy od „nástroje“ k firemní infrastruktuře. Pro týmy to znamená, že rozhodnutí mezi Codex Cloud, self-hosted Anthropic runnerem a vlastním řešením bude hlavně o síťové a identitní architektuře, ne o kvalitě modelu.

---

*Zdroje: [RuntimeWire](https://runtimewire.com/article/openai-is-preparing-a-new-codex-cloud-with-tailscale-and-azure-workload-identity), [Reddit diskuse](https://www.reddit.com/r/OpenAI/comments/1wm0xb6/openai_is_preparing_a_new_codex_cloud_with/).*
