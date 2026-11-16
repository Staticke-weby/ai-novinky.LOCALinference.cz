# 1xnui9u
**Viggle Remake pustil váhy pro přehrávání a úpravu celých videí**

r/StableDiffusion · u/init-5 · 4. listopadu 2026, 18:38 · 336 bodů / 29 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xnui9u/)

Viggle zveřejnil otevřené váhy modelu Viggle Remake, který umí přeobsadit postavy a upravit scény v existujících videích libovolné délky. Zachovává přitom původní pohyb, kameru i zvukovou stopu a nejdelším předvedeným kouskem je dvouminutový hudební klip. Váhy jsou na Hugging Face, vedle nich funguje i hotová aplikace na viggle.ai.

Remake je postavený jako agent-first nástroj vycházející z modelu H3. Součástí repozitáře je MCP server, takže výměnu postav může řídit agent v Claude Code nebo Codexu – video si sám rozstříhá na okna, namaluje klíčové snímky, napíše prompty, vyrenderuje, zkontroluje si práci a výsledek zase slepí. Pro ruční použití přibalil Viggle i ComfyUI nody a workflow, odlehčené int8 a GGUF verze pro menší grafiky a menší LoRA varianty s rankem 128 a 64. Reprodukce ukázkového videa White House Funk je v repozitáři včetně promptů.

Nejvěcnější výtku napsal u/GivePLZ-DoritosChip, který model hodně zkoušel lokálně. Nahrazování postav promptem nebo robotem podle něj funguje lépe než téměř u čehokoliv jiného, ale u skutečných lidí se známou tváří selhává přenos rysů a výsledek působí jako nepovedená LoRA. Právě v přesném držení identity přitom podle něj exceluje samotný Minimax H3, o jehož přednost tak Viggle přichází.

Na to navazuje otázka u/tofuchrispy, co vlastně běží pod kapotou a zda je Viggle jen framework kolem cizího video modelu, který řeší maskování a inpainting. Podobně prakticky se ptají další: na maximální rozlišení, odkaz na repozitář nebo prostě zda je to dobré. U/jonbristow to shrnul do tří slov dotazem, jestli to umí NSFW.

Zkušenost z ručního zkoušení popsal u/No_Cranberry_8107 jako zdlouhavou, hlavně kvůli požadavku na dobře strukturovaný prompt a několik malovaných klíčových snímků. Tvrdí, že s plánovačem záběrů BFS dostal mnohem věrnější výsledky jedna ku jedné prakticky bez promptování. Kdo nechce nic z toho řešit, tomu autor vzkazuje, ať sáhne po aplikaci, kde to agent udělá za něj.
