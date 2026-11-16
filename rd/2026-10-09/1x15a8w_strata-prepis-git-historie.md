# 1x15a8w
**Strata přepsala git historii, aby smazala stopy po Claude**

r/LocalLLaMA · u/dasbin · 9. října 2026, 00:52 · 734 bodů / 437 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x15a8w/)

Autor chtěl spustit vestavěný skript pro aktualizaci projektu Strata, jenže git skončil chybou, protože lokální a vzdálená historie neměly společného předka. Při pátrání po příčině zjistil, že byly přepsány všechny historické commity, z jejichž popisků zmizelo přiznání „Co-Authored by Claude“. Sám to označil za nechutné a podle něj se těžko hledá jiné vysvětlení než snaha nepoctivě zamaskovat původ projektu.

Nejvýše hodnocená reakce přitom mazání spíš chápe. u/gandazgul píše, že lhát by bylo něco jiného, ale on sám dělal ve vlastních projektech totéž, protože nechce, aby mu Anthropic cpal reklamu do repozitáře. Kdyby takhle postupoval každý nástroj, historie by byla plná nápisů, čím byl kód commitnut, editován nebo otestován. Na to navazuje u/HockeyDadNinja přirovnáním k dovětku „odesláno z Gmailu z mého Pixelu“, u/patchfoot02 mluví o vtíravé značce s logem, kterou je potřeba vypínat v nastavení, a u/oss-jiiim rovnou o obchodním spamu na úrovni „odesláno z iPhonu“. Podobně u/boredoo připomíná, že za commit ručí autor, a nepotřebuje, aby mu ho firma, které už platí, zaneřádila reklamou.

Druhá silná linka diskuse řeší vlastnictví a odpovědnost. u/devshore tvrdí, že by si umělá inteligence neměla sama přivlastňovat autorství softwaru, stejně jako ho nemá textový editor nebo operační systém. u/boutell píše, že ve své firmě takové dovětky zakazuje, protože každý autor musí brát kód za vlastní a dovětek ten pocit odpovědnosti ředí, navíc firmám komplikuje autorská pravidla. u/promethe42 dodává, že by nenechal přidávat dovětek „spoluautor“ ani ovladač klávesnice nebo editor, a git historii může potřebovat jako doklad práce pro daně či právní spory. u/yahbluez to shrnuje právně: nikde na světě si umělá inteligence nemůže nárokovat autorská práva, takže odstranění dovětku lze číst jako opravu, nikoli podvod.

Zároveň se ale ozývá nedůvěra, která se Stratou nesouvisí jen kvůli této kauze. u/saltyourhash víc než smazané dovětky trápí nezodpovědné přepisování veřejné větve, které rozbíjí aktualizace všem uživatelům. u/quadra-lab připomíná, že si projekt už poškodil pověst botováním diskusních fór, u/hurrdurrmeh mluví o armádě botů zvoucích lidi do Straty a přiznává, že nápady si vezme, ale nástroj samotný už nikdy nepoužije. u/Klutzy-Snow8016 proto nadhazuje, jestli by po takové zkušenosti neměl někdo auditovat i spustitelný soubor, který si Strata při instalaci stahuje.

Poučení z vlákna je tak dvojí: mazat reklamní dovětky z commitů chce leckdo, ale přepsat kvůli tomu celou veřejnou historii bez varování se nevyplácí.
