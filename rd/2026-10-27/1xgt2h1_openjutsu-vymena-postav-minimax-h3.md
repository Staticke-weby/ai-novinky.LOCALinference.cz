# 1xgt2h1
**Openjutsu: lokální výměna postav ve videu s MiniMax H3**

r/StableDiffusion · u/Devajyoti1231 · 27. října 2026, 14:50 · 412 bodů / 92 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1xgt2h1/)

Vývojář postavil převážně s pomocí Claude bezplatnou lokální obdobu funkce Genjutsu od Higgsfieldu a přihlásil ji do otevřené výzvy Comfy kolem Higgsfieldu. Stačí nahrát video a fotku člověka, který v něm má být, stisknout Run a nástroj postavu najde a vymění po jednotlivých klipech, přičemž zachová původní zvuk. Kromě výměny osob umí i výměnu objektů, změnu pozadí a dodatečné opravy tváří a barev, kód zveřejnil pod licencí MIT.

Nejvíc hlasů dostala skeptická otázka u/tekprodfx16, čím se liší od dosavadních pokusů, které s MiniMaxem končily nekonzistentními výsledky. Odpověď u/Silent_Listener_95 shrnuje hlavní lákadlo: vše běží lokálně bez nahrávání dat a lidi ve scéně sám najde a sleduje kombinace SAM a Qwen, takže nejsou potřeba ruční masky ani cloudová rozhraní. Do debaty se vložil i u/Key_Cap_8111, který pro stejnou soutěž zvolil opačnou cestu s Wan Animate a SAM2, a pochválil šedý manekýn jako chytrou fintu, jak zachovat pohyb bez propisování původního oblečení.

Nadšení ale rychle narazilo na instalaci. Uživatel u/alew3 popisuje, že na Linuxu s RTX 5090 mu projdou kontrola masky, hledání lidí i oprava barev, ale všechny režimy výměny ztroskotají na kontrole chybějícím uzlem MiniMaxH3ContexLoopSourceSlice, který prý není v žádné vydané verzi Context-Loop 0.7.3. Stejnou chybějící smečku hlásí i u/Trick_Set1865, který se navíc ptá, zda návod vůbec počítá s Linuxem, a u/picapaukrk končí na hlášce o překročení zvukového okna časové osy. U/VoidedCard zase bojují s hláškou, že aplikaci se nedaří zkontrolovat ComfyUI.

Třetí linka vlákna řeší, na čem to vůbec utáhnout a jak dlouhé video zvládne. Padají dotazy na nároky na videopaměť, na sestavu s 5060 Ti se 16 GB a na to, zda nástroj načítá celé video najednou, nebo po kouscích, takže by dal i třicetiminutovou stopáž. U/Akken_Kan varuje, že video-to-video postupy v MiniMaxu trvají velmi dlouho i na nové 5090, zvlášť bez zmenšení referenčního videa. Vedle toho se mísí pobavení a podpora: u/Round_Awareness5490 tvrdí, že chystal velmi podobnou práci a chtěl ji nazvat stejně, za shodu designu viní Claude, a u/plamtastic autorovi přeje, aby v soutěži vyhrál něco lepšího než RTX 4060 Ti.

Kdo má chuť si s lokální výměnou postav hrát, najde v Openjutsu slibný, ale zatím křehký základ, u kterého hodně záleží na přesné verzi uzlů a síle grafiky.
