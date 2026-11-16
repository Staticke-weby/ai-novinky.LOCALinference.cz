# 1wlzvcx

**ZCode po aféře s tichým uploadem kódu otevřel klienta (Apache 2.0) — komunita mluví o damage controlu**

| | |
|---|---|
| Subreddit | r/LocalLLaMA |
| Autor | u/ResearchCrafty1804 |
| Publikováno (Europe/Prague) | 21. 9. 2026 |
| Skóre / komentáře | 544 / 112 |
| Repozitář | https://github.com/zai-org/ZCode |
| Diskuse | https://www.reddit.com/r/LocalLLaMA/comments/1wlzvcx/zcode_is_now_open_source/ |

## Co se stalo

ZCode oznámil, že **otevřel svého klienta** na GitHubu (`zai-org/ZCode`, licence **Apache 2.0**) — včetně desktopové aplikace, webového pracovního prostředí, backendu, Agent CLI a běhového prostředí. V oznámení se omlouvá za „bezpečnostní problémy nahlášené komunitou“ a tvrdí, že **žádná data nebyla uchována a nikdy nebyla použita k tréninku modelů**.

Firma uvádí, že bezpečnostní náprava je dokončena v klientu **v3.14.0**, kde byla **odstraněna funkce Repo Wiki** a **postup nahrávání snímků lokálního repozitáře**; zmiňuje posudky **CAICT** a **NSFOCUS** s tím, že bucket `zcode-prod` na Alibaba Cloud OSS je ve stavu „nulových dat“ a smazán. Slibuje zveřejnění plné bezpečnostní zprávy a proces hlášení zranitelností s odměnami.

## Kontext, který komunitu rozzuřil

Podle komentujících byl klient přistižen při **tichém, šifrovanému uploadu uživatelského kódu** na servery (častý odkaz na blog ferstar.org o „silent workspace snapshot upload“). Open-sourcing je proto velkou částí vlákna čtený jako **řešení reputačního požáru**, ne jako projev otevřenosti.

## Citace

> „V reakci na bezpečnostní problémy produktu ZCode nahlášené komunitou jsme dokončili nezbytnou nápravu a upřímně se omlouváme všem našim uživatelům.“ (překlad) — ZCode

> „Pokud jde o kódová data zmiňovaná komunitou, potvrzujeme, že žádná taková data neuchováváme a že nikdy nebyla použita k trénování modelů.“ (překlad) — ZCode

> „Kdybych měl niklák za každý případ, kdy byla AI firma přistižena při exportu uživatelských dat a pak zveřejnila svého klienta jako open source, aby uklidnila davy, měl bych 2 nikláky. Což není mnoho, ale je divné, že…“ (překlad) — u/ImMadeOfBees (skóre 295)

> „Prostě ukradli lidem kód a asymetrickou kryptografií skrývají zboží, které nahráli do cloudu. Šílená sračka.“ (překlad) — u/__JockY__

> „"Pracovní postup pro nahrávání snapshotů lokálních repozitářů byl zakázán" odvádí neuvěřitelnou práci jako nenápadná odrážka v téhle omluvě.“ (překlad) — u/FlightUsed648

## Hlavní linky diskuse

- **Damage control.** Nejsilnější linie: srovnání s předchozím incidentem u Groku — firma přistižená při exfiltraci dat otevře klienta, aby uklidnila masy.
- **Věří někdo, že zdroják odpovídá produktu?** Několik komentujících pochybuje, že zveřejněný kód = to, co běží u zákazníků; padá i tvrzení „otevřeli 2 commity“ a že PR jsou zakázané.
- **Srovnání s jinými harnessy** (OpenCode, Pi, OMP, DSH, mini-swe-agent).
- **Nařčení z botů.** Část vlákna tvrdí, že kritika je downvotována boty — neověřitelné.

## Rozpory a neověřené informace

- **Rozpor:** vrací open-sourcing důvěru (Apache 2.0 jako pojistka do budoucna) vs „PR stunt, bez odpuštění“.
- **Rozpor:** šlo o nehodu/bug, nebo o úmyslnou exfiltraci skrytou asymetrickou kryptografií? Oznámení mluví o napravené bezpečnostní chybě; komentující citují technický blog jako důkaz záměru.
- **Neověřené:** tvrzení, že zveřejněný kód diverguje od produktu; že jde jen o 2 commity; že diskusi manipulují boti.

## Proč to je důležité

Je to nejostřejší případ dne na téma **důvěry v AI coding nástroje**: agentní klient s přístupem k celému repozitáři je bezpečnostní hranice, kde jeden tichý upload zničí reputaci. Open-sourcing je rozumná reakce (umožní audit), ale sám o sobě neřeší, co se stalo s daty předtím — a to je přesně to, co komunita odmítá přejít mlčením.

---

*Zdroje: [GitHub zai-org/ZCode](https://github.com/zai-org/ZCode), [Reddit diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1wlzvcx/zcode_is_now_open_source/), [technický blog ferstar.org](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/).*
