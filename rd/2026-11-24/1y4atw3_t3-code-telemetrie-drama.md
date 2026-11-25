# 1y4atw3
**T3 Code čelí obvinění z tajné telemetrie. LocalLLaMA řeší důvěru**

r/LocalLLaMA · u/jacek2023 · 24. listopadu 2026, 12:21 · 400 bodů / 185 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y4atw3/)

Open-source nástroj T3 Code od youtubera Thea čelí obvinění, že od března tiše sbíral telemetrii. Čínský vývojář, jehož vlákno z X přeložil a nasdílel u/jacek2023, tvrdí, že PR číslo 174 z 6. března 2026 zapnulo výchozí telemetrii PostHog bez dokumentace, vyskakovacího okna i přepínače v nastavení. Web projektu přitom víc než tři měsíce sliboval „No telemetry / Unless you opt in. Full stop.“, tedy nulový sběr bez výslovného souhlasu, a tenhle slib měl při redesignu 18. června zmizet bez oznámení.

Autor obvinění dodává, že v říjnu Theo osobně poslal změnu, která přepnula dávkové hlášení každých deset sekund na vlastní server. Diskusi na Redditu navíc rozvířila zmínka o issue číslo 4123 na GitHubu, které mělo být otevřeno a pak zase zavřeno, což u/packetsent označil za podlé a ptá se, zda to musel někdo udělat ručně.

Technicky založená část vlákna se snaží zjistit, co skutečně odchází. u/Pogsquog píše, že při výchozím nastavení T3 Code posílá statistiky používání a diagnostiku připojení službám, které T3 provozuje nebo platí, hlavně PostHogu a Axiomu, a vypnout to jde proměnnou T3CODE_TELEMETRY_ENABLED=false. Podle něj jde o volby modelu, režim oprávnění, délku běhu, počet tokenů, systém, verzi a hashe uživatelského a instalačního ID včetně pádových výpisů. Podobně to vidí u/pck91999, který na Macu mini a MacBooku napočítal za den 17 a 9 dávek na ingest.t3.codes a uklidňuje, že prompty ani kód se podle dokumentace neposílají, takže mluvit o „kradení dat“ je přehnané.

Jádro sporu je tak pro komunitu jinde: v rozporu mezi slibem na webu a zapnutým sběrem po výchozím nastavení. Právě na to naráží i poznámka, že hashovaná ID účtů Claude a Codex jsou stejná na každém stroji, takže anonymita je sporná, a odkaz na PR číslo 21506. Obránci jako u/fgk55555 namítají, že data se týkají jen využití modelu a tokenů, jdou vypnout, projekt je otevřený a kdo chce, může si ho forknout a nechat si provoz zkontrolovat agentem.

Zbytek vlákna se rychle stočil k osobě Thea a k únavě z vývojářských influencerů. Nejvýše hodnocený u/Lyelinn ho přirovnává k DHH a označuje ho za povrchního mluvícího s minimální technickou hloubkou, který vyrábí clickbait pro videa. u/NineThreeTilNow k němu přidává Primeagena a PirateSoftware a tvrdí, že jde o tvůrce bez pevných názorů, kteří tvoří to, co se „prodává“, u/FinBenton zase doufá, že si vlákno najde vyhledávání, aby se lidé Theovým věcem vyhnuli. Nechybí ani ironie typu „Theo? Zapletený do dramatu? Jsem ŠOKOVÁN!“ od u/zucchini_up_ur_ass nebo povzdech u/DankpawsDev, že by byl denně o něco šťastnější, kdyby mu z feedů zmizely zmínky o T3, Theovi a Omarchy.

Čtenář si z toho odnese jednoduché ponaučení, které se ve vlákně opakuje: u open-source nástroje rozhoduje nejen kód, ale i to, zda slib o soukromí platí ve výchozím nastavení.
