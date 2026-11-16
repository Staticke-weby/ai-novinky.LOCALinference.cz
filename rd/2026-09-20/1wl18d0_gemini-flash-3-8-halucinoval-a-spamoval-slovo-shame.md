# 1wl18d0

**Gemini Flash 3.8 halucinoval a spamoval slovo „shame“**

| Položka | Hodnota |
|---|---|
| Subreddit | r/GeminiAI |
| Autor | u/Junior_Deputy |
| Čas | 20. 9. 2026 01:42 (Europe/Prague) |
| Skóre | 443 |
| Komentáře | 66 |
| Odkaz | https://i.redd.it/yk1s1fanckqh1.jpeg |
| Diskuse | https://www.reddit.com/r/GeminiAI/comments/1wl18d0/gemini_flash_38_hallucinated_spammed_shame/ |

## Co se stalo

Uživatel u/Junior_Deputy zveřejnil v subredditu r/GeminiAI příspěvek s titulkem, že Gemini Flash 3.8 halucinoval a spamoval slovo „shame“. Podle vlastního popisu šlo o běžné „vibe coding“, tedy práci s AI asistentem v editoru, po níž model místo očekávaného výstupu začal opakovat jedno slovo. Autor dodává, že stejný problém viděl i u jiného redditora, a ptá se, co se vlastně děje.

Post odkazuje na screenshot (obrázek na i.redd.it), který zachycuje prostředí Antigravity IDE s vybraným modelem „Gemini 3.8 Flash High“. V panelu odpovědi je vidět nadpis „Proceeded with Implementation Plan“ a pod ním desítky řádků tvořených výhradně slovem „shame“, které zaplnily celou odpověď.

Ve stejné obrazovce je vidět i seznam změněných souborů projektu „Algerian Grocery Project Analysis“ – šest souborů se změnami (qoffa_tokens.dart, qoffa_bottom_sheet.dart, qoffa_tactile_pressable.dart, qoffa_typing_box.dart, app_router.dart, product_details_modal.dart) a tlačítka „Reject all“ a „Accept all“. Ve stavovém řádku je uvedeno Windows (windows-x64), Antigravity – Settings, čas 00:38 a datum 20/09/2026.

Diskuse pod příspěvkem se nese ve dvou rovinách: část komentujících řeší, zda jde o chybu konkrétní verze modelu a zda se vrátit k verzi 3.7, část si z opakovaného slova dělá legraci a přičítá ho tréninkovým datům, historii vyhledávání nebo „stresu“ modelu.

## Klíčová fakta

- Autor uvádí, že k chybě došlo při běžném „vibe coding“ a že stejný problém viděl i u dalšího redditora.
- Screenshot zachycuje Antigravity IDE s modelem označeným „Gemini 3.8 Flash High“ a odpovědí složenou z opakovaného slova „shame“.
- V IDE je zobrazeno šest souborů se změnami a tlačítka pro hromadné přijetí či odmítnutí změn.
- Několik komentujících hlásí stejné nebo podobné chování u verze 3.8 a doporučuje používat verzi 3.7.
- Jeden komentující nabízí technické vysvětlení: chybně nastavená post-processingová vrstva na konkrétním nasazení, která uměle vytlačí pravděpodobnost jednoho tokenu na první místo.
- Další komentující odkazuje na vlastní dřívější hlášení stejné chyby a jiný na arXiv preprint.

## Čísla

- 443 – skóre postu.
- 66 – počet komentářů pod postem.
- 25 z 45 – počet komentářů, které má balíček k dispozici (25 zobrazených z 45 stažených).
- 6 – počet souborů se změnami zobrazených v IDE na screenshotu.
- +10 −0 qoffa_tokens.dart, +130 −0 qoffa_bottom_sheet.dart, +20 −0 qoffa_tactile_pressable.dart, +83 −100 qoffa_typing_box.dart, +11 −0 app_router.dart, +42 −42 product_details_modal.dart – rozsah změn jednotlivých souborů na screenshotu.
- 00:38, 20/09/2026 – čas a datum ve stavovém řádku screenshotu.
- Čísla uvedená komentujícími (např. 3.7 vs. 3.8) jsou tvrzení komentujících, nikoli ověřená data.

## Citace

> „Normálně jsem vibe codoval a pak se stalo tohle, viděl jsem redditora se stejným problémem, tak co se sakra děje?“ (překlad) — u/Junior_Deputy

> „3.8 to dělá hodně, zatím používám 3.7.“ (překlad) — u/ByAyzen

> „Nejpravděpodobněji chybně nastavená post-processingová vrstva na konkrétním servírovacím nasazení, která uměle vytlačí pravděpodobnost jednoho tokenu (v tomto případě ‚Shame‘) na první místo bez ohledu na prompt nebo kontext.“ (překlad) — u/GabuTheDev

> „ale proč zrovna ‚shame‘? redditor, který měl tuhle stejnou chybu, měl stejné slovo“ (překlad) — u/Junior_Deputy

> „Příliš mnoho Hry o trůny.“ (překlad) — u/Reasonable-Yoghurt-7

## Co říkají komentáře

- **Návrat k verzi 3.7 kvůli chybovosti 3.8** – dva komentáře na nejvyšší úrovni (u/ByAyzen, u/RoundedAndSquared) doporučují používat verzi 3.7, autor odpovídá, že by měl udělat totéž. Jeden nesouhlasný komentář (u/Firm-Opening-5885) tvrdí, že „3.7 flash je stejná“.
- **Technická spekulace o vynuceném tokenu** – jeden komentář (u/GabuTheDev) popisuje možnou chybu nasazení, která vytlačí jeden token na první místo. Autor to podporuje tím, že jiný redditor měl stejné slovo „shame“.
- **Vtipy o tom, proč model říká „shame“** – více komentářů si dělá legraci: Hra o trůny, historie vyhledávání, uložené soubory, VRAM, „stresovaný“ Gemini, tréninková data od redditorů.
- **Srovnání s jinými modely a nástroji** – objevují se zmínky o Gemini 2 a 2.5 Pro, GPT („goblins“), Luně, deepseek v4.1 flash a Antigravity.
- **Další hlášení stejné chyby** – u/travianlime odkazuje na vlastní dřívější zkušenost, u/ZZotka přidává odkaz na arXiv preprint.

## Rozpory a neověřené informace

- **Způsobuje downgrade na 3.7 skutečně zmírnění chyby?** u/ByAyzen a u/RoundedAndSquared doporučují použít 3.7, ale u/Firm-Opening-5885 tvrdí, že „3.7 flash je stejná“. Jde o tvrzení jednotlivých uživatelů, nikoli o potvrzený závěr.
- **Příčina je technická, nebo humorná?** u/GabuTheDev tvrdí, že jde o „chybně nastavenou post-processingovou vrstvu na konkrétním servírovacím nasazení“, která vynucuje token „Shame“. Proti tomu stojí antropomorfní a vtipná vysvětlení (tréninková data, historie vyhledávání, stres, možná „vědomí“ modelu). Ani jedno není ověřené.
- u/Concurrency_Bugs tvrdí, že si model bere data o uživateli z interního profilu Google a „viděl historii vyhledávání“ – jde o vtip/spekulaci.
- u/travianlime tvrdí „stalo se mi to dříve“ s odkazem na další hlášení – jde o zprávu z druhé ruky.
- u/WaltzIndependent5436 tvrdí, že problém provází modely Gemini už od verze 2 nebo 2.5 Pro, a přirovnává ho k „goblins“ u GPT – neověřené tvrzení.
- Z obrázku ani balíčku nevyplývá žádné oficiální vyjádření Googlu k chybě.

## Proč to je důležité

Opakování jednoho tokenu místo smysluplné odpovědi je pro uživatele nástrojů pro psaní kódu zásadní selhání – zablokuje práci a vkládá do výstupu nesmyslný text, který musí člověk ručně odmítnout. Příspěvek zároveň ukazuje, že stejné slovo hlásí více lidí nezávisle, což naznačuje systémovou spíše než náhodnou povahu chyby. Diskuse je proto zajímavá jednak jako uživatelský report kvality modelu, jednak jako ukázka toho, jak rychle se v komunitě rodí spekulace o příčině bez oficiálního potvrzení.

## Zdroje

- https://www.reddit.com/r/GeminiAI/comments/1wl18d0/gemini_flash_38_hallucinated_spammed_shame/
- https://i.redd.it/yk1s1fanckqh1.jpeg
- https://www.reddit.com/r/GeminiAI/s/NXK3rRZ6p6
- https://arxiv.org/html/2609.16247v1
- 2026-09-20/_data/bundles/1wl18d0.md
- 2026-09-20/_data/img/1wl18d0.jpeg
