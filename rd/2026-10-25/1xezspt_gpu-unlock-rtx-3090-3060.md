# 1xezspt
**GPU unlock: RTX 3090 a 3060 získaly po odemčení desítky procent**

r/LocalLLM · u/Flat-Career4079 · 25. října 2026, 12:18 · 735 bodů / 194 komentářů · [diskuse](https://www.reddit.com/r/LocalLLM/comments/1xezspt/)

Na r/LocalLLM se rozjela debata kolem kernelového modulu gpu_unlock, který má odstraňovat umělé půlení tensorových výpočtů FP16, BF16 a TF32 s akumulací do FP32 na geforcích s čipy Ampere GA102 a GA106. Modul podle popisu v diskusi nastupuje přes cestu SEC2 bootu ještě před tím, než se naváže běžný ovladač Nvidie, a testovalo se při pevně stažených limitech příkonu, aby byl zisk „zadarmo" bez přestřelení tepelného rozpočtu.

Nejpodrobnější čísla přinesl u/k8-bit, který změřil syntetický GEMM test násobení matic o velikosti 8192³ v PyTorch na RTX 3060 12GB při limitu 170 W a na třech RTX 3090 při 270 W. Na slabší kartě vyskočil výkon v BF16 o 80 % z 26,5 na 47,6 TFLOPS, ve FP16 o 74 % z 26,7 na 46,5 TFLOPS a v TF32 o 76 % z 13,3 na 23,4 TFLOPS. Na RTX 3090 byl relativní zisk menší, tedy BF16 o 45 % z 63,5 na 92,4 TFLOPS, FP16 o 37 % z 62,1 na 85,1 TFLOPS a TF32 o 56 % z 34,6 na 54,0 TFLOPS, zatímco INT8 zůstal v obou případech prakticky beze změny. Právě proto se v komentářích řeší, že odemčení pomáhá hlavně tréninku a inferenci v poloviční přesnosti, ne kvantovaným modelům v nízkých bitech.

Vlákno to rychle stočilo k humoru i skepsi. u/WolFlow2021 zavzpomínal na vtip, že se procesor 486SX dal předělat na DX vyvrtáním díry na správném místě čipu, a u/pandi85 to shrnul hláškou, že po pálení tokenů je včerejší, teď se budou pálit čipy. Vážnější linku otevřel u/Real_MakinThings otázkou, k čemu je zisk ve FP16 a BF16, když se dnes všichni snaží o co nejnižší kvantizaci, a u/GaelOffMySoul rýpl, že BF16 na těchto kartách stejně nikdo nepoužívá, ale potěší to.

Zbytek diskuse je praktický: jestli má modul nějaký zjistitelný škodlivý účinek na grafiku, zda zatím chodí jen na Linuxu a jestli půjde rozšířit na další karty. Lidé se hlásí s RTX 3060 Ti, kde je podle u/Slasher006 vše snadno vratné, protože jde nabootovat s úpravou i bez ní, i s 20GB verzí RTX 3080, kde je ale zrychlení ve Stratě sotva měřitelné. Padají dotazy na GeForce RTX 2070 Super, Teslu V100, kartu CMP 170HX či řadu 5000 a na to, zda se zisk projeví i mimo lokální modely, třeba v DLSS upscalingu a generování snímků. Paralelní vlákno na r/StableDiffusion pak ukazuje rozšíření snahy na řadu RTX 2000 přes projekt KohakUnlock.

Kdo má Ampere v linuxovém stroji na lokální modely, tomu může odemek přinést citelný kus výkonu v poloviční přesnosti zdarma, pro hraní a nízkobitové kvantizace ale zatím důvod k nadšení chybí.
