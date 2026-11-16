# 1wl56g2

**Prosím, přestaňte už s těmi FP4 inference enginy, proboha**

| Položka | Hodnota |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/buttplugs4life4me |
| Čas | 20. 9. 2026 04:51 (Europe/Prague) |
| Skóre | 306 |
| Komentáře | 241 |
| Odkaz | https://www.reddit.com/r/LocalLLaMA/comments/1wl56g2/please_stop_with_the_fp4_inference_engines_for/ |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wl56g2/please_stop_with_the_fp4_inference_engines_for/ |

## Co se stalo

Autor příspěvku na r/LocalLLaMA si stěžuje na každodenní vlnu příspěvků, které představují „optimalizované konfigurace“ nebo nové inference enginy (nástroje pro běh modelů). Tyto příspěvky podle něj nejprve slibují výborné výsledky v jedné konkrétní věci, ale teprve na konci textu – nebo až v odpovědi na dotaz – vyjde najevo, že daný engine funguje pouze s formáty NVFP4/MXFP4.

Jeho hlavní výtka míří na to, že tvůrci těchto enginů zrychlí už tak nejrychlejší variantu běhu jen nepatrně, ale výstup modelu je podle něj „zcela uvařený“ a plný halucinací. Autor dodává, že podobný případ právě viděl i na r/ROCm.

Podle autora je v pořádku provozovat 4bitovou kvantizaci (quantization) u velkých modelů – ty obsahují velké množství informací, takže malá ztráta znamená jen to, že si model nepamatuje nějaký recept. U malých hustých (dense) modelů ale nasazení FP4 vede podle něj k jejich úplnému zničení.

V dodatečné úpravě příspěvku autor vysvětluje, že standardní kvantizace Q4 obvykle ponechává citlivé tenzory ve formátech BF16, Q8 nebo Q6/5 a K/V cache kvantizuje nanejvýš na FP8/Q8. Naproti tomu dotyčné „inference enginy“ obvykle vznikají jako fork (odvozená kopie) existujícího enginu – llama.cpp, SGlang nebo vLLM – a kvantizují úplně všechno dolů na FP4. To je podle něj skvělé pro rychlost, zejména bez online dequantizace (dequantization), ale výrazně to zhoršuje kvalitu. Standardní kvant Q4_K_M/XL od Unsloth je podle něj v pořádku.

## Klíčová fakta

- Autor kritizuje inference enginy, které převádějí všechny váhy do formátů NVFP4/MXFP4, a označuje jejich výstupy za náchylné k halucinacím.
- Podle jeho úpravy standardní Q4 kvantizace ponechává citlivé tenzory v BF16, Q8 nebo Q6/5 a K/V cache nanejvýš na FP8/Q8.
- Tvrdí, že malé husté modely FP4 „zabíjí úplně“, zatímco u velkých modelů je menší ztráta tolerovatelná.
- Většina diskuse se točí kolem toho, zda je NVFP4/MXFP4 v praxi bez problémů, nebo zda je nutná selektivní kvantizace.
- Část komentujících souhlasí s jádrem kritiky a stěžuje si na nízkou kvalitu forků a na nečestné vykazování benchmarků.
- Jeden z autorů vlastního enginu se do diskuse zapojil a hájí sdílení experimentálních enginů.
- Součástí vlákna jsou i vtipy o přehnaných číslech v token/s.

## Čísla

| Číslo | Co znamená |
|---|---|
| 306 | skóre příspěvku |
| 241 | počet komentářů |
| 4 | počet tenzorových formátů zmíněných jako „bezpečná“ úroveň (BF16, Q8, Q6/Q5, FP8/Q8) |
| 4× 5060 Ti | hardwarová sestava, na které podle komentujícího běžela NVFP4 konfigurace (tvrzení komentujícího) |
| 100 → 20 USD měsíčně | plánované snížení výdajů za cloudové předplatné (tvrzení komentujícího) |
| 8× RTX 6000 | sestava zmíněná v komentáři (tvrzení komentujícího) |
| pár R9700 | grafické karty zmíněné v komentáři (tvrzení komentujícího) |
| 3000 token/s | vtipné tvrzení o Raspberry Pi (tvrzení komentujícího) |
| 1002 tok/s | vtipné tvrzení o fiktivním enginu na GLM5.3 (tvrzení komentujícího) |

## Citace

> „A pak dole v příspěvku, nebo až poté, co se někdo zeptá, stojí ‚pouze NVFP4/MXFP4‘.“ (překlad) — u/buttplugs4life4me

> „Ale provozovat malé husté modely na FP4 je prostě zabije. Úplně.“ (překlad) — u/buttplugs4life4me

> „Váš standardní Q4_K_M/XL kvant od Unsloth je v pořádku.“ (překlad) — u/buttplugs4life4me

> „Provozuji Qwen3.8-27b s NVFP4 kvantem a KV cache. Nulové problémy. Časy se mění.“ (překlad) — u/DustNearby2848

> „NVFP4 je docela skvělé, pokud ho používáte správně. Očividně nekvatizujte všechno naslepo na NVFP4, citlivé části musíte nechat alespoň na FP8.“ (překlad) — u/JumpingJack79

> „Musíš se naučit, jak NVFP4 funguje, kámo. Na Blackwellu je to prakticky bezeztrátové FP8. Není důvod provozovat cokoli jiného.“ (překlad) — u/lukewhale

## Co říkají komentáře

- **NVFP4/MXFP4 funguje v praxi dobře** – někteří komentující (u/DustNearby2848, u/madbrain1976, u/thermal-runaway, u/lukewhale) uvádějí dobré výsledky s NVFP4/MXFP4, mimo jiné na modelech řady Qwen 27b.
- **Nedělejte z FP4 příspěvků tabu** – u/Sufficient_Local5025 a další se ohrazují proti omezování tématu; podle nich si má každý svůj případ užití hájit sám a nesouvisející příspěvky stačí přeskočit.
- **Většina nových inference enginů má nízkou kvalitu** – u/Daemontatox, u/FatheredPuma81 a u/ZenZombie117 mluví o forkách vytvořených převážně za pomoci AI („vibecoded“) a o tom, že mnohé nemají využití mimo upoutání pozornosti.
- **Výsměch nafouknutým benchmarkům** – vtipné a sarkastické odpovědi (u/38andstillgoing, u/RepulsiveRaisin7, u/tossit97531, u/tecneeq) zesměšňují přehnaná čísla o propustnosti (throughput).
- **Záleží na selektivní kvantizaci, ne na „vše do FP4“** – u/JumpingJack79, u/DistanceSolar1449 i sama úprava autora zdůrazňují, že citlivé vrstvy je nutné ponechat ve vyšší přesnosti.

## Rozpory a neověřené informace

- Autor tvrdí, že FP4 ničí malé husté modely a způsobuje halucinace, avšak několik komentujících (u/DustNearby2848, u/madbrain1976, u/lukewhale, u/thermal-runaway) uvádí, že s NVFP4/MXFP4 na modelech třídy Qwen 27b nemají žádné nebo jen nepostřehnutelné ztráty kvality. Jde o protichůdná tvrzení jednotlivých diskutujících.
- u/lukewhale tvrdí, že NVFP4 je na Blackwellu prakticky bezeztrátové FP8 a že není důvod používat cokoli jiného – to je v přímém rozporu s tvrzením autora, že enginy postavené čistě na FP4 kazí kvalitu.
- u/JumpingJack79 uvádí, že Q5 je pomalé a nevyplatí se, a doporučuje selektivní kvantizaci, zatímco autor a další hájí běžné Q4_K_M/XL kvanty jako dostatečné.
- Neověřená tvrzení komentujících: vtipné údaje o 3000 token/s na Raspberry Pi (u/38andstillgoing) a 1002 tok/s na GLM5.3 (u/elelem-123); tvrzení u/lukewhale, že NVFP4 je „téměř bezeztrátové FP8“; tvrzení u/Sufficient_Local5025, že MXFP4 Radiance build Qwen 27b je „naprostý game changer“; tvrzení u/madbrain1976 o provozu Qwen 3.8 27b v NVFP4 na 4× 5060 Ti a o snížení cloudového předplatného ze 100 na 20 dolarů měsíčně.
- u/WithoutReason1729 v komentáři uvádí, že příspěvek byl vybrán na Discord serveru a autor dostal zvláštní flair; jde o automatickou zprávu bota.

## Proč to je důležité

Diskuse ukazuje zásadní napětí v lokálním běhu modelů: honba za maximální propustností (throughput) přes agresivní kvantizaci může jít přímo proti kvalitě výstupu. Zatímco někteří považují NVFP4/MXFP4 za prakticky bezbolestné, jiní upozorňují, že úspěch závisí na selektivní kvantizaci citlivých tenzorů a vrstvení přesnosti. Vlákno zároveň odhaluje problém s důvěryhodností benchmarků a s kvalitou řady forků inference enginů, které se v komunitě objevují.

## Zdroje

- https://www.reddit.com/r/LocalLLaMA/comments/1wl56g2/please_stop_with_the_fp4_inference_engines_for/
- https://preview.redd.it/9n9it03lwmqh1.png?width=1200&format=png&auto=webp&s=e524247ab3a1c6b15aefcaf500b4447353ad5d29
- https://discord.gg/PgFhZ8cnWW
