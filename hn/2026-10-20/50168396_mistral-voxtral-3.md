# 50168396
**Mistral vydal Voxtral 3: hlasoví agenti v 50+ jazycích**

Hacker News · ilreb · 20. října 2026, 18:02 · 571 bodů / 148 komentářů · [diskuse](https://news.ycombinator.com/item?id=50168396)

Mistral představil Voxtral 3, novou rodinu řečových modelů a sadu pro stavbu hlasových agentů. Láká na ukázku, kde agentka Béatrice přečte francouzský dopis od lékaře, zjistí volný termín u dermatologa a rovnou ho zarezervuje i s anglickým shrnutím pro pacientku.

Oznámení popisuje tři kusy skládačky v jednom streamovaném řetězci: přepis řeči Voxtral Small Transcribe 3 s podporou více než 50 jazyků, rozpoznáním mluvčích a detekcí konce promluvy, syntézu Voxtral Mini TTS 3 s 35 jazyky a více než 50 dialekty včetně přizpůsobení emocí, tempa a důrazu, a SDK postavené na LiveKit, kde mezi poslechem a mluvením uvažuje běžný model a volá nástroje. Mistral slibuje odezvu pod jednu sekundu, telefonování přes SIP i běh v prohlížeči přes WebRTC a nasazení buď přes API hostované v EU, nebo celé na vlastní infrastruktuře kvůli kontrole nad daty.

V diskusi ale hned první vlákno zhořklo. Uživatel drum55 lituje, že je model zavřený, což prý jen potvrzuje bídnou situaci převodu řeči pro lokální nasazení, a causal se ptá, co pak vlastně znamená slibované vlastní nasazení. Podobně dr_hooo mrzí, že novinka není otevřená jako předchozí verze, a satvikpendem píše rovnou, že o zavřený model okamžitě ztrácí zájem, když je zavřených výborných převodů i syntéz plno.

Odtud se debata stočila k tomu, co si pustit doma. Gavinray chválí Kokoro jako zdaleka nejlépe znějící lokální syntézu, dost malou na běh na moderních telefonech v reálném čase, na které poslouchá audioknihy z PDF a e-pubů. Dr_hooo doporučuje Qwen ASR a QwenTTS a zmiňuje pocket-tts od Kyutai, arendtio zase službu speaches.ai kvůli jednoduchému balíčku a překvapivě nízké latenci a kalabrium doufá v menší modely pro osobní použití, protože hlasová data nechce posílat ven.

Zastánci Mistralu namítají, že omáčka není v samotném přepisu a hlase. Uživatel dymk píše, že kouzlo je v propojení s uvažujícím modelem v reálném čase a v zakrytí prodlev při volání nástrojů, což je vidět právě na ukázkové rezervaci. Aliljet se ptá, jak reálná ta konverzace bez prodlev je, a panoramix odpovídá, že cíl je pod sekundu. Odlišný tón přidává arjie, který si Voxtral chválí na přepis podcastů do textu i za to, že si nevymýšlí při tichu, zatímco MisterMunchkin tvrdí, že nové ukázky hlasů zní jako generický hlas umělé inteligence, kdežto jednička zněla jako skuteční lidé.

Z debaty tak zůstává rozpolcený obrázek: silná nabídka pro kontaktní centra, virtuální asistenty a hands-free copiloty, kterou ale komunita kolem otevřených modelů zatím spíš mine.
