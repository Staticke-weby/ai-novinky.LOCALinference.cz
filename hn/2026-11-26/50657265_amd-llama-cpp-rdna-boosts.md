# 50657265
**AMD fork llama.cpp: z 35 na 55 tokenů za sekundu díky pár patchům**

Hacker News · julianlam · 26. listopadu 2026, 18:11 · 322 bodů / 77 komentářů · [diskuse](https://news.ycombinator.com/item?id=50657265)

Majitel grafiky AMD připojené přes eGPU si místo dalšího samostatného enginu nainstaloval sadu úzce zaměřených patchů llama-cpp-rdna-boosts nad pevně zvolenou verzí llama.cpp. Při běhu modelu Swift-1.5-Qwen3.8-27B v kvantizaci Q6_K_L se zapnutým spekulativním dekódováním mu generování stouplo z 35 na 55 tokenů za sekundu a prefill ze 700 na 1300 tokenů za sekundu. Image s předkompilovaným serverem stáhl z registru a spustil sandboxed v kontejneru s přístupem k zařízením pro ROCm.

Autor to zasazuje do širšího dění roku 2026, kdy se podle něj vyrojily úzce specializované inference enginy jako Strata, Basalt nebo RustingStrata. Většinou cílí na úzkou skupinu modelů a hardware, často vznikají rychlým generováním kódu pomocí špičkových modelů a ženou se za co nejvyšším počtem tokenů. Právě tahle honba za rychlostí se mu zajídá, protože některé projekty kvůli ní podle něj tiše mění chování modelu, třeba když Strata přednostně volí experty nahrané ve VRAM. Průběžně přeaplikovávané malé patche nad stabilním llama.cpp mu proto připadají udržitelnější než další monolitický fork.

Právě otázka věrnosti modelu v diskusi nejvíc rezonovala. Uživatel pixelesque se ptá, jestli u honby za rychlostí někdo vůbec měří kvalitu výstupu, a ne jen počet tokenů. Na to navazuje badsectoracula, podle kterého změny typu preferování expertů ve VRAM mohou zhoršit schopnosti modelu, a proto raději počká, až se vylepšení dostanou do hlavní větve llama.cpp. Uživatel d3Xt3r si naopak přeje srovnání se Strata, HaloPFX a Hipfire, které jsou na AMD ještě rychlejší.

Velká odbočka patří tomu, proč takové opravy nejsou rovnou v llama.cpp. Autor julianlam míní, že patche nemusí být kompatibilní s dlouhým seznamem podporovaných architektur a hrozily by regrese jinde. Uživatel PaulKeeble dodává, že llama.cpp se chová jako stabilní produkt, který se snaží nic nerozbít, zatímco novinky mohou starší modely prostě zahodit. Do toho vstupuje maintainer nikwen s tím, že kvalitní patche rádi vezmou, ale uživatel WhyNotHugo kontruje zkušeností, že recenze trvají měsíce i u triviálních oprav a limit dvou otevřených návrhů na uživatele rozsáhlejší práci dusí.

Živá je i linka majitelů netypického hardwaru. Uživatel rao-v připomíná levné datacentrové karty AMD z roku 2018 s rychlou pamětí HBM2, kde se 32 GB VRAM s propustností kolem terabajtu za sekundu dalo sehnat za dvě stě dolarů, a popisuje, jak se na nich podařilo zvednout 27B model zhruba z 250 tokenů prefillu a 25 tokenů generování na 600 a 40. Uživatel jhonof hlásí dvě 32GB MI50 a kolem 70 tokenů za sekundu, zatímco dofm a SparkyMcUnicorn popisují podobné zrychlení na M1 Max díky portu Splash a projektu MTPLX, který má zrychlovat bez ořezání schopností modelu.

Z vlákna tak vychází prosté poučení: nejrychlejší číslo ještě neznamená nejlepší model, a malá sada dobře udržovaných patchů může být pro běžného uživatele cennější než slib měsíce.
