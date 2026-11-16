# 1xkoi9g
**DeepSeek zveřejnil prototyp Super-agenta, který si sám bere práci z GitHubu**

r/singularity · u/yogthos · 1. listopadu 2026, 00:32 · 875 bodů / 18 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xkoi9g/)

Tým DeepSeek Harness zveřejnil na GitHubu dsh-superagent, proaktivního coding agenta pro jeden repozitář zabaleného pro DeepSeek Harness. Prezentuje ho výslovně jako open-source výzkumný prototyp pod licencí MIT, nikoli jako oficiální produkt DeepSeeku ani jako svou interní verzi.

Podle repozitáře agent naslouchá GitHubu a volitelně Feishu. Když ho pověřený člověk požádá o práci, otevře work item, pracuje na něm ve vlastní session a složce a odpoví v původní konverzaci, typicky pull requestem, zatímco webový panel ukazuje jen to, co potřebuje člověka. Autoři přiznávají, že značnou část kódu napsali coding agenti, takže prototyp může obsahovat chyby a nekonzistentní styl, a se zprovozněním má pomáhat další AI agent krok za krokem podle SETUP.md.

Nejvýše hodnocený komentář od u/michaelTM_ai vzkazuje ostatním, ať si přečtou dokumentaci. Samotný agent je podle něj docela normální, výjimečné je, jak usilovně je navržený tak, aby mlčel. Jádrem filozofie z dokumentu 000-philosophy je brát si co nejméně lidské pozornosti: jedná jen na zmínku od povoleného člověka nebo podle pravidla, které napsal tým, a pravidlová proaktivní práce začíná v režimu pouze se záznamem, kdy jen loguje, co by udělal.

Stejný uživatel vypichuje detaily, které podle něj stojí za okopírování. Příkazy v shellu se po pěti sekundách přesouvají na pozadí, aby pracovník mohl dál číst nové zprávy během běhu, a úkoly na pozadí mají po každém kroku nejvýš třicet minut. Zdravý stav pak podle něj nezabírá žádné místo.

Zbytek vlákna řeší, jestli je to vůbec něco velkého. u/Perfect-Campaign9551 se ptá, jestli to není prostě GitHub bot a nic moc složitého, u/MisfiledCentury se ptá, jestli je to jako dots pro GitHub repozitář, zatímco u/mWo12 kontruje, že přesně takhle by to mělo vypadat u OpenAI. Do toho u/Foreign_Skill_6628 vtipkuje o přicházejícím černém pondělí pro AI průmysl a o tom, že zveřejnění po pátečním zavření burz nebyla náhoda, což právě u/michaelTM_ai odmítá s tím, že jde o MIT výzkumný prototyp pro jedno repo. Úplný závěr patří u/analyticaljoe s provokací, jestli se dá použít na výrobu biologické zbraně, protože ji vyrábět nechce, ale živě ho zajímá, jestli by to šlo.
