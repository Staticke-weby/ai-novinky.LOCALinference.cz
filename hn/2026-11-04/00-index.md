# Hacker News – denní AI/tech souhrn, 4. 11. 2026

## Metodika

Zdroj: Hacker News, okno **4. 11. 2026** (Europe/Prague). Data pocházejí z kolektoru `scripts/hn-collect.py`; kandidáti jsou v `_data/candidates.json`, plné balíčky v `_data/bundles/`.

Z **45 kandidátů** vzniklo **20 článků**. Pět témat se překrývá s dnešním Redditem (RTX Spark, Kimi K3.1 Pro, Tencent Hy4, Ripple-65B a odmítnutí datacenter v referendech); v plánu jsou označena `souvisi_s` a ve sloučeném denním přehledu se spojí s redditovým článkem.

**1 téma bylo vyřazeno jako už vyšlé:** ceny RTX 5090 (navazují na story o 64/96GB modifikacích z 3. 11.). Zbylých 24 kandidátů bylo mimo AI/tech záběr – politika, obecná věda, klasické programování bez AI přesahu a lifestylové texty.

U pěti externích odkazů se nepodařilo načíst plný text (paywall nebo HTTP 403): Tencent Hy4, Qualcomm Cloud AI 100 Ultra, OpenAI/Pierre, Conductor a částečně PHP2Shell. Články proto vycházejí z dostupných úryvků, metadat a diskuse. Komentáře na HN nemají veřejné skóre; jejich pořadí odpovídá řazení HN.

## Články

| # | Téma | Skóre | Komentáře | Čas (Praha) | Poznámka |
|---:|---|---:|---:|---|---|
| 1 | [AI nutí firmy splácet 40 let technického dluhu. Případ PHP2Shell](50364336_ai-technicky-dluh-php2shell.md) | 1144 | 662 | 12:52 | — |
| 2 | [Gemini trénuje i na historii chatů předplatitelů. Opt-out prakticky neexistuje](50363461_gemini-trenink-historie-chatu-predplatitele.md) | 652 | 168 | 11:10 | — |
| 3 | [Nvidia RTX Spark na Linuxu: firmware zamkne GPU na 780 MHz a inference spadne na 35 %](50362905_nvidia-rtx-spark-linux-firmware-35-procent.md) | 597 | 276 | 09:46 | též Reddit `1xo1f2a` |
| 4 | [AMD poprvé v historii předběhne Intel. Ve čtvrtletí čeká tržby 17 miliard dolarů](50367125_amd-predbehne-intel-17-miliard.md) | 519 | 193 | 16:38 | — |
| 5 | [Kimi K3.1 Pro má otevřené váhy, milionový kontext a multimodální agentní zaměření](50366999_kimi-k3-1-pro-otevrene-vahy.md) | 459 | 132 | 16:30 | též Reddit `1xnrhvb` |
| 6 | [Američané v referendech odmítli datacentra. Prošla omezení v desítkách lokalit](50365982_americane-odmitli-datacentra.md) | 324 | 655 | 15:27 | též Reddit `1xngtve` |
| 7 | [Geoffrey Hinton: možná bychom byli bez AI lépe](50363554_geoffrey-hinton-bez-ai-lepe.md) | 304 | 301 | 11:23 | — |
| 8 | [Ripple-65B: americký open-weight model od pěti lidí míří na agentní kódování](50369925_ripple-65b-open-weight-agentni-kodovani.md) | 271 | 97 | 19:53 | též Reddit `1xnx3cs` |
| 9 | [Ask HN: Jak dnes lidé skutečně používají AI agenty?](50366117_ask-hn-jak-pouzivat-ai-agenty.md) | 245 | 234 | 15:37 | — |
| 10 | [OpenAI kupuje Pierre Computer Company](50366863_openai-kupuje-pierre-computer.md) | 225 | 69 | 16:21 | — |
| 11 | [Tencent Hy4: 770miliardový model míří k otevřeným vahám a levnějšímu API](50365780_tencent-hy4-open-weights.md) | 220 | 72 | 15:11 | též Reddit `1xnhzbz` |
| 12 | [Anthropic představil FlashProve: kryptografický důkaz, že odpověď opravdu vygeneroval daný model](50368626_anthropic-flashprove-provable-inference.md) | 202 | 88 | 18:17 | — |
| 13 | [Conductor se připojuje k Metě. Cloudová verze končí](50369503_conductor-joining-meta.md) | 158 | 170 | 19:22 | — |
| 14 | [Všechno je teď AI podvod. Esej o reklamách, které nikdo nekontroluje](50371508_vsechno-je-ai-podvod.md) | 134 | 51 | 22:05 | — |
| 15 | [Qualcomm Cloud AI 100 Ultra: 150W karta se 128 GB paměti pro inferenci](50370654_qualcomm-cloud-ai-100-ultra.md) | 131 | 53 | 20:55 | — |
| 16 | [Kino AI: mediální knihovna a střižna, na které pracují lidé i agenti](50368804_kino-ai-media-manager.md) | 82 | 32 | 18:31 | — |
| 17 | [Garry Tan z YC utrácí až 200 tisíc dolarů ročně za tokeny pro AI agenty](50366971_garry-tan-yc-200-tisic-tokeny-agenti.md) | 78 | 96 | 16:28 | — |
| 18 | [Akcie AI klesají. Volby v Texasu zvedly rizika pro datacentra](50362274_akcie-ai-texas-volby-datacentra.md) | 54 | 75 | 08:00 | — |
| 19 | [Codex dostal pokyn restartovat server. Zničil systemd, kontejnery a způsobil škodu přes 10 tisíc dolarů](50363717_codex-restart-server-skoda.md) | 45 | 32 | 11:43 | — |
| 20 | [Mac Studio s M5 Ultra a 512 GB paměti míří na lokální velké modely](50369098_mac-studio-m5-ultra-512-gb.md) | 33 | 27 | 18:51 | — |

## Příloha: všechny AI/tech story (24 položek)

Tabulka obsahuje všech 20 zpracovaných témat a čtyři další AI/tech story z `appendix.json`, které se do výběru nedostaly (už vyšlé téma, nižší priorita nebo krátká diskuse). U zpracovaných témat odkaz míří na soubor článku, u ostatních na diskusi na HN.

| ID | Titulek | Skóre | Komentáře | Čas (Praha) |
|---|---|---:|---:|---|
| 50364336 | [AI nutí firmy splácet 40 let technického dluhu. Případ PHP2Shell](50364336_ai-technicky-dluh-php2shell.md) | 1144 | 662 | 12:52 |
| 50363461 | [Gemini trénuje i na historii chatů předplatitelů. Opt-out prakticky neexistuje](50363461_gemini-trenink-historie-chatu-predplatitele.md) | 652 | 168 | 11:10 |
| 50362905 | [Nvidia RTX Spark na Linuxu: firmware zamkne GPU na 780 MHz a inference spadne na 35 %](50362905_nvidia-rtx-spark-linux-firmware-35-procent.md) | 597 | 276 | 09:46 |
| 50367125 | [AMD poprvé v historii předběhne Intel. Ve čtvrtletí čeká tržby 17 miliard dolarů](50367125_amd-predbehne-intel-17-miliard.md) | 519 | 193 | 16:38 |
| 50366999 | [Kimi K3.1 Pro má otevřené váhy, milionový kontext a multimodální agentní zaměření](50366999_kimi-k3-1-pro-otevrene-vahy.md) | 459 | 132 | 16:30 |
| 50365982 | [Američané v referendech odmítli datacentra. Prošla omezení v desítkách lokalit](50365982_americane-odmitli-datacentra.md) | 324 | 655 | 15:27 |
| 50363554 | [Geoffrey Hinton: možná bychom byli bez AI lépe](50363554_geoffrey-hinton-bez-ai-lepe.md) | 304 | 301 | 11:23 |
| 50369925 | [Ripple-65B: americký open-weight model od pěti lidí míří na agentní kódování](50369925_ripple-65b-open-weight-agentni-kodovani.md) | 271 | 97 | 19:53 |
| 50366117 | [Ask HN: Jak dnes lidé skutečně používají AI agenty?](50366117_ask-hn-jak-pouzivat-ai-agenty.md) | 245 | 234 | 15:37 |
| 50366863 | [OpenAI kupuje Pierre Computer Company](50366863_openai-kupuje-pierre-computer.md) | 225 | 69 | 16:21 |
| 50365780 | [Tencent Hy4: 770miliardový model míří k otevřeným vahám a levnějšímu API](50365780_tencent-hy4-open-weights.md) | 220 | 72 | 15:11 |
| 50368626 | [Anthropic představil FlashProve: kryptografický důkaz, že odpověď opravdu vygeneroval daný model](50368626_anthropic-flashprove-provable-inference.md) | 202 | 88 | 18:17 |
| 50369503 | [Conductor se připojuje k Metě. Cloudová verze končí](50369503_conductor-joining-meta.md) | 158 | 170 | 19:22 |
| 50371508 | [Všechno je teď AI podvod. Esej o reklamách, které nikdo nekontroluje](50371508_vsechno-je-ai-podvod.md) | 134 | 51 | 22:05 |
| 50370654 | [Qualcomm Cloud AI 100 Ultra: 150W karta se 128 GB paměti pro inferenci](50370654_qualcomm-cloud-ai-100-ultra.md) | 131 | 53 | 20:55 |
| 50368804 | [Kino AI: mediální knihovna a střižna, na které pracují lidé i agenti](50368804_kino-ai-media-manager.md) | 82 | 32 | 18:31 |
| 50366971 | [Garry Tan z YC utrácí až 200 tisíc dolarů ročně za tokeny pro AI agenty](50366971_garry-tan-yc-200-tisic-tokeny-agenti.md) | 78 | 96 | 16:28 |
| 50362274 | [Akcie AI klesají. Volby v Texasu zvedly rizika pro datacentra](50362274_akcie-ai-texas-volby-datacentra.md) | 54 | 75 | 08:00 |
| 50363861 | [Ceny RTX 5090 v obchodech přesahují 9 tisíc dolarů, GPU od Nvidia zdražují](https://news.ycombinator.com/item?id=50363861) | 52 | 77 | 12:02 |
| 50363717 | [Codex dostal pokyn restartovat server. Zničil systemd, kontejnery a způsobil škodu přes 10 tisíc dolarů](50363717_codex-restart-server-skoda.md) | 45 | 32 | 11:43 |
| 50365760 | [Jaron Lanier o paralelách mezi AI a sociálními sítěmi](https://news.ycombinator.com/item?id=50365760) | 43 | 10 | 15:10 |
| 50369098 | [Mac Studio s M5 Ultra a 512 GB paměti míří na lokální velké modely](50369098_mac-studio-m5-ultra-512-gb.md) | 33 | 27 | 18:51 |
| 50365009 | [Katastrofa je pořád lepší než AI](https://news.ycombinator.com/item?id=50365009) | 13 | 10 | 14:05 |
| 50362700 | [Ask HN: Jaký dopad mají americké volby na AI?](https://news.ycombinator.com/item?id=50362700) | 8 | 11 | 09:16 |
