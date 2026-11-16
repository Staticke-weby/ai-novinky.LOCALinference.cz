# 50439193
**AlphaProof Code formálně ověřil šifrování Signal. Trvalo to týdny místo let**

Hacker News · ilreb · 10. listopadu 2026, 13:11 · 606 bodů / 179 komentářů · [diskuse](https://news.ycombinator.com/item?id=50439193)

Google DeepMind představil AlphaProof Code, agentní rámec pro formální verifikaci kódu, a jako ukázku síly jím nechal ověřit kryptografický protokol Signal. Agentní tým sepsal miliony řádků důkazů v jazyce Lean a dokázal jeho klíčové vlastnosti. Práci, se kterou by se expertní tým potýkal roky, zvládl za týdny.

Systém převádí bezpečnostní cíle na matematické věty, které se pak strojově ověřují, a stojí na modelu Gemini 4 Carbon. Ambicí je zlevnit formální verifikaci, která se dosud považovala za zlatý standard bezpečného softwaru, ale dovolil si ji jen málokdo. Právě cenu a pracnost měl agentní přístup srazit na únosnou míru.

Nadšení v diskusi mísí obdiv s korekcemi. Uživatel p-e-w žasne, že je kód Signalu bezpečný nejen prakticky, ale i ve striktním formálním smyslu, a jeho autory pasuje na inženýry nejvyššího kalibru. Gasp0de ale připomíná podstatný detail, že ověřen byl jen šifrovací protokol, nikoli celá aplikace Signal, a milkshakes dodává, že o zbytku kódu by si tak jistý nebyl. Computer0 to shrnuje s nadsázkou, že je rád, že Signal vypadá dobře i v očích robotických vládců.

Nejvěcnější linka se točí kolem toho, čemu vlastně důkaz věřit. Uživatel thibsrn chválí praktické využití, ale všímá si, že agent nezpochybňuje specifikaci, jen ověřuje implementaci proti ní. Na to navazuje ane otázkou, jak je zaručeno, že se zkompilovaný kód běžící na modelu procesoru v Leanu chová stejně jako na skutečném čipu a že specifikace sepsaná modelem opravdu odpovídá tomu, co dělá kód Signalu. Jinými slovy formální důkaz nezaručuje, že stejné záruky platí i pro reálné běhové prostředí.

Zbytek vlákna se rozpadá do odboček, které ukazují, co lidi na tématu fascinuje. Paganel se ptá, jak se formální dokazování vyrovnává s problémem zastavení, a xrisk, NooneAtAll5 nebo sebzim4500 trpělivě vysvětlují, že dokazovač si neklade za cíl rozhodnout o všech programech, jen podat důkaz pro ten konkrétní. Nurumaik volá, ať teď přijde na řadu Telegram a jednou provždy se rozsekne debata o vlastní kryptografii, na což pona-a odpovídá, že Telegram si vzal protokol na jednorázové klíče, ořezal ho na špatných místech a nechává mimo šifrovanou část trvalé identifikátory zařízení. A zatímco xrisk přemítá, na kolik dolarů tahle sranda vyšla, conartist6 vtipkuje, že bude skvěle, až každé spuštění testů bude stát deset tisíc za to, že umělá inteligence zkontroluje svůj obří důkaz.

Z diskuse tak zůstává dvojí dojem: úleva, že formální metody přestávají být výsadou letitých projektů, i střízlivé vědomí, že důkaz protokolu ještě není důkazem celé cesty od specifikace až po čip v kapse.
