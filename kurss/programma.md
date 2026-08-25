# Programmēšana II — kursa programma (12. klase)

Padziļinātais kurss **Programmēšana II** (augstākais mācību satura apguves līmenis) ir
210 stundas. Skolā tas tiek īstenots viena gada laikā pa 6 stundām nedēļā, no kurām divas
ir patstāvīgais darbs. Reāli mācību gadā sanāk ~186 stundas, kas ietilpst standarta
pieļautajā samazinājumā.

**Priekšnosacījums:** apgūts pamatkurss Programmēšana I (10. un 11. klase).

## Standarta temati un to segums

| Standarta temats | St. standartā | Mūsu bloks | St. |
| --- | --- | --- | --- |
| 1. Objektorientēta programmēšana un ārējās bibliotēkas | 30 | 01 | 28 |
| 2. Datortīkla, servera un drošas datubāzes izveide | 30 | 02 | 28 |
| 3. Datu struktūras, programmsaskarne (API), mašīnmācīšanās | 36 | 03 | 32 |
| 4. Problēmas analīze, programmatūras specifikācija un darba plānošana | 24 | 04 | 18 |
| 5. Programmatūras izstrāde | 42 | 05 | 32 |
| 6. Produkta izveide grupā | 54 | 06 | 28 |
| — | — | 07 (eksāmena finišs) | 20 |

## Kursa apguves prasības un īpatsvars

Standarts nosaka piecas prasības ar noteiktu īpatsvaru vērtējumā. Ceturtā dalās divās daļās,
tāpēc mums ir seši summatīvie darbi.

| Prasība | Bloks | Īpatsvars |
| --- | --- | --- |
| 1. Programmprodukta izveide objektorientētā vidē, izmantojot ārējās bibliotēkas | 01 | 15 % |
| 2. Datortīkla, servera un drošas datubāzes izveide un konfigurācija | 02 | 15 % |
| 3. Programmprodukts ar datu struktūrām, API un mašīnmācīšanos | 03 | 15 % |
| 4.a Problēmas analīze, specifikācija un darba plānošana | 04 | 10 % |
| 4.b Programmatūras izstrāde | 05 | 20 % |
| 5. Programmprodukta izveide, sadarbojoties komandā | 06 | 25 % |

## Bloki

### 01. Objektorientētā programmēšana un ārējās bibliotēkas — 28 st.
**Mērķis:** izmantojot objektorientētas programmēšanas valodas pamatprincipus un bibliotēkas,
izstrādāt konkrētu programmatūras risinājumu.

- **Izpētes jautājumi:** Kādi ir OOP pamatprincipi? Kur tiek deklarēti iekšējie mainīgie un
  funkcijas? Kādam nolūkam lieto konstruktorus? Kādam nolūkam nepieciešama abstrakcija,
  iekapsulēšana, mantošana, polimorfisms?
- **SR:** Skaidro OOP pamatprincipus, veido programmas objektorientētā valodā (T.A.2.4.15.) ·
  Izmanto valodas un tās bibliotēku dokumentāciju, lai patstāvīgi apgūtu jaunas iespējas
  (T.A.2.4.10.)
- **Jēdzieni:** klase, objekts, konstruktors, `self`, abstrakcija, iekapsulēšana, mantošana,
  polimorfisms, standarta bibliotēka, grafiskā lietotāja saskarne
- **Vērtēšana:** SV1 — programmprodukts ar grafisko saskarni (15 %)

### 02. Datortīkls, serveris un droša datubāze — 28 st.
**Mērķis:** izveidot un konfigurēt daudzlietotāju lokālu tīklu, izveidot serveri izstrādātāja
vajadzībām, izplānot un realizēt datubāzes pielietojumu programmproduktā.

- **Izpētes jautājumi:** Kāds ir relāciju pielietojums datubāzē? Kas ir kriptēšana un kāds ir
  tās pielietojums? Ko ietver maršrutētāja noklusētā konfigurācija? Kas ir dinamiskā un
  statiskā IP adrese? Kāda ir tīmekļa servera problemātika, to uzturot vai nomājot?
- **SR:** Plāno datubāzi, t. sk. veido ER modeli (T.A.2.3.2.) · Izveido datu apstrādes sistēmu
  ar paša veidotu datubāzi (T.A.2.4.17.) · Izmanto kriptogrāfijas metodes (T.A.3.1.2.) ·
  Izveido un konfigurē tīklu un serveri (T.A.2.3.1.)
- **Jēdzieni:** ER modelis, normalizācija, relācija, indekss, transakcija, jaucējfunkcija,
  publiskā un privātā atslēga, IP adrese, MAC adrese, portu pāradresācija, HTTPS
- **Vērtēšana:** SV2 — tīkla, servera un datubāzes izveide ar dokumentāciju (15 %)

### 03. Datu struktūras, programmsaskarne, mašīnmācīšanās — 32 st.
**Mērķis:** izmantojot atvērtā koda bibliotēkas un dažādas datu struktūras, izstrādāt API
risinājumu un pielietot mašīnmācīšanās principus.

- **Izpētes jautājumi:** Kā pielieto atvērtā koda bibliotēkas un kādi ir riski? Kā izveidot
  API atbildi? Kādam mērķim paredzētas dažādas datu struktūras? Kādi ir mašīnmācīšanās principi?
- **SR:** Meklē un pievieno atvērtā koda bibliotēkas, lieto API (T.A.2.4.11.) · Izmanto
  dažādas datu struktūras un ar tām saistītos pamatalgoritmus (T.A.2.4.14.) · Lieto gatavu
  mašīnmācīšanās algoritmu (T.A.2.4.18.)
- **Jēdzieni:** masīvs, kopa, ieraksts, steks, rinda, saraksts, koks, grafs, datne,
  algoritma sarežģītība, API galapunkts, API atslēga, vadītā un nevadītā mašīnmācīšanās
- **Vērtēšana:** SV3 — programmprodukts ar datu struktūrām, API un ML (15 %)

### 04. Problēmas analīze, specifikācija, plānošana — 18 st.
**Mērķis:** izpētes rezultātā saskatīt automatizācijas iespējas, definēt darba uzdevumu un
izveidot programmatūras prasību specifikāciju.

- **SR:** Veic izpēti, analizē ikdienas procesus (T.A.2.4.1.) · Definē problēmu un formulē
  darba uzdevumu (T.A.2.4.1.) · Veido prasību specifikāciju, izvēlas izstrādes modeli,
  valodu un vidi, pamato izvēli (T.A.2.4.2., T.A.2.4.4., T.A.2.4.12.)
- **Jēdzieni:** procesa analīze, automatizācijas potenciāls, lietotāja profils, prasību
  specifikācija, prototips, struktūrskice, izstrādes modelis
- **Vērtēšana:** SV4 — analīze un specifikācija ar aizstāvēšanu (10 %)

### 05. Programmatūras izstrāde — 32 st.
**Mērķis:** strukturējot programmas kodu, izstrādāt programmatūru, izmantojot izstrādes
labās prakses principus.

- **SR:** Izstrādā programmatūru, lietojot labās prakses principus koda pierakstā un
  strukturēšanā (T.A.2.4.13., T.A.2.4.19., T.A.2.4.6., T.A.2.4.9.) · Veic programmatūras
  testēšanu (T.A.2.4.6., T.A.2.4.9.)
- **Jēdzieni:** vienībtestēšana, integrācijas testēšana, akcepttestēšana, atkļūdošana,
  versiju pārvaldība, zars (branch), koda pārskatīšana
- **Vērtēšana:** SV5 — individuāls programmprodukts (20 %)

### 06. Produkts komandā — 28 st.
**Mērķis:** izstrādāt programmvadāmu risinājumu komandā, sadalot darba pienākumus un
īstenojot visus izstrādes dzīves cikla posmus.

- **SR:** Veic projektēšanu un plānošanu, sadala pienākumus (T.A.2.4.5.) · Izstrādā
  programmatūru komandā, dokumentējot katru posmu (T.A.2.4.3.) · Vienojas par vienotu koda
  stilu (T.A.2.4.8.) · Veic vienību, integrācijas un akcepttestēšanu (T.A.2.4.6.) · Lieto
  projektu un versiju pārvaldības rīkus (T.A.2.4.9.) · Novērtē algoritmu sarežģītību
  (T.A.2.4.16.) · Izstrādā izvēršanas plānu, ceļvedi un uzturēšanas plānu (T.A.2.4.7.) ·
  Izvēlas licenci (T.A.3.1.4.)
- **Jēdzieni:** komandas lomas, koda pārskatīšana, apvienošanas pieprasījums (pull request),
  konflikts, integrācija, izvēršanas plāns, uzturēšanas plāns
- **Vērtēšana:** SV6 — komandas programmprodukts (25 %)

### 07. Eksāmena finišs — 20 st.
**Mērķis:** sagatavoties centralizētajam eksāmenam, strādājot eksāmena apstākļos.

Blokā nav jaunas vielas. Ir eksāmena uzbūves apskats, iepriekšējo gadu uzdevumi pa daļām,
trīs mēģinājuma eksāmeni īstos apstākļos un mērķtiecīga robu aizpildīšana pēc rezultātiem.
Skat. [`kurss/eksamens.md`](eksamens.md).

## Programmēšanas valodas

**Python** ir kursa galvenā valoda — tajā skolēni kārtos eksāmenu. Objektorientētā
programmēšana, datu struktūras, algoritmi un API risinājumi ir Python.

**SQL** datubāzēm, **JavaScript** tīmekļa daļai, ja projekts to prasa. Eksāmenā skolēns
drīkst izmantot jebkuru valodu, ko apguvis, bet gatavojamies Python.
