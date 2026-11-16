# 1wxxz1n
**GPT-6 Astra vzal hotový kód pro kvantové obvody a zrychlil ho o dalších 10×**

r/singularity · u/141_1337 · 5. října 2026, 05:05 · 655 bodů / 72 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1wxxz1n/)

Autor sdílel obrázek s příběhem výzkumníka, který tři měsíce vyvíjel software pro návrh kvantových obvodů a dostal se na zhruba desettisícinásobné zrychlení oproti původnímu řešení. Pak vzal tenhle už hotový a vyladěný kód, předal ho modelu GPT-6 Astra a ten ho přes noc zrychlil o dalších zhruba desetkrát. Příspěvek vyšel s příznakem Singularity is Nearer.

Nejostřejší hádka se strhla kolem toho, v čem to zrychlení vlastně vězí. u/SpudsRacer tvrdí, že převod z C++ do Rustu sám o sobě rychlost nepřinese, bezpečnost ano, ale rychlost ne, a těžkou práci podle něj odvedly chytré inženýrské triky. Přidává se u/Infamous-Bed-7535 s tím, že portování C++ do Rustu se zisky rychlosti nemá nic společného, a u/Leather_Fall_1602 rýpe, že to zní chytře jen tomu, kdo nic neví o programování. Podobně to vidí u/ILikeAnanas, podle něhož se dá u akademika rozumně čekat, že původní kód v C++ byl příšerný a algoritmus průměrný.

Druhá linka vlákna naopak řeší, proč je právě ladění výkonu pro modely jako dělané. u/DublinLegend42 píše ze zkušenosti, že akademici programují hrozně, i když je kód čím dál důležitější, a právě tady čeká obrovské zlepšení. u/Deto to rozvádí: vymyslet algoritmus pro vědecký problém a dotáhnout ho na úrovni bitů, kompilátoru a stroje jsou dvě úplně jiné dovednosti a modely se na tu druhou hodí dokonale, protože mohou použít původní výstupy jako srovnávací bod a dál iterovat. Do stejného rámce to zasazuje u/Dangerous-Sport-2347 citátem o dostatečně přesné metrice, na které se dá rychle iterovat, v takových úlohách prý nejnovější modely předvádějí nadlidský výkon.

Ozývá se i praxe z firemních laboratoří. u/SYNTHENTICA popisuje výzkumný dům plný fyziků píšících kód, kde možnost nechat psaní na Claude místo přepisování nápadů softwarovými inženýry hodně zrychlila práci a zbytek vývojářů se mohl soustředit na produkt. Vedle toho běží vtipnější a skeptičtější nota: u/hornswoggled111 přiznává, že je to pro něj magie, a čeká, až budou hmatatelné přínosy v jeho životě očividnější, zatímco u/Medium_Apartment_747 glosuje, že za tu jednu noc vlastní OpenAI nový kvantový algoritmus. Sám autor u/141_1337 do diskuse přihodil odkaz na PDF článku a GitHub repozitář synthetiq.

Z vlákna tak zůstává hlavně obraz umělé inteligence jako nástroje na zrychlování vědeckého softwaru, kde člověk dodá nápad a model dotáhne implementaci do podoby, na kterou by v laboratoři nebyl čas ani trpělivost.
