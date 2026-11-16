# 1x2bsk1
**Iris-3B: třímiliardový model maluje pixely přímo, bez VAE**

r/StableDiffusion · u/Deadity · 10. října 2026, 12:19 · 253 bodů / 50 komentářů · [diskuse](https://www.reddit.com/r/StableDiffusion/comments/1x2bsk1/)

Uživatel u/Deadity sdílel odkaz na model speridlabs/iris-3b, který má generovat obraz přímo v pixelovém prostoru, tedy bez VAE a bez latentního prostoru. Příspěvek bez vlastního textu je označený jako novinka a během pár hodin nasbíral slušnou pozornost.

Odkaz míří na stránku modelu na Hugging Face a v balíčku je k němu jen strohá stopa po článku s označením Paper 2610.09450, publikovaném před čtyřmi dny. Víc detailů o architektuře nebo tréninku se z dostupných úryvků vyčíst nedá, celá debata se tak odehrává v komentářích.

Nejvíc hlasů dostal nápad uživatele u/KS-Wolf-1978, že by bylo zajímavé prohnat výstupy modelu detektory umělé inteligence, které se silně spoléhají právě na artefakty VAE. Když model žádný enkodér ani dekodér nepoužívá, mohly by tyhle nástroje tápat. Hned za ním se ozval u/HassanAchievedIt s typicky redditovskou nedočkavostí na odlehčenou čtyřkrokovou turbo verzi, a u/Incognit0ErgoSum si s úsměvem posteskl, že podporu pro ComfyUI zveřejnil už o den dřív a sklidil za to jen šest hlasů.

Jádro údivu shrnul u/CarllSagan: že to funguje bez latentního prostoru, to prý odporuje všemu, co o generování obrázků věděl. Na to navazuje praktická otázka u/rahjerz za nováčky, jestli tenhle směr zrychlí generování, zlepší kvalitu, nebo dokonce sníží nároky na hardware. Podobně se ptají u/diffusion_throwaway a u/PhilosopherSweaty826, jaké jsou vlastně výhody modelů bez VAE, a u/FartingBob se přiznává, že jako příležitostný uživatel stejně netuší, co VAE a latentní prostor přesně znamenají, ale experimenty novými směry vítá.

Nechybí ani zasazení do kontextu. Uživatel u/roxoholic se ptá, čím se liší od Chroma Radiance nebo PixelDiT, a u/silenceimpaired dodává, že nejde o první takový pokus, ale možná o nejlepší, a odkazuje na práci uživatele z profilu lodestones. Skepsi přináší u/DietAshamed2246, podle kterého zatím žádný z těch „pixel space" modelů neprorazil do hlavního proudu a VAE má navíc uplatnění i jako enkodér. Zvědavou tečkou je dotaz u/NimbleDave, jestli by se přímé malování pixelů nehodilo právě na pixel art a sprity v nízkém rozlišení.

Pro čtenáře z toho plyne jednoduché vodítko: Iris-3B stojí za vyzkoušení hlavně jako ukázka cesty mimo latentní prostor, ale na odpovědi o rychlosti, kvalitě a nárocích si diskuse zatím spíš klade otázky, než aby je zodpovídala.
