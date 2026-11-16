# 50406670
**OpenStick za 10 dolarů: čtyřjádrový homelab s LTE a GPS**

Hacker News · LaurensBER · 7. listopadu 2026, 19:12 · 487 bodů / 98 komentářů · [diskuse](https://news.ycombinator.com/item?id=50406670)

Za deset dolarů včetně poštovného se dá pořídit miniaturní domácí server, který je úplně tichý a skoro nic nespotřebuje. Zařízení OpenStick nabízí čtyři jádra Cortex-A53 na 1 GHz, 512 MB RAM, 4 GB eMMC úložiště a k tomu 4G modem s GPS a Wi-Fi. Po složitější instalaci na něm běží Debian se systemd a Podmanem, takže zvládne i kontejnerové služby.

Autor na blogu popisuje, co všechno se na takto omezený hardware vejde, pokud se software vybírá podle spotřeby v řádu jednotek megabajtů. Provozuje tam například CastSponsorSkip pro přeskakování sponzorů na zařízeních Google Cast, upravené AdGuard Home na filtrování DNS, agenta Zeroclaw ovládaného přes Telegram, tunel Cloudflare pro bezpečný přístup z internetu i monitoring Beszel, Gatus a čtečku Fusion RSS. Většina služeb si podle něj vystačí s 8 až 40 MB paměti.

Nejživější část diskuse řeší, kde sehnat samotný hardware. LaurensBER píše, že svůj kus koupil na AliExpressu, kde je to trochu loterie, protože prodejci přesný čip neuvádějí, ale za tu cenu se riziko vyplatí a nejhůř člověk skončí se záložním 4G modemem. Grombobulous upozorňuje, že původní repozit projektu čtyři roky nikdo neaktualizoval a odkazy z Hackaday už nefungují, mkl proto odkazuje na rozcestník openstick.org s návody a tipy na nákup a dools tvrdí, že má na prodej asi tři stovky kusů se stejným čipem msm8916.

Další vlákna se točí kolem zprovoznění. Polycancel popisuje, že po smazání hotspot připojení přes nmcli se mu zařízení fakticky zablokovalo a ptá se na vynucení režimu EDL, Qision zase řeší, zda lze dongle připojit na domácí Wi-Fi místo režimu hotspotu, což mu dools potvrzuje z vlastní zkušenosti. Na dotaz geoffbp ohledně záloh autor odpovídá, že každou noc zálohuje přes restic do Backblaze, protože na NixOS je hardware příliš slabý.

Hodně prostoru dostaly alternativy a bezpečnost. NortySpock vyjmenovává, co vměstnal do Raspberry Pi 4 a tenkého klienta, od lehkého webserveru po MQTT a měření latence, Grombobulous a jprd zase chválí levné vyřazené Chromeboxy s přehrátým firmwarem jako skvělé stroje na kontejnery. Kolem Cloudflare Tunnela se rozjela přestřelka o soukromí, kdy hikemu odmítá představu, že by mohla provoz číst americká agentura, sam345 kontruje, že při nákupu z Číny by čekal spíš čínskou stranu, a autor připouští, že plně auditovatelný stack je extrémně těžký. V menším sporu o RSS čtečky rcarmo chválí snímky Fusionu, mmozeiko doporučuje jedno-binární yarr a msephton navrhuje FreshRSS jako mezipaměť pro mobilní klienty.

Z malého LTE klíče se tak v diskusi stává návod, jak začít se self-hostingem skoro zadarmo, když člověk počítá každý megabajt paměti.
