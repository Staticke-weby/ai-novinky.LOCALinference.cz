# 50387738
**Nvidia Kubernetes Engine: správu GPU clusterů si vezmete k sobě**

Hacker News · gkapur · 6. listopadu 2026, 04:16 · 123 bodů / 27 komentářů · [diskuse](https://news.ycombinator.com/item?id=50387738)

NVIDIA vydala NVKE, management plane pro provoz Kubernetes clusterů na vlastní NVIDIA GPU infrastruktuře. Každý workload cluster má vlastní control plane, etcd a node pools a zákazníci k němu přistupují přes Kubernetes API a kubectl. Projekt je open-source v repozitáři dsx-ai-factory/nvke, zatím ale běží jako preview, jeho API a chování se mohou měnit a do produkce se nehodí.

Dokumentace láká hlavně na snadné vyzkoušení: lokální quickstart běží na simulovaných strojích bez NVIDIA účtu a vystačí si s linuxovým hostem nebo virtuálkou s alespoň 6 CPU a 12 GiB volné paměti. Ostrá instalace už je náročnější, jediným podporovaným poskytovatelem infrastruktury je v preview NVIDIA Infra Controller, uzly se ověřují přes TPM a SPIFFE/SPIRE a na sestavení obrazů a komponent navazuje sesterský projekt NVIDIA Kubernetes Recipes.

Hned první výtka mířila na formu oznámení. jeremy_carroll napsal, že takhle dopadá, když FAQ k produktu generuje umělá inteligence, a místo popisu, co produkt dělá, přijde jen výpis dat. chandlerh se NVIDIE nezvykle zastal, že hned první odstavec to říká jasně: platformní týmy si nainstalují management plane, kterým vytvářejí a provozují clustery pro své zákazníky.

Pak se debata stočila k otázce, k čemu je to vlastně dobré. jimbokun se ptal, jestli běžný Kubernetes neumí nasazovat i na GPU, na což yjftsjthsd-h odpověděl stručným ano s odkazem na oficiální dokumentaci. Věcněji to zarámoval QuentinM: NVKE cílí na nájemnicky oddělené clustery v referenčním stacku DSX, kde se o izolaci sítě stará NICo a BlueField a host se mezi nájemníky maže a znovu atestuje, což dává smysl hlavně pro honbu za statusem NVIDIA Cloud Partner nebo pro potřebu podpory celého stacku od NVIDIE. websap otevření stacku vítal a rýpl si, že hodně negativity jde od lidí, kteří obvykle spravují tři clustery v jednom regionu přes spravovanou službu na AWS nebo GCP.

Třetí linka byla kritičtější k architektuře. Yasuraka vyčítá, že NVKE míchá několik obav, které by měly zůstat oddělené, jako CAPI, Kamaji a gpu-operator, a bral by si z něj jen kind-based bootstrapper management clusteru a integraci SPIFFE a TPM. asaiacai přitakal, že by si přál větší viditelnost právě pro CAPI a Kamaji, a ptal se, proč si mimo zajeté hyperscalery prostě nerozjet rke2 nebo k3s. Podobně antimario označil řešení za zbytečně těžké a nekomponovatelné, uzamykající k jednomu dodavateli na mnoha úrovních, a přál by si nástroje, které stávající infrastrukturu obohacují unixovým způsobem. eel k tomu přidal praktickou pochybnost, jestli by při hromadě vlastního hardwaru od NVIDIE a bez zájmu o partnerský status nebylo prostě nejjednodušší nasadit rovnou Kubernetes.

Mezi tím probleskla i nostalgie. topspin poznamenal, že zpráva o čemsi kolem Kubernetes se dostala na titulku, což bývalo před lety na denním pořádku a je docela rád, že ta doba skončila. random3 dostal flashbacky dávno zapomenutých věcí jako OpenStack a EMC Rex-ray a esseph doplnil, že OpenStacku je teď zase plno, protože Broadcom si znepřátelil většinu zákazníků VMware. luipugs si mezitím neodpustil dotaz, zda topspin právě nevymyslel zkratku BAI ve významu před umělou inteligencí.

Kdo má vlastní GPU a chce clustery pronajímat dál s atestací a izolací, tomu dává NVKE smysl prostudovat, ostatní zůstanou u lehčích cest.
