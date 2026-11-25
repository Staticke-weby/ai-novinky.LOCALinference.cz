# 1y4kikk
**Paměť pro milion tokenů spadla ze 130 TB na 890 MB**

r/LocalLLaMA · u/edrevo · 24. listopadu 2026, 19:16 · 690 bodů / 66 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1y4kikk/)

Jediná konverzace o délce milionu tokenů kdysi potřebovala 130 TB paměti grafických karet, dnes se vejde do 890 MB. Ukazuje to přehled na blogu three.dev, který prošel cestu od Llamy 1 65B až po DeepSeek-V4.1-Flash. Rozdíl dělá několik let výzkumu úspornější pozornosti modelů.

Text rozebírá šestici postupných triků, které pád umožnily: FlashAttention, Grouped Query Attention a Multi-head Latent Attention doplněné kvantizací KV cache, slučováním více tokenů do jednoho záznamu a nakonec cache sdílenou napříč různými vrstvami.

Největší ohlas v diskusi sklidila hláška u/gtek_engineer66, že zákon pozornosti je lepší než Mooreův zákon. Chválu sbírá i samotné zpracování, podle u/LionPrestigious6612 je vidět skutečná práce a je mnohem lepší než obvyklé odfláknuté příspěvky. Zároveň se řeší grafika: u/backyard_tractorbeam připomíná, že logaritmická škála potřebuje dílky na ose, jinak se v ní špatně čte.

Nejobsahovější rozbor přidal u/Sun77177. Prvních dvaapadesátkrát je podle něj zadarmo, FlashAttention srazí nároky ze 130,5 TB na 2,5 TB bez změny výstupu, zatímco zbytek do 890 MB už model platí změnou toho, co doopravdy počítá, zhruba dvoutisícidevítisetkrát. Do toho zapadá poznámka u/slowtractor, že srovnání prochází několika modely a konstrukcemi cache, takže nejde o jeden model zrychlený jen softwarovými úpravami. U/Mysterious_Bison_907 si z čísel dopočítal druhou stranu mince, že Llama 1 65B by do 80 GB vtěsnala jen kolem 650 tokenů kontextu.

Třetí linka diskuse řeší, jestli se za úspory neplatí kvalitou. U/AdWild3943 píše, že úpravy kontextu u V4 a V4.1 výrazně zhoršují zapamatování v dlouhém kontextu, takže se o stabilním mainstreamu zatím nedá mluvit, u/Solembumm3 mluví o obrovské ztrátě kvality a u/ComplaintMaker pochybuje o použitelnosti čtyřbitové sdílené cache na milionu tokenů. U/throwaway2676 k tomu přidává paradox, že špičkové kontextové okno je už skoro dva roky zaseknuté na jednom milionu. Odlehčení dodal u/timur_timur poznámkou, že se chat v jednu chvíli stane samotnou cache.

Z vlákna tak zůstává dvojí obrázek: křivka paměťových nároků padá strměji než kdysi výkon čipů, ale část komunity čeká, až úsporné triky doženou i spolehlivost na dlouhém kontextu.
