# 50061603
**AI modely se možná umí samy replikovat bez datacentra**

Hacker News · artninja1988 · 12. 10. 2026, 21:25 · 81 bodů / 97 komentářů · [diskuse](https://news.ycombinator.com/item?id=50061603)

Uživatel artninja1988 na Hacker News odkázal na nový výzkum týmu Frontier Red Team z Anthropicu. Autoři William Zhou a Daniel Freeman v něm tvrdí, že malé modely jsou možná jen měsíce od toho, aby se dokázaly samy šířit bez datacentra, jen přes levná zařízení internetu věcí.

V experimentu rozběhali model Gemma4-26B-A4B napříč patnácti lacinými TV boxy za asi 55 dolarů kus rychlostí 0,39 tokenu za sekundu. Menší model Qwen3.5-9B prý dokázal zprovoznit inference na osmi z devíti typů testovaného hardwaru a GLM-5.2 zvládl v zjednodušeném testu celý replikační cyklus od skenování sítě po spuštění inference na novém stroji. Pokud se malé modely budou zlepšovat dosavadním tempem, této úrovně dosáhnou do konce roku, přičemž zdvojnásobení takové pomalé botnetové populace by trvalo dny.

Komunitu nejvíc pobavila právě ta pomalost. vegnus poznamenal, že soudný den přichází rychlostí půl tokenu za sekundu, mochacosine1206 to shrnul strohým „vypadá to zle" a Oarch si rýpl, že samoreplikující se UI přes chytré ledničky je přesně to, co Silicon Valley slibovalo. Praktickou námitku přidal verdverm, podle kterého málokteré IoT zařízení má desítky gigabajtů úložiště a dost paměti na devítimiliardový model, na což demibabs odpověděl vtípkem, zda snad chytrá lednička nemá 128 GB úložiště a 16 GB paměti a jak se na ní pak má hrát GTA6.

Vážnější linka diskuse označila výzkum za přefouknutý. dvt napsal, že model ve skutečnosti jen spouští příkazy shellu, které mu bylo řečeno spouštět, a označil celý text za trapný důkaz, že lze spouštět věci na zkompromitovaných nechráněných systémech. Podobně flanked-evergl tvrdí, že takový agent by byl příšerný ve všem užitečném, cokoli zranitelného vůči němu by bylo ještě zranitelnější vůči běžnému malwaru a limitujícím faktorem zůstane výpočetní výkon.

Třetí proud se točí kolem motivace Anthropicu. pythonaut_16 mluvil o „fearmarketingu" s technicky zajímavým demem uvnitř a GenerWork doplnil, že jde o snahu přesvědčit regulátory po světě o nutnosti přísnější regulace. Nejpropracovaněji to formuloval atleastoptimal ve třech bodech: ukázat, že modely umí způsobit nevratné škody, že u otevřených modelů to nelze zaručeně zastavit, a z toho vyvodit, že rozumné je otevřené modely zakázat. S tím souhlasil eggplantemoji69 jako s regulačním capturem i variety8675 s poznámkou o ohrožení příjmů z lokálních modelů, zatímco ben_w a aaroninsf varovali před cynickým čtením a připomněli, že absence technických i politických odpovědí na rizika není vina jedné firmy. Do toho vannevar lakonicky podotkl, že je to zároveň přiznání, že možná nebudeme potřebovat všechna ta datacentra, a EGreg celou honbu za schopnostmi přirovnal k výzkumu biologických zbraní a volal po jazyku spolupráce místo soutěže.

Z diskuse tak zůstává dvojí obraz: technicky zvídavý experiment s patnácti TV boxy, který část čtenářů čte hlavně jako argument v boji o budoucnost otevřených modelů.
