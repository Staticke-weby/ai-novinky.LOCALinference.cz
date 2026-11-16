# 1xodizg
**Claude Code rozchodil head tracking z AirPods 3 na Linuxu. Nikdo to předtím nedokázal**

r/ClaudeAI · u/Matteocean · 5. listopadu 2026, 09:31 · 504 bodů / 62 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xodizg/)

Autor chtěl na Linuxu ovládat myš pohybem hlavy pomocí gyroskopu v AirPods 3, který tam normálně slouží pro prostorový zvuk. Všechny open-source projekty přitom trojky označovaly za nepodporované. Po odpoledni stráveném s Claude Code se mu to povedlo: sluchátka začala posílat data o pohybu zhruba na 200 Hz a vzniklý kód zveřejnil na GitHubu jako mousepods.

Práci si podle vlastních slov rozdělili tak, že Claude napsal většinu kódu a on testoval na živých sluchátkách a dělal rozhodnutí. Zlom přišel, když nechal v pozadí běžet agenty, aby prohrabávali cizí projekty. Jeden z nich našel odpověď v kódu iOS frameworku: AirPods 3 mluví jiným protokolem než modely Pro a Linux jejich senzory skrýval kvůli nastavení velikosti Bluetooth paketů. Po opravě tohoto nastavení se stream dat rozjel.

Diskuse se okamžitě rozjela směrem k hrám. Nejvýše hodnocený komentář u/1NFail sní o závodění, kde by se člověk přirozeněji podíval do bočních zrcátek, a zmiňuje i letecký simulátor nebo GTA 6. Na něj navazuje u/Dutch_Razor s nápadem použít sluchátka jako náhradu eye trackingu pro rozhlížení v kokpitu. Ozývá se i u/Knite_0wl_1337, že by se takové testy měly dělat na dalším hardwaru, a majitel AirPods Pro 3 u/GilbertRPG se hlásí, že to zkusí napojit a případně přispěje.

Vedle her se řeší i praktičtější využití a limity. u/pazra doufá, že by se zbavil bolesti zápěstí, kdyby mohl odložit myš, u/pikinz žertuje o přepínání videí trhnutím hlavy při doomscrollingu a u/Njagos fantazíruje o provizorním VR headsetu z AirPods a AR brýlí. u/AI_Bullish se ptá na výdrž baterky při tak hustém streamování pohybových dat a u/Tough_Temporary_377 zjišťuje, jestli existuje něco podobného pro macOS. Nejstručnější shrnutí pobavilo nejvíc: u/Different_Lab830 píše, že celé to složité reverzní inženýrství skončilo u nastavení velikosti paketů, na které nikdo nesáhl, což je prý vrchol Linuxu.

Zkušenost rezonuje i u dalších stavitelů. u/matthias81f popisuje skoro stejnou dělbu práce při vývoji aplikace pro televizi Samsung: Claude staví, instaluje, čte logy a mačká tlačítka po síti, člověk testuje před skutečným zařízením. u/Over-Independent4414 v tom vidí hlavní ponaučení vlákna, tedy zadat agentům různé části problému a nechat je pracovat paralelně. Pro čtenáře je pointa jednoduchá: levná sluchátka, která už mají v šuplíku, se mohou změnit v bezdrátový head tracker pro hry i práci s počítačem.
