# 1xjvc08
**Lokální Qwen 27B na kódování selhává. 802 komentářů hledá příčinu**

r/LocalLLM · u/Major-Creative · 31. října 2026, 00:54 · 431 bodů / 802 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/)

Malá softwarová firma si pořídila vlastní stroj na experimenty s lokálním vývojem – Ryzen 5 5500, 32 GB DDR4 a RTX 3090 s 24 GB paměti. Nasadila na něj Qwen 3.8 27B se 128K kontextem jako náhradu za Claude Sonnet 5.5, jenže výsledek je prý zoufalý: model se ztrácí v zadání, točí se v opakovacích smyčkách a nedokončí ani jednoduché úkoly. Přitom pracuje ve stejném kořenu projektu a se stejnými .md soubory s pokyny a dokumentací, se kterými Claude úkoly samostatně plní.

Diskuse se hned stočila k jednomu podezřelému. Nejvýše hodnocený komentář u/Repulsive_Initial308 lakonicky píše, že na první pohled pozná, že firma jede na Ollamě – a autor to v dodatečné editaci potvrdil. Přidává se u/Express_Quail_1493 s tím, že opakující se smyčky jsou typický znak špatné konfigurace, šablony chatu nebo streamování tokenů, a u/LegitimateCopy7 radí Ollamu zahodit, pokud má jít o nástroj a ne hračku. Jako lepší start pro začátečníky zmiňují LM Studio s Bionic enginem nebo čisté llama.cpp a Stratu.

Druhá velká linka řeší kvantizaci a nastavení, o kterých příspěvek původně mlčel. u/HolaUsername, u/initalSlide i u/Apprehensive_Stop314 se ptají na totéž: jaký přesně quant, jaká teplota a parametry, jaký harness a engine. u/FastHotEmu tvrdí, že ani v Q4 model normálně funguje výborně, takže jde o špatný model, engine nebo konfiguraci. Podobně u/Erik-Zandros upozorňuje, že na 24 GB VRAM při 128K kontextu firma pravděpodobně jede silně ořezanou 4bitovou kvantizaci, případně model přetéká do systémové RAM, a u/aithosrds označuje Q4 za minimum a doporučuje vypnout nebo stáhnout reasoning.

Třetí část vlákna firmě domlouvá, že Qwen nelze nasadit jako přímou náhradu za Claude se stejnou dokumentací a očekáváním. u/dreamyrhodes radí mluvit s malým modelem jako s juniorem – krok za krokem, po funkcích, s rekapitulací a dokumentováním každého kroku. u/jefoce popisuje, že model zesílí rozsekáním do subagentů s malou odpovědností pro kódování, revize či databázi a přísnými pokyny v XML značkách s velkými písmeny, a u/aithosrds varuje, že za polovinou kontextu se model začíná točit, takže má smysl držet úkoly spíš do 64K.

Zároveň se ozývají lidé, kterým Qwen 27B pro kódování funguje. u/Bagelsarenakeddonuts na něm napsal desítky tisíc řádků Rustu, které prošly testy i kontrolou jinými modely, a chválí odlehčenou swift verzi s kratším přemýšlením. u/dsdt lakonicky hlásí, že lokální Qwen opravuje chyby, které Claude nechal v repozitářích, u/pioo84 na něm postavil celé androidí aplikace a u/soulman901 si nechal vygenerovat hry včetně klonu Pac-Mana. Nejvtipněji rozdíl vystihl u/an0maly33 parodií vnitřního monologu modelu, který u prosté chyby donekonečna přešlapuje, zatímco větší Qwen Next Flash prý jen přečte, opraví a je hotovo.

Z vlákna tak nakonec plyne spíš povzbudivá zpráva: problém nejspíš není v samotné váhové třídě 27B, ale v kombinaci Ollamy, nízké kvantizace, přetíženého kontextu a cloudových návyků.
