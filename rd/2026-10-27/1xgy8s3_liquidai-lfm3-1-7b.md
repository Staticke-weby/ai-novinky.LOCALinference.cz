# 1xgy8s3
**LiquidAI vydalo LFM3-1.7B pro lokální agenty**

r/LocalLLaMA · u/jacek2023 · 27. října 2026, 18:04 · 355 bodů / 79 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1xgy8s3/)

LiquidAI vydalo LFM3-1.7B, textový model pro lokální agenty a specializované aplikace postavený na nové tri-hybridní architektuře. Má kontext 256 tisíc tokenů a je laděný pro agentní prostředí jako Hermes Agent, Pi nebo OpenClaw, ve čtyřbitové kvantizaci zabere kolem jednoho gigabajtu, takže se vejde do telefonu i notebooku, a je určený k rychlému doladění na konkrétní domény a nástroje na jedné grafické kartě.

Podle podkladů od LiquidAI má model 1,73 miliardy parametrů ve 24 vrstvách kombinujících krátké konvoluce, posuvnou i globální pozornost a slovník o 128 tisících tokenech. Spolu s ním vyšla celá rodina LFM3 – základní checkpoint trénovaný na 22 bilionech tokenů, vision model s videem, audio model, omni model pro text, obraz i zvuk a rychlé rozhodovací modely – a podpora pro běh v llama.cpp už byla sloučena.

Nadšení v diskusi je skoro hmatatelné. u/Aggravating-Push-207 to shrnul hláškou, že se do toho tentokrát pořádně opřeli, u/Hot_Example_4456 přidal zvolání o velkém nasazení a u/paryska99 se ptá, jestli už jsou Vánoce. Nejvíc rezonují výsledky: u/netherreddit chválí, že benchmarky vypadají na 1,7 miliardy parametrů skvěle, u/_raydeStar tvrdí, že Liquid v testech porazil Qwen 3.5 9B, u/Repulsive_Initial308 doufá, že tohle konečně překoná Qwen 3.5 4B, a u/Steuern_Runter upozorňuje, že v LiveCodeBench v6 je lepší než Qwen3 Max.

Vedle oslav se řeší hlavně praktické nasazení. u/crusaderky popisuje, že potřebuje parsovat weby a PDF včetně grafů a neví, jestli sáhnout po textovém modelu, po verzi s viděním, nebo složitě volat vision nástroj z textového modelu. u/mantisalt se ptá, v jaké aplikaci novinku nejlépe vyzkoušet na telefonu, a u/atumblingdandelion se přidává s otázkou, jak se takové modely na telefonu vůbec provozují a k čemu jsou. Do toho u/Equal-Document4213 řeší podporu doladění pro medicínské sumarizace v edge nasazení, kde prý rychlost s DSpark smetla jejich optimalizace FlanT5.

Nechybí ani skepse a chuť po větším. u/JLeonsarmiento pochybuje, že se dá Hermes řídit s čímkoli pod zhruba 25 miliardami parametrů, ale dodává, že se nechá překvapit. u/DrBattletoad doufá v další model 8B-A1B, který mu na telefonu funguje skvěle, a u/Old-Juggernut-101 se už teď nemůže dočkat větších modelů. Praktickou tečku přidává u/ByYiro otázkou, jestli umožňuje licence bez omezení komerční nasazení ve firemní aplikaci.

Z malého modelu, který se vejde do kapsy, se tak stává velká sázka na lokální agenty – a diskuse naznačuje, že rozhodne až to, jak obstojí mimo tabulky benchmarků.
