# 50579297
**Programátor si nechal AI napsat FPGA, na kterém běží LLM**

Hacker News · ankitvgupta · 20. listopadu 2026, 19:15 · 132 bodů / 50 komentářů · [diskuse](https://news.ycombinator.com/item?id=50579297)

Programátor Ankit Gupta neměl s hardwarem téměř žádné zkušenosti a Verilog nikdy nepsal, přesto rozběhl jazykový model na přeprogramovatelném čipu FPGA v cloudu AWS. Místo studia hradel a průběhů signálů nechal pracovat coding agenty, které psaly nízkoúrovňové C++ a Verilog a samy ověřovaly výsledky. Z prvního funkčního, ale pomalého návrhu se smyčka postupně dostala ze 6,43 na 213 tokenů za sekundu, tedy na více než třiatřicetinásobek.

V textu popisuje, jak cloudový agent v prostředí Conductor běžel několik dní téměř samostatně a autor ho spíš jen povzbuzoval výzvami k větší kreativitě a dalšímu zrychlení. Vystřídaly se v něm modely Astra a Opus, výsledkem byly zhruba tři miliony řádků pokusného kódu a třicet milionů řádků zpracovaných výstupů. Ani podrobný návrh od zakladatelů startupu DeepGrove s ternárními vahami podle zpětného pohledu agenta design zásadně nezměnil, nejvíc pomohla procesní rada neulpívat na hodinových simulacích a rychleji se dostat k výsledkům na hardware.

V diskusi nejvíc rezonovala cena experimentu, 10 000 dolarů za tokeny Claude a OpenAI. Uživatel jluxenberg ji označil za přehnanou kuriozitu mimo vlastní rozpočet, ricardobeat připomněl, že šlo o startupové kredity, tedy v praxi zdarma, a mixtureoftakes s adastra22 dodali, že paušální předplatné za 200 dolarů měsíčně v přepočtu na ceníkové ceny odpovídá mnohatisícové útratě. Vedle peněz se řešila i velikost: datadrivenangel podle stop v textu usuzuje na model Maple s 20 miliardami parametrů, zatímco ilaksh namítá, že aktivní je jen kolem miliardy parametrů v malé kvantizaci, a proto nejde o průlom.

Technická linka se stočila k tomu, zda mají FPGA pro inference vůbec smysl. Uživatelé nomel a numpad0 připomínají, že logika postavená na vyhledávacích tabulkách spotřebuje mnohonásobně víc plochy čipu než přímá hradla a za rekonfigurovatelnost se platí rychlostí, spotřebou i cenou. Praktickou zkušenost přidal mikeayles: na běžném FPGA rozběhl několik modelů, malý se třemi miliony parametrů dostal na 59 000 tokenů za sekundu, ale osmimiliardový s pamětí DDR se zasekl kolem čtrnácti, a právě rychlá paměť HBM je podle něj tím kouzlem, které to celé umožní.

Zbytek vlákna je oslavou i parodií vibe codingu. Uživatel chalkycrimp chce prostě vidět kód, codekansas radí jako další krok vyladit trénování přímo pro zvolenou architekturu FPGA a cpldcpu ukazuje vlastní generátor v C s modelem Opus 4.5 s tím, že implementace transformerů je novým „ahoj světe" programování s AI. Do toho reuben364 popisuje, jak podobně postavil jazyk s typovým systémem, backendy včetně Verilogu i implementaci RISC-V, na které na desce Arty běží Doom, a tracerbulletx vypráví, jak si po večerech znovu postavil celou firemní platformu pro reklamu a správu zákazníků. Jen kooi se při čtení autorových povzbudivých promptů styděl a čekal by aspoň špetku odbornosti.

Zůstává tak obrázek doby, kdy největší výkon nepřidává chytřejší rada, ale rychlá iterace a velký rozpočet na pokusy.
