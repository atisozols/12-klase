# 04. bloks — teorija un paraugi

## §1 Procesu analīze

Katram procesam uzdod četrus jautājumus:

1. **Kas ir konkrētais process?** — soļi, kas notiek, un secība.
2. **Kurus soļus var automatizēt?** — kur dators var darīt to pašu, ko cilvēks.
3. **Kāpēc automatizācija ir vajadzīga?** — laiks, kļūdas, apjoms.
4. **Kam un kādi būs ieguvumi?** — kurš to sajutīs un cik.

Izpētes metodes:

| Metode | Ko dod | Kad lieto |
| --- | --- | --- |
| Novērojums | ko cilvēks tiešām dara | process ir redzams |
| Intervija | kāpēc viņš to dara tā | process ir galvā, ne uz papīra |
| Dokumentu analīze | kādi dati jau eksistē | ir veidlapas, tabulas, žurnāli |
| Laika mērīšana | cik tas maksā | jāpamato, ka ir vērts |

Novērojums un intervija bieži nesakrīt — cilvēks stāsta, kā **vajadzētu** notikt, bet dara
citādi. Tieši šī atšķirība parasti ir vērtīgākais atradums.

## §2 Automatizācijas potenciāls

Labs automatizācijas kandidāts:

- **atkārtojas** — notiek katru dienu vai katru nedēļu;
- **ir likumsakarīgs** — soļi ir vienādi katru reizi;
- **prasa laiku** — pietiekami daudz, lai ietaupījums būtu manāms;
- **rada kļūdas** — manuāla pārrakstīšana, aprēķini ar roku.

Slikts kandidāts: notiek reti, prasa cilvēka spriedumu, katru reizi ir citādi, vai arī
automatizācija maksātu vairāk nekā ietaupītu.

**Biežākā kļūda:** automatizēt to, kas ir interesanti, nevis to, kas sāp. Ja process aizņem
divas minūtes mēnesī, tam nav vērts rakstīt programmu — lai cik patīkami to būtu darīt.

## §3 Problēma un darba uzdevums

**Slikti:** «Pieteikšanās process ir neefektīvs.»
Nevar pārbaudīt, vai tas ir atrisināts.

**Labi:** «Pulciņu pieteikumus pieņem uz papīra. Skolotājs tos pārraksta izklājlapā, kas
aizņem apmēram 3 stundas septembrī, un katru gadu rodas 5–10 kļūdas ar dubultiem
pieteikumiem.»

Labā formulējumā ir **kas, cik bieži, cik ilgi un kāda ietekme**. Vismaz viens skaitlis.

**Problēma** apraksta pašreizējo stāvokli. **Darba uzdevums** apraksta, kas jāizstrādā.
Tos nesajauc: «vajag lietotni» nav problēma, tas jau ir risinājums.

Darba uzdevumā vienmēr ir arī **apjoms**: kas ietilpst un kas neietilpst. Otrais saraksts
ir tikpat svarīgs — tas pasargā no bezgalīga projekta.

## §4 Specifikācijas uzbūve

Standarts nosaka sešas daļas:

1. risināmā problēma un tās raksturojums;
2. automatizācijas risinājuma mērķis un uzdevumi;
3. lietotāju lomas un tām paredzētās darbības;
4. datu klases;
5. programmatūras darbības apraksts (funkcijas);
6. cita informācija pēc nepieciešamības — prototips, ierobežojumi, riski.

## §5 Prasības

**Funkcionālā** prasība apraksta, ko sistēma dara:

> F3. Sistēma neļauj pieteikties pulciņam, kurā vairs nav brīvu vietu.

**Nefunkcionālā** apraksta, cik labi:

> N1. Pieteikumu saraksta ielāde ar 500 ierakstiem nav ilgāka par 2 sekundēm.

Katrai prasībai jābūt **pārbaudāmai**. Pārbaude ir tests: ko izdarīšu un ko sagaidu.
Ja to nevar uzrakstīt, prasība ir formulēta par vaļīgu.

Prioritātes: **obligāta** (bez tās sistēma nav lietojama) · **vēlama** (uzlabo, bet nav
kritiska) · **ja paliek laiks**.

## §6 Datu klases

Datu klases ir lietas, par kurām sistēma glabā informāciju. Tās iegūst no prasībām:
katra prasība kaut ko lasa vai raksta, un tas kaut kur jāglabā.

Pārbaude abos virzienos:

- katrai prasībai — vai dati tās izpildei ir modelī?
- katrai tabulai — vai to kāda prasība tiešām lieto?

Ja tabula neatbilst nevienai prasībai, tā, visticamāk, nav vajadzīga.

## §7 Prototips

Prototips ir struktūrskices plus pāreju shēma. Tā mērķis nav skaistums, bet loģikas
pārbaude: vai lietotājs saprot, kur ir un ko darīt tālāk.

Katram ekrānam pieraksti, **kas notiek pēc katras darbības** — uz kuru ekrānu nonāk, ko
sistēma saglabā, ko parāda kļūdas gadījumā.

Pārbaudes veids: iedod prototipu cilvēkam, kas tavu ideju nezina, un lūdz izpildīt uzdevumu.
Kur viņš apstājas, tur ir problēma.

## §8 Izstrādes modeļi

| Modelis | Kā strādā | Kad der |
| --- | --- | --- |
| Ūdenskrituma | posmi pēc kārtas, atpakaļ neiet | prasības skaidras un nemainās |
| V-modelis | katram izstrādes posmam savs testēšanas posms | augstas drošības sistēmas |
| Iteratīvais | vairāki cikli, katrā uzlabo | prasības precizējas gaitā |
| Pakāpeniskais | sistēmu piegādā pa daļām | var lietot arī nepabeigtu |
| Agile | īsi sprinti, bieža atgriezeniskā saite | mainīga vide, pieejams pasūtītājs |

Ūdenskritums nav automātiski slikts: lidmašīnas vadības programmatūrai, kur prasības nosaka
regula un kļūda maksā dzīvības, tas ir pareizais modelis. Agile ar fiksētu līgumu un
termiņu savukārt nestrādā — nevar vienlaikus solīt fiksētu saturu un mainīt to gaitā.

Mūsu 05. un 06. bloks ir **iteratīvs ar starpposmiem**: divi punkti, kuros parāda paveikto
un koriģē plānu.

## §9 Valodas un vides izvēle

Kritēriji:

1. **uzdevuma tips** — tīmeklis, datu apstrāde, darbvirsmas lietotne;
2. **bibliotēkas** — vai vajadzīgais jau ir uzrakstīts;
3. **tava pieredze** — cik ātri sāksi strādāt;
4. **uzturēšana** — vai pēc gada to vēl varēs palaist.

«Izvēlējos, jo protu» ir derīgs arguments, ja to pasaka godīgi un tas iekļaujas termiņā.
Nederīgs arguments ir «jo tā ir modernā».

## §10 Plānošana

30 stundas 05. blokā reāli sadalās apmēram šādi:

| | Stundas |
| --- | --- |
| Izstrāde | 18 |
| Testēšana un labošana | 6 |
| Dokumentācija | 3 |
| Rezerve | 3 |

Uzdevums ir labs, ja to var izpildīt vienā stundā un par to var pateikt «gatavs» vai «nav».

Plānā vajadzīgas divas lietas: **starpposmi** (kas būs gatavs 10. un 20. stundā) un
**saraksts «ko izmetīšu»**. Otro uzraksti tagad, kamēr esi mierīgs.

## §11 Riski un pieņēmumi

**Risks** ir tas, kas var notikt un sabojāt plānu. **Pieņēmums** ir tas, ko tu uzskati par
pašsaprotamu, bet neesi pārbaudījis.

Riskus novērtē pēc diviem kritērijiem: cik liela varbūtība un cik liela ietekme. Rīcības
plānu raksta tiem, kur abi ir augsti.

Biežākie skolas projektu riski:

1. apjoms ir par lielu — visbiežākais;
2. ārējais pakalpojums pārstāj strādāt;
3. dati, uz kuriem balstās projekts, nav pieejami;
4. slimība vai citu priekšmetu darbi izsit no grafika.

Pirmajam risinājums ir zināms jau iepriekš: saraksts «ko izmetīšu».
