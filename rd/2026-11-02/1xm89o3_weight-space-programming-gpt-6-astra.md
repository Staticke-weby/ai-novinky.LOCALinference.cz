# 1xm89o3
**GPT-6 Astra umí číst a přepisovat váhy modelů. Malému Qwenu zvedl matematiku z 7,9 na 48,1 procenta**

r/singularity · u/troll_khan · 2. listopadu 2026, 21:18 · 1510 bodů / 157 komentářů · [diskuse](https://www.reddit.com/r/singularity/comments/1xm89o3/)

Čtyři výzkumníci z MIT CSAIL popsali techniku nazvanou Weight-Space Programming: velký frontier model přímo čte a přepisuje váhy jiné neuronové sítě, bez gradientů a bez klasického tréninku. V experimentu GPT-6 Astra upravila model Qwen3.5-0.8B tak, že změnila 131 072 z přibližně 0,8 miliardy vah, tedy pouhých 0,016 procenta.

Podle oznámení autora Rikiyi Takehiho na síti X se tím matematické schopnosti malého modelu znásobily: MATH-500 stoupl ze 7,9 na 48,1 procenta, GSM8K ze 13,8 na 67,1 procenta a IFEval z 21,0 na 62,3 procenta. Zásah podle něj hlavně rozbil smyčky v uvažování, kvůli kterým model vyčerpal limit tokenů dřív, než stihl odpovědět — podíl takto zaseknutých odpovědí klesl z 93 na 33 procent.

V diskusi převládlo nadšení smíšené s úžasem nad samotným principem. u/SquareQuit1741 se ptá, zda jde o novou hranici po škálování a inference-time škálování, a přidává, že svět bude v roce 2030 vypadat úplně jinak. u/DnDiene žasne, jak může model „koukat na obrovskou řadu čísel a prostě pochopit, co dělají“, a přirovnává to k mimozemské formě inteligence, zatímco u/johnxreturn to shrnuje jako úžasné, děsivé a otevírající spoustu dveří.

Nejsilnější věcná linka ale výsledek krotí. u/Key_Extension_2501 píše, že výsledek je přehnaně nafouknutý, protože Astra u Qwenu jen odstranila bariéru, která mu bránila použít znalosti, jež už měl — smyčku v řetězci úvah. Nové znalosti ani schopnosti prý nepřidala, což dokládá pokus s modelkou Gemma 3 270M, která nesmyčkuje a u níž se zlepšení vůbec nedostavilo. Podobně u/Slappatuski tvrdí, že titulek klame: model prý neporozuměl vahám pohledem, ale spíš odstranil váhy způsobující smyčku, takže označení Weight-Space Programming je zavádějící. Doplňují to u/GiveSparklyTwinkly otázkou, zda si model za lepší matematiku nepohoršil v něčem jiném, a poznámkou u/Distinct-Question-16, že na vadu upozorňovala už samotná karta modelu Qwen.

Třetí proud debaty míří k rekurzivnímu sebezlepšování. u/hydraofwar pokládá „otázku za milion dolarů“, zda to funguje i tehdy, když Astra edituje vlastní váhy, u/personalityson se ptá narovinu, proč by GPT-6 Astra nevylepšila sama sebe, a u/EmptyVolition242 v tom vidí náznak superinteligence. Praktický pokus přidal u/liltingly, který metodu hned zkouší na menším transformátoru zaseknutém při tréninku a popisuje, jak modelu zakázal sahat na cloud a dovolil mu jen numerickou analýzu vah.

Zatím jde o rané výsledky bez recenzního řízení, spíš o odstranění brzdy u jednoho malého modelu než o univerzální přepisování inteligence.
