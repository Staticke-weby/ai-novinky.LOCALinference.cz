# 1y0e59m
**Kitten-TTS-2: nejmenší model má 4 MB a mluví rychleji než realtime**

r/LocalLLaMA · u/ElectricalBar7464 · 19. listopadu 2026, 17:44 · 301 bodů / 96 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y0e59m/)

KittenML vydal rodinu supertitěrných vícejazyčných modelů pro převod textu na řeč Kitten-TTS-2 Pico se 7 miliony parametrů, Nano se 17 miliony a Mini s 80 miliony. Nejmenší Pico má 4 MB a na jednom vlákně procesoru smartphonu běží rychleji než v reálném čase.

Podle popisu autora je Nano s 8,8 MB a osmi jazyky kvalitnější variantou a Mini se 48 MB zvládne šestnáct jazyků. Kód i váhy jsou pod licencí Apache 2.0 a váhy leží na Hugging Face. Nová řada slibuje proti předchozí generaci zhruba šestkrát menší Pico, výrazně lepší kvalitu a vícejazyčnou podporu s během na telefonu či Raspberry Pi na jediném vlákně.

Nejživější debata se vede o kvalitě výslovnosti. U/Competitive_Ad_5515 chválí angličtinu a němčinu, ale stěžuje si, že model skoro úplně ignoruje čárky a tečky a všechno spojuje do jedné věty. U/foundafreeusername naopak oceňuje, že zatímco Kokoro komolí novozélandské názvy měst, Kitten je zvládá překvapivě dobře. U/Lorian0x7 dodává, že roztomilé hlasy slyší zatím jen v angličtině.

Druhá linka řeší, co takto malý model umožní na okraji sítě. U/jomic01 poznamenává, že čtyřmegabajtový model je dost malý na to, aby se přibalil přímo do aplikace místo stahování hlasového balíčku při prvním spuštění. Na to navazují dotazy, jestli půjde provozovat ve WebAssembly, kdy budou váhy pro audio.cpp a zda je kompatibilní se sherpa-onnx. U/Devatator_ by ho hned nasadil do vlastního asistenta, jen co vyřeší úspornou detekci budicího slova, a u/No-Estimate-362 přemýšlí o hře, kde by stejná postava musela vyjadřovat vztek nebo stres.

Zbytek vlákna patří přáním do budoucna a srovnávání. U/tat_tvam_asshole se ptá na klonování hlasu, u/TokenLearner na portugalštinu a u/oulmax na další jazyky. U/foundafreeusername by uvítal mandarínštinu a mladé hravé mužské hlasy ve stylu anime postav. U/geearf řeší, jestli má smysl přecházet z BlueTTS, a u/coder543 postrádá pořádné srovnání kvality všech velikostí v grafech a preferenčních testech.

Z diskuse tak vychází drobný model s velkými ambicemi: vejde se skoro kamkoliv, ale o přízeň si musí říct výslovností a hlasy pro další jazyky.
