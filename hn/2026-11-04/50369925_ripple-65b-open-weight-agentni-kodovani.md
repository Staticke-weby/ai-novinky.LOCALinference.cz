# 50369925
**Ripple-65B: americký open-weight model od pěti lidí míří na agentní kódování**

Hacker News · Philpax · 4. listopadu 2026, 19:53 · 271 bodů / 97 komentářů · [diskuse](https://news.ycombinator.com/item?id=50369925)

Laboratoř Ricursive Intelligence vydala Ripple-65B Preview, hustý open-weight model trénovaný od nuly na 12 bilionech tokenů. Model s kontextem až milion tokenů míří na agentní kódování a podle firmy dosahuje v testu Terminal-Bench 2.1 skóre 80,52, tedy nejlepšího výsledku mezi americkými otevřenými modely. Vznikl přitom jako vedlejší produkt interní platformy pro návrh čipů, jejíž neveřejná varianta pomáhá navrhovat hardware.

Oznámení staví hlavně na efektivitě: celý vývoj od nuly včetně ladění dat a posttréninku měl stát 32 milionů dolarů, tedy desetinu nákladů předchozího nejlepšího výsledku. Firma vsadila na modernizovaný hustý Transformer místo směsi expertů, vlastní syntetická data a úsporný posilovací trénink se 1,4 milionu průchodů, model je k dispozici na Hugging Face, Together AI, GMI Cloud a OpenRouter.

Největší rozruch v diskusi způsobilo slovo americký v titulku. wmf gratuluje, ale připadá mu jako špatná vizitka, že firma vůbec nezmiňuje ostatní otevřené modely, flatline souhlasí, že srovnání nedává mimo autory smysl. tedivm to glosuje hláškou o tom, že jsme vždy byli ve válce s Eurasií a je prostě snazší předstírat, že Čína neexistuje, když tak drtivě vede, advael si zase utahuje z neustálého zužování kategorie, až ze SOTA zbyde nejlepší americký otevřený model. Naopak stewartpark a swiftcoder namítají, že právě domácí původ může být pro část zákazníků včetně vládních agentur rozhodující, a frinxor dodává, že segmentace dává smysl.

Konkrétní čísla přinesl 2001zhaozhao: Ripple má 80,5 bodu, zatímco větší čínský Qwen 3.8 Flash Next dosahuje 84,3 a menší Qwen 3.8 s 27 miliardami parametrů 73,0, takže bude záležet na tom, jak moc je výsledek vyladěný na benchmark. syntaxing poznamenává, že když příspěvek nezmiňuje Qwen, nebývá výkon nic moc, a ethan-boneh doplňuje, že Qwen 3.8 s 27 miliardami dává 73 procent na Terminal-Bench 2.1. karmakaze firmě vyčítá dvojité vybírání třešniček, když pro velikostní srovnání bere Inkling místo lepšího a menšího Beam 1.0 a v grafu ukazuje Nemotron 3 Ultra místo menšího a lepšího Nemotron 3.5 Super, yorwba pak počítá, že náskok 0,42 procentního bodu před druhým nejlepším modelem ve vlastním testu je sotva významný.

Zbytek vlákna odlehčují slovní hříčky kolem názvu. dofm se ptá, zda teď máme Recursive a Ricursive, oba dělající jazykové modely, xyzrt odpovídá, že jeden staví sebezdokonalující se umělou inteligenci přes společný návrh čipů a ten druhý jen přes software. giwook vidí v tom rekurzi a wmf navrhuje založit Rickursive, laboratoř, která tě nikdy neopustí a nikdy tě nezklame. Mezi vtipy probleskne i praktické přání jszymborski po 27miliardové destilaci a otázka 6thbit, co vlastně americký znamená, na kterou conception odpovídá prostě tím, že za modelem stojí americká laboratoř.

Z diskuse tak zůstává rozpor mezi solidním inženýrským příběhem levného hustého modelu a marketingem, který si vítězství nejdřív ohraničil hranicemi.
