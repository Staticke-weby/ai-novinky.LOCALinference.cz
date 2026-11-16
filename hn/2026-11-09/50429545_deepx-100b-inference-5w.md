# 50429545
**DeepX slibuje inferenci 100B modelů pod 5 W. Čísla jsou ale simulovaná**

Hacker News · giuliomagnifico · 9. listopadu 2026, 19:33 · 149 bodů / 23 komentářů · [diskuse](https://news.ycombinator.com/item?id=50429545)

DeepX dokončil návrh druhé generace svého čipu pro edge AI, která sází na paměti LPDDR5X s výpočty přímo v paměti. Firma mluví o až 6,7násobném zlepšení výkonu a láká na běh modelů o desítkách až stovce miliard parametrů rychlostí 10 až 30 tokenů za sekundu v jednotkách wattů.

Podle odkazovaného článku se ale marketingové číslo 5 W vztahuje jen na modely pod 4 miliardy parametrů, zatímco stovka miliard znamená výhradně směs expertů s přibližně 3 až 20 miliardami aktivních parametrů. Uváděné metriky jsou navíc simulované, vyžadují asi 2,7krát vyšší celkový příkon kolem 13,5 W a kompilátor je zatím jen prototyp, nikoli hotová náhrada za zavedené nástroje typu Nvidia ISAAC. Po hardwarové stránce čip nabízí 80 TOP/s a propustnost 150 GB/s, bez upřesnění, pro jakou přesnost ten výkon platí.

Právě ten rozpor mezi titulkem a detaily diskusi nejvíc dráždí. Augment_me vytáhl z článku čtyři zádrhele od simulovaných čísel přes utajený příkon pamětí až po nedokončený kompilátor a NewJazz to shrnul jako zavádějící, protože husté 100miliardové modely vůbec nejsou ve hře. Idiotsecant si z 13,5 W dělá legraci, že lidský mozek jede na 10 až 20 W, takže je ještě kam se zlepšovat, zatímco sampton dodává, že jsme v teritoriu Jetson Nano.

Nejvěcnější rozbor přidal PaulKeeble, který čip postavil vedle běžné herní karty s nějakými 750 TOP/s v INT4 a 650 GB/s. Při 150 GB/s vychází dekódování na zhruba 10 tokenů za sekundu u 7miliardového aktivního modelu v kvantizaci Q4 a na 30 tokenů za sekundu jen u zhruba 2,5 miliardy aktivních parametrů. Plná FP16 se mu proto zdá nepravděpodobná a bez velkých modelů typu Qwen 27B zbývá prostor hlavně pro úsporné směsi expertů se 2 až 7 miliardami aktivních parametrů, což by ale podle něj na slušnou domácí AI stačilo.

Zbytek vlákna už řeší, co by takový úsporný čip znamenal. LaurensBER píše, že se ho v Evropě každý týden někdo ptá na provozování AI doma, protože důvěra v USA i Čínu je na dně, a lokální DeepSeek třídy Flash by pak byla jasná volba. Ilaksh jde ještě dál a tipuje, že do 18 až 36 měsíců bude výkonná lokální AI všude, zatímco ares623 připomíná, že každá optimalizace pro datacentra zlevňuje i domácí běh. Skepsi drží nomorewords, kterému v materiálech chybí rychlost zpracování vstupního promptu a bojí se zdražení pamětí s výpočty v paměti, a kylehotchkiss, který za dlouhý běh modelu Gemma na stolním čipu M5U naměřil kolem 72 W a v San Diegu to prý na účtu za elektřinu pozná.

Z diskuse tak zbývá jednoduchý obrázek: myšlenka úsporné inference doma lidi láká, ale dokud DeepX neukáže reálná měření místo simulací, zůstane slib o stovce miliard parametrů za pár wattů spíš reklamou než plánem na nákup.
