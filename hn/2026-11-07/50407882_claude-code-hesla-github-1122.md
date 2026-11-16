# 50407882
**Claude Code uložil hesla do 1122 veřejných souborů na GitHubu**

Hacker News · shmulc · 7. listopadu 2026, 21:45 · 305 bodů / 208 komentářů · [diskuse](https://news.ycombinator.com/item?id=50407882)

Bezpečnostní společnost Apiiro upozornila, že ve veřejných repozitářích na GitHubu našla 1 122 souborů s přihlašovacími údaji, které si tam uložil Claude Code po kliknutí na volbu Don't Ask Again. Schválené příkazy včetně hesel a klíčů se tak zapsaly do souborů uvnitř projektu a po commitu je mohl číst kdokoliv na internetu.

Podle autorů výzkumu je jádrem problému umístění souboru .claude/settings.local.json, který vzniká přímo v adresáři projektu a Claude Code ho přidá jen do globálního gitignore, nikoli do gitignore samotného repozitáře. Na čerstvém klonu nebo druhém počítači se tak tváří jako běžný soubor a nic nebrání jeho verzování. Ze 1 105 trasovaných repozitářů přitom soubor ve 539 případech změnil commit, u kterého je Claude uvedený jako spoluautor.

Diskuse se hned stočila k tomu, jestli je titulek fér. Uživatel qezz namítá, že soubor leží prostě v repozitáři a veřejný je jen tehdy, když je veřejný i repozitář. Autor výzkumu shmulc odpovídá, že všechny nálezy pocházejí z veřejných repozitářů, ale i v soukromém se tajemství šíří s každým klonem a forkem a zveřejní se ve chvíli, kdy se zveřejní repozitář. Uživatel mschuster91 dodává, že ani uvnitř firmy nikdo nechce, aby heslo k produkční databázi viděl každý vývojář s přístupem.

Podobně to vidí uživatel Aurornis, podle kterého samotné tlačítko hesla nevystaví – vystaví je až kombinace ručně schváleného příkazu s tajemstvím přímo v textu a commitu lokálního nastavení do veřejného repozitáře. Shmulc ale trvá na tom, že právě tohle lidé nečekají: soubor se tváří jako lokální, ve skutečnosti se ale commitne jako cokoliv jiného. Uživatel toppa33 to shrnuje jako nešťastnou výchozí hodnotu, kdy jedno kliknutí dostane hesla do souborů, které lidé verzují.

Do vlákna pak vstoupil Boris Cherny z týmu Claude Code s tím, že soubor nemá být v source controlu a firma zvažuje, jak podobným únikům zabránit. Doporučuje zapnout secret scanning a místo ručních pravidel povolení používat automatický režim, který je podle něj bezpečnější a je ve výchozím nastavení zdarma ve všech tarifech. Reakce ale byla ostrá – uživatel JohnMakin píše, že bezpečnostní best practice je tajemství do souborů vůbec nezapisovat, a uživatel doginasuit mluví o přehazování odpovědnosti za předvídatelnou chybu.

Právě doporučení automatického režimu vyvolalo další spor. Uživatelé bluebands a markasoftware pochybují, že je automatika bezpečnější, když v citlivých případech stejně ukládá trvalé výjimky. Uživatel 80fj0348i naopak popisuje, že mu automatický režim odmítá i bezpečné operace, takže se bez ručních pravidel v provozu neobejde. Praktičtější křídlo debaty navrhuje obrácenou logiku výjimek pro soubory jako .env, proxy, která agentovi podstrčí neškodné náhradní tajemství, nebo důsledné ignorování nastavení na úrovni Gitu.

Z vlákna tak zůstává jednoduché ponaučení: co vypadá jako lokální nastavení, může po prvním commitu žít vlastním životem na GitHubu.
