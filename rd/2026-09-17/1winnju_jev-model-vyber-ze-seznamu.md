# 1winnju
**Jev umí jen vybírat ze seznamu, někdo z něj udělal chatbota**

r/LLM · u/TheCamer1 · 17. září 2026, 09:58 · 91 bodů / 19 komentářů · [diskuse](https://www.reddit.com/r/LLM/comments/1winnju/jev_the_new_ai_that_can_only_pick_from_a_list_has/)

Model Jev od TypeSafe (typesafe.ai) neumí psát věty. Dostane něco k posouzení a seznam možností a ke každé vrátí pravděpodobnost, že sedí — typicky se tak poznává spam v e-mailu nebo se produkt zařazuje do jedné ze 200 kategorií. Je v tom rychlý a levný, jenže textovou odpověď si z něj člověk běžnou cestou nevynutí. Autor příspěvku u/TheCamer1 se právě touto nemožností pobavil a postavil z něj chatbota, který odpovídá výběrem z nabídky.

Funguje to překvapivě prostě: autor se modelu ptá, které slovo ze seznamu asi 250 slov nejpravděpodobněji následuje po rozepsané větě. Když je věta „Dogs are“, model vybere „loyal“, věta se prodlouží a ptá se znovu, takže každé slovo odpovědi je výsledkem jedné takové otázky. Protože Jev slova spíš hádá než umí, autor přidal druhý krok — z deseti nejpravděpodobnějších slov sestaví deset vět a nechá model vybrat tu, která zní nejlépe. Slovo tak vyjde asi na 1,3 sekundy a odstavec zhruba na cent, slovník tvoří seznam 4 000 slov plus slova z uživatelovy zprávy. To, co není na seznamu, Jev prostě nehláskuje, zkoušení je možné s vlastním klíčem od TypeSafe a zdrojový kód autor zveřejnil na GitHubu.

Největší ohlas vzbudilo to, že část čtenářů vtip nepochopila. u/flamedrifter se směje právě lidem, kteří pointu minuli, a u/Zachattackrandom nevěřícně vysvětluje, že věta o „zcela novém nápadu ptát se na nejpravděpodobnější token“ je přece otevřená ironie. Do téhle linky zapadá i reakce u/CorkBios, který autorovi s vážnou tváří gratuluje k „vynálezu autoregresivního jazykového modelu“ a vysvětluje mu logity a tokeny. Autor u/TheCamer1 se jen směje, že mu sarkasmus v postu asi neprošel.

Vedle toho se rozjela věcná hádka o to, co Jev vlastně je. u/ihexx si utahuje z marketingového humbuku kolem modelu, který se tváří jako „System 1“ zcela odlišný od velkých jazykových modelů, a přitom je uvnitř podle něj jen omezený slovník nad jazykovým modelem. Vadí mu i sliby o vyřešených halucinacích pomocí omezení slovníku a tvrzení o paralelním běhu, který prý zvládne s prefixovou mezipamětí každý jazykový model. u/porkyminch oponuje, že méně flexibilní, ale velmi rychlý model pro rozhodování ve zlomku sekundy má smysl, a jako příklad z dem ukazuje hraní Dooma za 7 dolarů na hodinu.

Zbytek vlákna sbírá drobné nápady a hlášky. u/Ok-Fox3479 navrhuje zpracování po znacích a srovnání s jinými modely, autor ale odpovídá, že Jev hláskování vůbec nezvládá a bez schopnosti plánovat dopředu z toho leze jen změť znaků. u/paperstudio_jen vtipkuje, že když model umí vybírat další pixel, může kreslit obrázky, u/yeathatsmebro suše dodává, že multimodální klasifikátory tu byly dávno před velkými jazykovými modely.

Čtenář si z toho odnese jednoduché ponaučení: i model, který neumí napsat větu, se dá donutit mluvit, jen to bude pomalé, drahé a vtipnější než užitečné.
