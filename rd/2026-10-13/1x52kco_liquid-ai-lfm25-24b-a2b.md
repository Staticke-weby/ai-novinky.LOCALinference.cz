# 1x52kco
**Liquid AI vydala LFM2.5-24B-A2B pro lokální agenty**

r/LocalLLaMA · u/Skyline34rGt · 13. října 2026, 19:14 · 482 bodů / 131 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x52kco/)

Autor v komunitě nasdílel odkaz na novinku od Liquid AI spolu s GGUF variantou a bezplatným demem na playground. LFM2.5-24B-A2B je největší a zároveň poslední model rodiny LFM2.5, která se tím roztáhla od drobného 230M až po 24 miliard parametrů. Jde o čistě textový reasoning model postavený pro rychlé a soukromé agenty přímo v zařízení, kterému na jeden token stačí jen kolem 2,45 miliardy aktivních parametrů.

Podle modelové karty má být model v agentních a tool-use úlohách konkurencí pro Qwen3.6-35B-A3B, tedy model s asi o polovinu více parametry, když na LiveClaw hlásí 48,09 bodu proti 38,19. Výrobce slibuje až 1,7krát rychlejší inferenci než srovnatelná MoE a láká na 184 tokenů za sekundu na Apple M5 Max a až 21 tisíc tokenů za sekundu na jediném NVIDA B300. Pod kapotou je 40 vrstev, 64 expertů s top-4 routingem, trénink na 36 bilionech tokenů, kontext 131 tisíc tokenů a šestnáct jazyků od angličtiny po polštinu.

Největší ohlas mají v diskusi „chudí na grafiky“, jak to nazval u/MiMillieuh. u/TioMir model označil za ideální pro svůj lokální server se 6 GB VRAM a 16 GB RAM a už jen čeká na kvantizace od Unslothu, u/Holiday_Point_603 zase pochválil nenáročný formát pro lidi s 24 GB kartami. První měření znějí slibně: u/Morphon na sestavě s 12GB 5070 a 64 GB paměti naměřil v Q4 trvale 64 tokenů za sekundu a model je podle něj použitelný i čistě na procesoru notebooku se Zen 5, u/Solid_Vermicelli_510 hlásí 20 až 25 tokenů za sekundu na stařičké RTX 2060 se 6 GB a Ryzenu 1600AF. I proto padla vtipná otázka u/danigoncalves, jestli jde vlastně o rychlejší Qwen 3.6 35B A3B.

Nadšení ale brzdí první testy kvality. u/Morphon píše, že v jeho sadě model zatím propadl v abstraktním uvažování, logice i humanitně laděných testech, a skutečný smysl vidí až v agentních postrojích, které bude zkoušet dál. Podobně u/uti24 na Strix Halo v Q6_K popisuje, že je model sice pěkně rychlý, ale prostou hru Asteroids v LM Studiu nedokončil ani po několika pokusech a Qwenu 3.6 35B se podle něj neblíží. u/Gotxi zase líčí zkušenost z playground, kde si model při vyhledávání na webu vyvodil špatný závěr a opakovaným přemýšlením ho místo opravy proměnil ve svou pravdu.

Mezi tím se ozývají praktici, kteří už náhradu hledají. u/Adventurous-Wing-988 tvrdí, že mu model v chatu stačí na to, aby nahradil šestidolarové předplatné, které používá vedle Cursoru na kódování, u/Septerium sní o nesmyslně rychlém agentovi Hermes na terminálové a pythoní úkoly a uživatel etaoin314 v něm vidí pilnou včelku pro pomalejší modely, které by ji řídily. Opatrnější je u/hideo_kuze_: na skutečné kódování by raději pomalejší, ale schopnější Qwen 3.8 a na kreativitu Gemmu. Do toho se vrací stará výtka k licenci, kterou u/No-Paper-557 shrnul prosbou o nápravu v konkurenci otevřených modelů.

Kdo má slabou kartu a chce rychlého lokálního pomocníka na agenty, tenhle únik by si neměl nechat ujít — jen od něj zatím nečekejte zázraky v logice ani v kódu.
