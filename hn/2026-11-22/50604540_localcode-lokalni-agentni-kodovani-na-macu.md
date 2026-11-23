# 50604540
**Localcode: agentní kódování s lokálními modely na Macu jedním příkazem**

Hacker News · mjwsolo · 22. listopadu 2026, 23:18 · 46 bodů / 13 komentářů · [diskuse](https://news.ycombinator.com/item?id=50604540)

Localcode je open-source agent pro kódování, který běží celý lokálně na Macu s Apple Silicon a neposílá kód do cloudu. Instaluje se příkazem uv pip install localcode a v adresáři projektu se spouští prostým localcode. Kód je pod licencí Apache 2.0 a vyžaduje Python 3.10 nebo novější, k tomu Mac s macOS 13 a alespoň 16 GB sdílené paměti.

Podle popisu na GitHubu umí číst a upravovat soubory v projektu, sám pouštět testy, buildy, Git i shellové příkazy, hledat v kódu podle jména, obsahu a struktury a dokonce rozjet aplikaci a zkontrolovat, že odpovídá. Nabízí výběr ze 12 modelů ve 169 kvantizacích, stahování z Hugging Face na pozadí a přepínání příkazem /models, přičemž doporučí nejschopnější model, který se vejde do paměti. Běžící model umí vystavit i dalším lokálním aplikacím přes /server nebo příkaz localcode api s OpenAI kompatibilním endpointem.

Nejživější debata se stočila ke jménu. Uživatel mark_l_watson upozornil, že stejnou značku nese i aplikace na getlocalcode.app, se kterou na 64GB Macu provozuje DeepSeek. Autor mjwsolo odpověděl citátem o dvou těžkých věcech v informatice, kešování a pojmenovávání, a vysvětlil, že jejich projekt je od dubna vyvíjené open-source CLI postavené na llama.cpp a opencode, zatímco zmíněná aplikace je nativní s vlastním enginem. Uživatel dofm doplnil, že autor příspěvku byl s názvem zřejmě první, a přirovnal konkurenční projekt k Osaurus, jen místo linuxových kontejnerů vsadil na App Sandbox.

Technická část vlákna řešila, čím se Localcode liší od volné skládačky. Uživatel jbonatakis se ptal, proč ho použít místo kombinace llama.cpp a pi, a uživatel ctkhn se ptal na výhody proti opencode s omlx jako serverem modelů. Autor v dokumentaci láká hlavně na optimalizace: vlastní draftování tokenů, kopírovací draftování při přepisu už přečtených souborů, znovupoužití prompt keše, předehřátí prvního dotazu při načítání modelu a předkompilovaná GPU jádra bez půlminutového čekání.

Nejvěcnější výměnu přinesla bezpečnost. Uživatel dofm se ptal, jestli ochrana proti přístupu mimo adresář projektu není jen domácí a jestli nechybí podpora seatbeltu, když shellové příkazy můžou sáhnout kamkoli. Autor mjwsolo přiznal, že má pravdu: čtení a zápis mimo projekt i cesty přímo uvedené v příkazu vyvolají žádost o souhlas, ale skript nebo python -c už projde všude, kam dosáhne uživatelský účet. Výzvy tak chrání spíš před chybou než před útokem a kdo chce skutečnou hranici, má dnes spustit Localcode v sandbox-exec nebo virtuálu. Podporu seatbeltu pro shellové příkazy prý autor hned zapsal jako úkol a ptal se, zda by ji lidé chtěli zapnutou standardně.

Z vlákna tak vychází Localcode jako lákavá volba pro vývojáře, kteří chtějí agentní pomoc přímo na svém stroji, ale s vědomím, že lokální neznamená automaticky izolované.
