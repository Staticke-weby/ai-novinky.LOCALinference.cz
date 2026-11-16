# 1xozfcv
**Anthropic slévá 30 tisíc změn denně, ale 98 procent issue zůstává bez řešitele**

r/ClaudeAI · u/nseavia71501 · 6. listopadu 2026, 01:48 · 867 bodů / 101 komentářů · [diskuse](https://www.reddit.com/r/ClaudeAI/comments/1xozfcv/)

Anthropic podle vlastního engineering blogu slévá přes 30 tisíc změn kódu denně, ale ve veřejném repozitáři Claude Code zeje 16 060 otevřených issue, z nichž 15 766 nemá přiřazeného řešitele. Autor příspěvku, který se představuje jako seniorní vývojář, upozorňuje, že mezi měsíce či roky starými hlášeními jsou i vážné bezpečnostní chyby, třeba únik e-mailu uživatele v hlavičce User-Agent třetím stranám. Kontrastuje to s tím, že firma má kapacitu na drobnosti typu pixelovaného srdíčka ve Windows aplikaci, které se objeví po několikerém kliknutí.

Nejvíc hlasů dostala ostrá diagnóza od u/lubujackson: všechno je prý „vibed“, inženýři pracují v šíleném tempu s hejny agentů a lidské code review už se nedělá. Nikdo podle něj nechce řešit architekturu ani technický dluh a za opravu bezpečnostní chyby nikdo nedostane bonus pět milionů dolarů, všichni se prý snaží odemknout nový trh v hodnotě bilionů nebo přepnout vypínač k pověsti tvůrce umělé obecné inteligence.

Věcnější linka hledá pro Anthropic polehčující okolnosti. u/Pure_Material_9235 tipuje, že firma se bojí prompt injection při automatickém řešení issue z veřejného GitHubu, a proto chce u všeho člověka, což ji zásadně brzdí. Podobně u/TechgeekOne a u/salazka připomínají běžnou praxi, kdy GitHub slouží jen jako veřejné zrcadlo a skutečné třídění běží v interním systému z důvodů bezpečí a soukromí zaměstnanců.

Tuto teorii podporuje zkušenost u/digabdo, kterému jeho hlášení bez komentáře zavřeli pro neaktivitu, ale všiml si, že problém mezitím zmizel – usuzuje z toho, že Anthropic tiše sleduje, třídí a opravuje interně pomocí agentů, jen pokrok na GitHubu nedokumentuje. Naproti tomu u/East-Acanthaceae-879 krotí samotné číslo 30 tisíc: nejde prý o žádný vlastní systém správy verzí, jen o fronty na slučování s průběžnou integrací a spoustu malých pushů, což dělá Meta s Facebookem už dávno.

Zbytek vlákna je skeptičtější k motivacím firmy. u/abeuscher píše, že na bezpečnost nejsou žádné regulace, a dokud nákupní rozhodnutí nestojí na počtu otevřených issue, firmu nic nenutí je opravovat. u/TeamTomorrow to rámuje jako střet značky bezpečnosti se značkou rychlého dodávání, u/uninchar přihodil srovnání s jinými repozitáři a u/ShodoDeka shrnuje pocit mnohých, že nasypat hromadu okrajových funkcí je prostě snazší než řešit chyby s možnými dominovými dopady.

Z diskuse tak zůstává otázka, kterou autor položil na začátku: když Claude umí psát, revidovat a slévat kód v takovém měřítku, proč ho firma systematicky nepoužívá na třídění a eskalaci vážných chyb místo toho, aby se opravovalo až to, co se stane virálním na Redditu.
