# 1x47taj
**MiniCPM-V 4.7 35B-A3B: první open-source MoE běžící na telefonu**

r/LocalLLaMA · u/Skyline34rGt · 12. října 2026, 19:16 · 198 bodů / 64 komentářů · [diskuse](https://www.reddit.com/r/LocalLLaMA/comments/1x47taj/)

Autor u/Skyline34rGt nasdílel odkaz na Hugging Face s novinkou označenou jako New Model: MiniCPM-V 4.7 ve variantě 35B-A3B. Jde o první MoE model v řadě MiniCPM-V, který zvládá porozumění jednomu i více obrázkům a videu a cílí na běh přímo na zařízení.

Podle popisu u modelu stojí plynulý běh na kombinaci techniky Lookahead Expert Scheduling, jemné kvantizace po vrstvách a spekulativního vzorkování DSpark. Vývojáři udávají rychlost dekódování přes 13 tokenů za sekundu na iPhone 17 Pro Max a slibují podporu pro iOS, Android a HarmonyOS, čipy od Rockchipu přes Intel a AMD po Arm a frameworky SGLang, vLLM, llama.cpp a Ollama včetně kvantizovaných variant GGUF, BNB, AWQ, GPTQ a FP8.

Nejvýše hodnocený komentář patří u/jacek2023, který má radost ze „vzkříšení": model se tu už jednou objevil a pak skončil na chybě 404. Mezitím byla podpora začleněna do llama.cpp, takže si ho lidé konečně mohou spustit. Na to navazuje u/OcelotOk8071 přáním, aby llama.cpp umělo i právě lookahead pro experty.

Hodně vlákna se točí kolem srovnání s Qwenem. Tvrzení, že 35B-A3B v režimu Instruct poráží Qwen3.6 35B-A3B při kratším čase inference, přijde u/danigoncalves odvážné a u/Outdatedm3m3s se ptá, jestli je to vážně na úrovni Qwenu 27B. u/Repulsive_Initial308 v něm vidí možného nástupce pětatřícítek, u/pseudonerv ale pochybuje, že by překonal Qwen 3.8 27B, a u/MerePotato postrádá širší programátorské benchmarky. Do toho zapadá postřeh u/gardenvarietyzombie, že karta modelu děkuje Qwenu 3.6 za jazykový základ – ptá se tedy, jestli jde o finetune, což u/killerstreak976 bere jako ten jediný, na který se těšil.

Praktickou linku drží pochybnosti o běhu na telefonu. u/quadra-lab označuje 13 tokenů za sekundu na iPhonu 17 Pro za působivé, ale silně pochybuje, že by to na zařízeních s HarmonyOS běželo podobně, a u/fatihmtlm se ptá, jak se to vůbec vejde do 12 GB paměti iPhonu. u/moahmo88 hlásí vlastní zkušenost slovy, že je to rychlé a hloupé, zatímco u/CiobanuXashi naopak píše, že s videem a vizí na telefonu konečně působí lokální vidění prakticky, ne jen teoreticky. Nejosobnější vsuvku přidal u/geldonyetich se vzpomínkou na měsíc na baterkách po vytopené pojistkové skříni, kdy mu telefon sloužil jako stolní počítač – právě pro takové situace mu podobné modely dávají smysl.
