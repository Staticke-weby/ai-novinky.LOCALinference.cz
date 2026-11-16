# 1wqybjk
**MiniMax H3 a pohyb kamery z Blenderu v ComfyUI**

r/comfyui · u/Time-Ad-7720 · 26. září 2026, 18:49 · 206 bodů / 16 komentářů · [diskuse](https://www.reddit.com/r/comfyui/comments/1wqybjk/i_used_a_blender_mannequin_clip_to_guide_minimax/)

Autor si nejdřív postavil pohyb kamery v Blenderu: přes Codex CLI a Blender MCP vytvořil jednoduchou scénu s manekýnem, tělo nechal stát na místě a hlavu s očima nechal sledovat objektiv. Pětisekundový render v rozlišení 1080 na 1080 při 30 snímcích za sekundu pak spolu s referenčním listem postavy a obrázkem nábřeží vložil do reference-to-video workflow modelu MiniMax H3 v ComfyUI, kde prompt každému vstupu přiřazuje roli postavy, prostředí a pohybu kamery. Jízda se drží převážně polocelku s rychlými plynulými přejezdy, krátkými výdržemi a jedním extrémním detailem před koncem a vrací se do úvodní kompozice, autor ale upozorňuje, že výstup je potřeba zkontrolovat kvůli držení identity, rámování, konzistenci pozadí a spoji smyčky. Na RTX 5070 Ti s 32 GB paměti generoval na 20 kroků rychlostí asi 53 sekund na iteraci, tedy zhruba 17 minut a 40 sekund samotného samplování bez načítání a dekódování, při nastavení rozlišení 0,6 a poměru stran 1:1 bez turbo LoRA, všechny soubory včetně scény, workflow a promptů dal k dispozici na Disku.

Nápad si rychle získal příznivce. u/wildmonkeywranglerovi to přijde jako výborný nápad, u/Easy_Werewolf7903 děkuje za sdílení a u/yotraxx slibuje, že to co nejdřív vyzkouší. Protiváhu k pečlivému stavění scény v Blenderu přinesl u/RazsterOxzine, který si vystačí s webkamerou a bílým tričkem: MiniMax H3 s tím prý nemá problém, stačí mu k tomu OBS.

Vedle chvály se řešily i alternativní cesty a limity. u/enndeeee poznamenal, že totéž umí Meridian s VGGT, a prozradil, že právě staví workflow založený na Gaussian Splattingu. Praktickou otázku přidal u/SpaceNinjaDino, jestli autor zkoušel více postav najednou, protože od tří postav na záběru se mu postavy začínají slévat; autor odpověděl, že víc než dvě postavy v jednom záběru zatím nezkoušel.

Nejdelší výměna patří postavení MiniMaxu mezi lokálními generátory videa. u/wildmonkeywrangler píše, že si s MiniMax H3 hraje týden a je závislý, a ptá se ostatních na shodu, jestli je pro lokální generování bez placených služeb velkých firem nejlepší. u/BoredHobbes odpovídá, že kromě LTX nic jiného není, a sám autor tvrdí, že je to nejlepší, co existuje. Do toho si u/Serenafriendzone utahuje, že ceny souborů s animacemi z Blenderu a motion capture dat letí k Měsíci, a u/Just_Lingonberry_352 by si přál generování v reálném čase, na což autor lakonicky odpovídá, že bude brzy.

Kdo si chce přesný pohyb kamery nejdřív osahat nanečisto, dostává tu hotový recept: rozhýbat panáka v Blenderu a teprve pak pustit ke slovu video model.
