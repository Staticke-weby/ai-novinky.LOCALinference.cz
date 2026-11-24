# 50618513
**Claude Ship: agenti přebírají review, opravy i schvalování PR**

Hacker News · matthieu_bl · 23. listopadu 2026, 21:14 · 41 bodů / 12 komentářů · [diskuse](https://news.ycombinator.com/item?id=50618513)

Anthropic spustil v betaverzi Claude Ship pro týmy na plánech Team a Enterprise s repozitáři na GitHubu. Služba má převzít všechno, co se děje po otevření pull requestu, od revize přes opravy až po rozhodnutí o mergi, aby týmy vydávaly kód stejně rychle, jako ho dnes s agenty píšou. Firma se ohání čísly z vlastního týmu Claude Code, kde se od června do září počet mergnutých PR více než zdvojnásobil a podíl vrácených změn klesl o víc než 40 procent.

Systém stojí na třech částech: Code Review nabízí tři úrovně hloubky od Quick po Deep, PR Steward drží request zelený, řeší padající CI, konflikty i připomínky a po každém pushi vypíše, co změnil a jak to vrátit, sám ale merge neschvaluje. O něm rozhoduje teprve Claude Approvals podle politiky uložené jako soubor v repozitáři, obdoby chytřejšího CODEOWNERS, kterou firma doporučuje nejdřív pustit v pozorovacím režimu. Vývojář si novinku vyzkouší příkazem /ship přímo v Claude Code, spotřeba se účtuje po tokenech s možností nastavit limity a Enterprise mohou získat nejméně 10 tisíc dolarů v kreditech.

Největší ohlas sklidila ironie, že si umělá inteligence už píše, čte, reviduje i merdžuje kód sama. Uživatel hiddenvulkcan glosuje, že naštěstí máme aspoň umělou inteligenci, která to po té umělé inteligenci kontroluje, a uživatel fwlr celou evoluci shrnul do čtyřstupňového posunu od „Claude píše kód, ale já ho čtu" až po „Claude píše, čte, reviduje i merdžuje" s dovětkem, že právě tam už jsme. Uživatel tersers k tomu přihodil logický další krok, že Claude poběží přímo na počítači uživatele a bude kód opravovat v reálném čase.

Z praktičtějšího soudku zaujala úvaha uživatele bob1029, který to chce navrhnout vlastnímu týmu. Hodně kódu u nich vzniká s modely OpenAI, a právě proto mu dává smysl nechat kontrolu na modelu od jiného dodavatele jako rozumné oddělení odpovědnosti.

Oproti tomu uživatel viklove nechápe, pro koho nástroj vlastně je. Popisuje ho jako centralizované vymáhání pravidel pro týmy s nízkou důvěrou a tvrdí, že bota kontrolujícího připomínky a posílajícího opravy si šikovný tým postaví trivialně sám, nejlépe ještě před vznikem PR a bez závislosti na jednom dodavateli. Podobně laděná je i odbočka, zda jde o pověstnou softwarovou továrnu: zatímco uživatel Atotalnoob ji přirovnává spíš k nabídce Port.io, uživatel verdverm diskusi shodil odkazem na žertovný web o uctívání Clauda.

Z vlákna tak nakonec nejvíc trčí rozpor mezi slibem, že review přestane brzdit práci, a obavou, že se z člověka stane jen divák vlastního vývoje.
