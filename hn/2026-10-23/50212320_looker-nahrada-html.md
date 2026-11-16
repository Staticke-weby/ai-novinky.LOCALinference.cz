# 50212320
**Nahradili Looker za 150 tisíc dolarů hromadou HTML souborů**

Hacker News · skadamat · 23. října 2026, 19:15 · 124 bodů / 75 komentářů · [diskuse](https://news.ycombinator.com/item?id=50212320)

Datový tým ve firmě o pěti stech lidech se staral o Snowflake, dbt s více než dvěma tisíci modely a běžnou platformní rutinu, a k tomu firma platila zhruba 150 tisíc dolarů ročně za přibližně tři sta licencí Lookeru. Tým přitom tvořili jen tři inženýři. V únoru jedna kolegyně za odpoledne spíchla interní službu na sdílení HTML souborů a po osmi měsících má stejně týdenních uživatelů jako Looker, jehož využívání mezitím kleslo o třetinu.

Podle odkazovaného blogu to začalo tím, že lidé ve financích, provozu a marketingu začali hromadně promptovat v Claude a odnášeli si analýzy jako hezké jednostránkové weby s grafy, které ale končily ve složce se staženými soubory a ve Slacku. Nová služba je ukládala do S3 za firemní přihlášení a později přidala živé dotazy s tokenem diváka, takže oprávnění řešil Snowflake a význam dat hlídaly dbt modely. Autor popisuje i předělávku na pořádné zabezpečení se sandboxovaným iframem, kontrolou skriptů a publikováním přes jednotný konektor, a vyčísluje jeden dashboard zhruba na milion tokenů a padesát centů.

Diskuse se hned zvrhla k tomu, kdo text vlastně psal. Uživatel Vaushite suše poznamenal, že to psala umělá inteligence, a uživatel formerly_proven souhlasil, že techničtější pasáže zní strojově. Uživatel extr se toho ale zastal s tím, že obsahově to není odpad a alternativou by bylo, že by tak podrobný popis vůbec nevznikl, a uživatel adwn dodal, ať se kritizuje obsah, ne způsob vzniku. Do toho si uživatel doctorpangloss rýpl do věty o Kubernetes, kde nasazení nové služby vypadá jednoduše jen proto, že už firma měla Terraform, Helm a celou mašinerii okolo.

Nejživější spor je o peníze. Uživatel ekreloff vyčítá autorovi, že do účtu za vlastních 8,3 tisíce dolarů nezapočítal platy inženýrů za osm měsíců práce bokem a úspora je tak spíš poloviční. Uživatel alexkbuilds oponuje, že se tím kupuje i svoboda dashboardy si volně vymýšlet pouhým popisem, což v tuhých šablonách Lookeru nešlo. Podobně to vidí uživatel Glyptodon, podle kterého se BI nástroje nahrazují snadno, pokud pod nimi leží slušná datová vrstva.

Třetí linka řeší, jestli obrázek za padesát centů stačí. Uživatel alexkbuilds přiznává, že u předchozího zaměstnavatele nikdy nevyřešili, jak zaručit, že se všichni dívají na správná čísla, a bez analytiků se to neobejde. Uživatel james_marks to shrnul hláškou, že slogan BI zní lhát kolegům sebevědomě a s lehkostí. Uživatel bushido a uživatel yfontana rozlišují hezkou vizualizaci a skutečné BI, tedy společné definice metrik, správu a řízení přístupu, a varují, že záplava lehce vygenerovaných stránek může rozhodování spíš zhoršit. Nostalgicky to uzavřel uživatel phone_book vzpomínkou na firmu, kde si lidé kopírovali PHP stránky s SQL a bookmarky porazily i drahý BI nástroj.

Z vlákna tak zůstává pocit, že sloupce s grafy dnes umí vyrobit kdokoli, ale důvěra v čísla se pořád staví mnohem pomaleji.
