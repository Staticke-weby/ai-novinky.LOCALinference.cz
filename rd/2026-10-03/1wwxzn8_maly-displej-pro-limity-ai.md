# 1wwxzn8
**Malý displej z AliExpressu ukazuje limity Codexu a Claude**

r/ChatGPT · u/Senior_Wear4670 · 3. října 2026, 23:05 · 512 bodů / 61 komentářů · [diskuse](https://www.reddit.com/r/ChatGPT/comments/1wwxzn8/)

Autor koupil na AliExpressu malé hodiny za 5 650 wonů a předělal je na ukazatel svých limitů v Codexu a Claude. Počítač obraz vykreslí a pošle ho na displej přes Wi-Fi, takže v hodinách zůstal původní firmware. Snímek v příspěvku ukazuje jen ukázkové hodnoty, řádek s Grokem je rozpočet pro CLI, ne limit předplatného, a kód k projektu autor zveřejnil na GitHubu pod názvem click6067-ship-it/token-tv.

Největší ohlas měla prostá poznámka u/Pasto_Shouwa, že právě použití hodin z AliExpressu to dělá mnohem lepším. Autor přitakal, že titěrná krabička je polovina kouzla, a u/Plus_Information_990 dodal, že posílat obraz přes Wi-Fi a nesahat na firmware je chytré, protože tak hodiny nejde bricknout. Ten by si je prý klidně postavil na stůl, zatímco u/Bakuryoko v nápadu vidí hlavně úzkost – na to autor odpověděl, že je to takový malý monitor stresu.

Pak se diskuse stočila k technice. u/lulzxdxdxd se ptal, jak často počítač hodnoty posílá a odkud čísla pro Codex a Claude vůbec bere, jestli z endpointů, lokálních logů, nebo stahováním dashboardu. Autor vysvětlil, že výchozí interval je pět minut s možností zkrátit ho až na 60 sekund, počítač vždy vyrendruje obrázek o velikosti 240x240 a nahraje ho jen tehdy, když se změnil. Claude čte z endpointu pro využití přes přihlášení v CLI a Codex z funkce app-serveru pro čtení limitů, upozornil ale, že část kolem Claude není dokumentované veřejné API, a tak se může časem změnit.

Řešil se i samotný hardware a co s ním dál. Na dotazy, kde tak levný displej sehnat, autor poradil hledat výrazy GeekMagic SmallTV nebo smart weather clock a dodal, že testoval verzi SD_PRO s funkcí fotoalba, takže podobně vypadající hodiny nemusejí být kompatibilní. u/Joe_Franks si na stejných hodinách chce udělat odbočku pro data z počítače a zachovat nahrávání malého gifu, u/Chess-Gitti by projekt nejraději viděl jako Docker kontejner nebo doplněk pro Home Assistant. Autor upřesnil, že hodiny si nic samy nestahují, počítač limity přečte, obrázek nakreslí a protlačí ho přes stávající funkci pro nahrávání fotek, přičemž webové rozhraní slouží jen k nastavení a náhledu.

Vedle toho se objevily i alternativy. u/K_M_A_2k napsal, že jemu na stejný přehled stačí tlačítka na Stream Decku s pět hodinovým a týdenním přehledem pro Claude a týdenním pro ChatGPT. Na nápad udělat z ukazatele aplikaci pro Apple Watch autor odpověděl, že čtení využití zatím běží na počítači, takže hodinky v projektu nejsou, a u/Grouchy-Western-5757 dodal, že by ji postavil, kdyby nemusel platit vývojářský účet u Applu.
