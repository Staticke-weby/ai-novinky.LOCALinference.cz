# 50275128
**Nvidia vydala Nemotron 3.5 Transcribe. Otevřený přepis pro 40 jazyků**

Hacker News · wondersky · 28. října 2026, 16:17 · 116 bodů / 20 komentářů · [diskuse](https://news.ycombinator.com/item?id=50275128)

Nvidia zveřejnila Nemotron 3.5 Transcribe, open-weight model pro automatické rozpoznávání řeči ve 40 jazycích. Je určený pro přepis nahraného zvuku a experimentálně zvládá rozlišit blízké mluvčí, což podle diskuse v jiných otevřených modelech řeči chybí.

Odkazovaný zápis na Hugging Face ho řadí mezi modely Automatic Speech Recognition a nese označení NVIDIA-Nemotron-3.5-Transcribe-30B-A4B. Stránka ho ukazuje jako čerstvě aktualizovaný přírůstek s desítkami tisíc stažení a lajků.

Nejvěcnější srovnání přinesl mewse-hn, který model právě testuje proti Parakeetu. Popisuje ho jako pomalejší, těžší a s vyšší chybovostí, i když přiznává, že zkouší kvantovanou verzi Q4, která nemusí mít plnou přesnost. Naději vidí ve vestavěném překladu, jehož test ještě běží a který by mohl vyšší nároky vyvážit. Podobně skepticky zní xpct, podle kterého Nemotron 3 na běžné slovní zásobě chybuje každých pár vět, až ho překvapilo, jak moc ho v poznávání slov sám překonává. jiehong souhlasí a za lepší označuje Parakeet nebo Qwen ASR, zároveň lituje, že Mistral neuvolnil Voxtral 3 jako open source.

Jiná větev diskuse řeší, k čemu se model vlastně hodí. solarkraft lituje omezení na nahraný zvuk a připomíná, že diktování mu prakticky vyřešil Nemotron Streaming v Handy, který velmi dobře zvládá němčinu míchanou s anglickými výrazy a značkami. PorciiVorbesc se ho hned ptá, jak si to nastavil, odpověď ale v balíčku nezazněla. Stranou pak stojí stručný dotaz wahnfrieden, jak si model vede v japonštině.

Třetí linka se točí kolem hardwaru a praktického nasazení. throwaway81523 vysvětluje zkratku ASR jako automatické rozpoznávání řeči, tedy totéž co převod řeči na text, a řeší, že model prakticky počítá s Nvidia GPU. Sám za použitelné považuje i tempo desetiny reálného času, kdy by hodinový přepis nechal přes noc počítat starý x86 stroj. Farmadupe2 oponuje, že referenční kód v Pythonu poběží na většině architektur a optimalizaci pro Intel NPU nebo cílový procesor prý zvládne jednorázový přepis za 10 až 30 USD v tokenech Opus. Do toho zapadá dotaz vjulian, který má tisíce hodinových MP3 rozhovorů se specializovanou slovní zásobou a dvěma až třemi mluvčími a zvažuje lokální aplikaci nad modelem OpenAI, který mu v posledním testu vyšel nejlépe. knicholes na to jen suše odpovídá, že odpověď se možná nikdy nedozví.

Z vlákna tak vyplývá obvyklý kompromis otevřených přepisovačů: lokální nasazení a překlad navíc proti vyšší náročnosti a zatím horší přesnosti než zavedená konkurence.
