# Hacker News – denní AI/tech souhrn, 30. 10. 2026

## Metodika

Vybral jsem z 45 kandidátů, které pro 30. 10. 2026 připravil sběrný skript (`_data/candidates.json`). Ten den jsem prošel 1 000 story v datasetu; do přílohy se dostalo 63 story s alespoň 10 komentáři, z toho 19 označených jako AI a dvě další AI/tech story, které jsem zařadil ručně (Herdr a rezoluce proti bailoutu AI bubliny).

Po filtraci a deduplikaci vyšlo **13 článků**. Jeden duplicitní HN post jsem sloučil (50302334 → 50300683). Dvě témata se překrývají s dnešním Redditem a jsou v plánu označená `souvisi_s`: herní remaky Anthropicu (Reddit `1xjgfuv`) a Altmanův výrok o DRAM (Reddit `1xizbq1`); ve sloučeném denním přehledu se spojí do jedné sekce.

Jako už vyšlé jsem vyřadil **3 kandidáty ve 2 tématech**: širší výprodej technologických akcií kvůli nákladům na AI (50306008 a 50303833) navazoval na včerejší propad Alphabetu o 500 mld. USD a téma levných GPU (50302407) na redditový post z 28. 10. Zbylé nevybrané položky byly mimo AI/tech záběr nebo měly slabý zdroj.

Několik externích článků nešlo načíst celý (FT vrátil 403, Reuters 401, YouTube jen rámec), takže články staví na dostupných úryvcích, popisu v balíčku a diskusi. HN komentáře nemají veřejné skóre, proto se v textech neuvádí.

## Články

| # | Titulek | Skóre | Komentáře | Čas (Praha) | Poznámka |
|---:|---|---:|---:|---|---|
| 1 | [Zadní vrátka v oficiálním rozšíření Claude Code pro VS Code](50300683_zadni-vratka-claude-code-vs-code.md) | 863 | 513 | 08:09 | sloučeno 50302334 |
| 2 | [AI nenahrazuje SRE, ale bere jim praxi na vzácné incidenty](50305693_ai-nenahrazuje-sre-deskilling.md) | 557 | 411 | 16:52 | — |
| 3 | [Anthropic těsně před IPO čeká junk rating, tvrdí Blackstone](50307219_anthropic-ipo-junk-rating.md) | 301 | 249 | 18:27 | — |
| 4 | [Proton zrušil AI „re-pohovory“ po odporu zaměstnanců](50307183_proton-zrusil-ai-re-pohovory.md) | 270 | 222 | 18:24 | — |
| 5 | [NES emulátor běží ve vahách Qwenu, každý token je instrukce](50306442_nes-emulator-v-weights-qwen.md) | 231 | 118 | 17:40 | — |
| 6 | [Cisco dal 27letému inženýrovi neomezené tokeny na přepis legacy kódu](50304122_cisco-neomezene-tokeny-legacy-kod.md) | 150 | 189 | 15:08 | — |
| 7 | [Anthropic zakázal přepisování existujících her v Claude Code](50304358_anthropic-zakaz-hernich-remaku.md) | 106 | 104 | 15:22 | Reddit `1xjgfuv` |
| 8 | [Altman: držet DRAM doma je plýtvání, patří do datacenter](50305797_altman-dram-lokalni-inference.md) | 83 | 93 | 16:58 | Reddit `1xizbq1` |
| 9 | [Intel spadl o 25 %, strhl s sebou čipový trh](50303791_intel-pad-25-procent-cipovy-trh.md) | 81 | 95 | 14:43 | — |
| 10 | [Demokraté chtějí zabránit bailoutu AI bubliny](50302814_demokrate-proti-bailoutu-ai-bubliny.md) | 633 | 486 | 13:08 | — |
| 11 | [AI maže hranici mezi produktovým manažerem a vývojářem](50309534_ai-maze-hranici-pm-a-vyvojare.md) | 55 | 76 | 21:14 | — |
| 12 | [Ask HN: práce s AI unavuje víc než práce bez ní](50301479_ask-hn-unava-z-ai.md) | 144 | 139 | 10:17 | — |
| 13 | [Herdr: desktop pro terminály a coding agenty](50298436_herdr-desktop-pro-coding-agenty.md) | 350 | 243 | 01:42 | — |

## Příloha: všechny AI/tech story s alespoň 10 komentáři

| ID | Skóre | Komentáře | Čas (Praha) | Titulek |
|---|---:|---:|---|---|
| 50300683 | 863 | 513 | 08:09 | [Backdoor v rozšíření Claude Code pro VS Code na Cursor Marketplace](50300683_zadni-vratka-claude-code-vs-code.md) |
| 50302334 | 655 | 17 | 12:05 | [Backdoory v oficiálních rozšířeních Claude Code](50300683_zadni-vratka-claude-code-vs-code.md) |
| 50302814 | 633 | 486 | 13:08 | [Američtí kongresmani vedou demokratickou rezoluci proti záchraně Big Techu před AI bublinou](50302814_demokrate-proti-bailoutu-ai-bubliny.md) |
| 50305693 | 557 | 411 | 16:52 | [AI nenahrazuje SRE, jen je zbavuje dovedností](50305693_ai-nenahrazuje-sre-deskilling.md) |
| 50298436 | 350 | 243 | 01:42 | [Herdr vydal nativní aplikaci](50298436_herdr-desktop-pro-coding-agenty.md) |
| 50307219 | 301 | 249 | 18:27 | [Anthropic po IPO možná nezíská investiční rating, tvrdí Blackstone](50307219_anthropic-ipo-junk-rating.md) |
| 50307183 | 270 | 222 | 18:24 | [CEO Protonu ruší AI „přepohovory“](50307183_proton-zrusil-ai-re-pohovory.md) |
| 50306008 | 249 | 280 | 17:13 | [Americké technologické akcie prudce padají kvůli obavám z nákladů na AI](https://news.ycombinator.com/item?id=50306008) |
| 50306442 | 231 | 118 | 17:40 | [Show HN: Funkční Nintendo v ~1GB vah Qwen](50306442_nes-emulator-v-weights-qwen.md) |
| 50304122 | 150 | 189 | 15:08 | [Cisco dalo inženýrovi neomezené AI tokeny na přepsání legacy kódu](50304122_cisco-neomezene-tokeny-legacy-kod.md) |
| 50301479 | 144 | 139 | 10:17 | [Ask HN: Jste v téhle éře AI taky unavení?](50301479_ask-hn-unava-z-ai.md) |
| 50304358 | 106 | 104 | 15:22 | [Anthropic zakročuje proti přepisování videoher](50304358_anthropic-zakaz-hernich-remaku.md) |
| 50305797 | 83 | 93 | 16:58 | [Sam Altman si myslí, že plýtváte DRAM](50305797_altman-dram-lokalni-inference.md) |
| 50303791 | 81 | 95 | 14:43 | [Intel padá o 25 % a kvůli chmurnému výhledu strhává dolů čipové akcie po celém světě](50303791_intel-pad-25-procent-cipovy-trh.md) |
| 50299182 | 63 | 40 | 03:33 | [CVE-2026-98432: Riziko use-after-free v Linux TCP a ověření záplaty](https://news.ycombinator.com/item?id=50299182) |
| 50309534 | 55 | 76 | 21:14 | [Ani produktoví manažeři nejsou v bezpečí](50309534_ai-maze-hranici-pm-a-vyvojare.md) |
| 50304280 | 52 | 24 | 15:18 | [Neal Stephenson o AI a o tom, co přijde dál [video]](https://news.ycombinator.com/item?id=50304280) |
| 50302407 | 41 | 53 | 12:16 | [Optika vydrží desetiletí, GPU tři roky: AI boom není dot-com boom [video]](https://news.ycombinator.com/item?id=50302407) |
| 50303833 | 17 | 11 | 14:47 | [Prasknutí AI bubliny](https://news.ycombinator.com/item?id=50303833) |
| 50303030 | 13 | 11 | 13:33 | [Musk a Zuckerberg se na hovorech k výsledkům snaží přejmenovat AI na „superinteligenci“](https://news.ycombinator.com/item?id=50303030) |
| 50310055 | 7 | 18 | 21:58 | [Show HN: Ultrarychlý agentní workspace v Rustu](https://news.ycombinator.com/item?id=50310055) |

U story bez samostatného článku míří odkaz na diskusi na HN. Sloučené story míří na článek, do kterého byly sloučeny.
