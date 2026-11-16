# 50402212
**Anthropic rozebral paměť agentů: zápisky, sny a malé složky**

Hacker News · geoffbp · 7. listopadu 2026, 07:39 · 155 bodů / 86 komentářů · [diskuse](https://news.ycombinator.com/item?id=50402212)

Anthropic ve výzkumném textu rozebral, jak by si měl agent pamatovat zkušenosti mezi sezeními. Pamětí myslí znalost získanou z předchozích relací a uloženou tak, aby si ji mohl později znovu přečíst, a odděluje ji od změn vah při tréninku, učení uvnitř jedné konverzace i kompakce kontextu. Klíčové je podle něj rozhodnutí, co je v daném okamžiku dost důležité na zápis, protože příliš horlivé zapisování paměť spíš zahltí.

Článek to ukazuje na hraní Pokémon Red zhruba po deseti tisících krocích: Claude Sonnet 3.7 zapisoval skoro všechno a nasbíral 413 souborů ve 225 složkách, samostatný záznam ke každé bitvě či postavě, a získal jeden odznak. Claude Fable 5 si vedl jen devět souborů ve dvou složkách plus přehledový global.md se strategií a pravidly a získal čtyři odznaky. Jako lék na zastaralé či chybné zápisky popisuje Anthropic takzvané dreaming, kdy model přehraje poznámky proti původnímu transkriptu a opraví je – v ukázce z jeskyně Mt. Moon si tak opravil špatnou polohu PokéCenter a místo bloudění se vrátil zpět do jeskyně a došel do dalšího města.

Nejostřejší reakci přinesl uživatel troupo, podle kterého je článek nafouknutý a paměť ve skutečnosti nefunguje, protože jde jen o náhodné markdown soubory, které model stejně ignoruje. Podobnou zkušenost popisuje uživatel ashishact, jemuž Claude Code paměť slibuje a pak tutéž poznámku ukládá znovu a znovu. Uživatel anonymous908213 k tomu dodává, že označovat přepisování poznámek za snění je jen marketing snažící se vzbudit dojem vědomí.

Opačný pól drží praktici, kteří automatickou paměť rovnou vypínají. Uživatel yfontana píše, že v každém nástroji automatické vytváření vzpomínek zakázal a v Claude Code jich maže asi 95 procent, protože se většinou týkají jen právě řešeného úkolu a do dalších sezení jen zanášejí kontext. Přidávají se uživatelé sunaurus, hridyaagrawal nebo epihelix, podle nichž stačí projektový AGENTS.md a viditelný progress.md v repozitáři, které přežijí přechod mezi nástroji a jdou zkontrolovat v diffu.

Mezi těmito krajnostmi se objevuje snaha paměť ochočit ruční kurátorstvím. Uživatel russellbeattie si nechal od Claude Code vypsat paměť svého dlouho běžícího projektu a zjistil 61 souborů včetně indexu MEMORY.md, mezi nimi i dávno zapomenutý pokyn o velkém písmenu za dvojtečkou uložený jen pro daný projekt. Uživatel prtmnth na to má vlastní dovednost memory-prune, která automaticky vytvořenou vzpomínku posoudí a buď ji přesune do komentářů v kódu či AGENTS.md, nebo nejčastěji rovnou smaže. Uživatel 2001zhaozhao naopak slovo dreaming hájí jako trefnou analogii k řešení konfliktů v paměti, které dlouhodobý výkon sráží nejvíc.

Z diskuse tak vychází prosté ponaučení: psát si málo, ale ověřeně, a zbytek pravidelně promazávat.
