# 04. Problēmas analīze, specifikācija un darba plānošana

**18 stundas (12-089 – 12-106)** · Standarta 4. temats · **SV4 īpatsvars: 10 %**

**Bloka mērķis:** izpētes rezultātā saskatīt automatizācijas iespējas reālā procesā, definēt
darba uzdevumu un izveidot programmatūras prasību specifikāciju, pēc kuras var izstrādāt
risinājumu.

**Teorija un veidnes:** [`teorija.md`](teorija.md) · **Darba fails:** [`uzdevumi.md`](uzdevumi.md)
**Specifikācijas veidne:** [`specifikacija-veidne.md`](specifikacija-veidne.md)
**Noslēgums:** SV4 — analīzes un specifikācijas aizstāvēšana (12-106)

**Eksāmenā:** 1. daļa (programmatūras dzīvescikls), 17 % no punktiem.

> Specifikācija, ko uzrakstīsi šajā blokā, ir **05. bloka individuālā projekta darba
> uzdevums**. 11. klasē tu to jau darīji vienreiz — šoreiz uzsvars ir uz **procesa analīzi**:
> ne tikai «ko lietotājs grib», bet «kur šajā procesā ir lieks darbs, ko var automatizēt».

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 04-analize-un-specifikacija/README.md && python3 bin/darbafails.py 04-analize-un-specifikacija -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 12-089 | Reāla procesa izvēle analīzei. | Atrod reālu procesu, kurā ir automatizācijas potenciāls. |
| 12-090 | Procesa attēlošana shēmā. | Attēlo pašreizējo procesu shēmā ar soļiem, lēmumiem un iesaistītajiem. |
| 12-091 | Ikdienas procesu izpēte un analīze. | Izvēlas procesa izpētes metodi un pamato izvēli. |
| 12-092 | Automatizācijas iespēju noteikšana. | Nosaka, kuras procesa daļas ir automatizējamas un kuras nav. |
| 12-093 | Problēmas precīza formulēšana. Darba uzdevums. | Formulē risināmo problēmu izmērāmi un pārvērš to darba uzdevumā. |
| 12-094 | Programmatūras prasību specifikācijas saturs un uzbūve. | Nosauc specifikācijas daļas un raksta pārbaudāmas prasības. |
| 12-095 | Patstāvīgs darbs: pilns prasību saraksts. | Uzraksta pilnu funkcionālo un nefunkcionālo prasību sarakstu. |
| 12-096 | Datu klases specifikācijā. Datu modelis. | Nosaka, kādi dati sistēmā jāglabā, un attēlo tos modelī. |
| 12-097 | Lietotāja saskarnes prototips. Struktūrskices. | Izveido saskarnes prototipu, kas parāda galvenos ekrānus un pārejas. |
| 12-098 | Programmatūras izstrādes modeļi. | Salīdzina izstrādes modeļus un pamato izvēli savam projektam. |
| 12-099 | Programmēšanas valodas un izstrādes vides izvēle. | Pamato valodas, bibliotēku un vides izvēli konkrētam uzdevumam. |
| 12-100 | Darba plānošana. Uzdevumu sadalīšana un termiņi. | Sadala izstrādi uzdevumos un izplāno 30 stundu darbu. |
| 12-101 | Patstāvīgs darbs: specifikācijas pabeigšana. | Pabeidz specifikāciju atbilstoši veidnei. |
| 12-102 | Cita specifikācijas recenzēšana. | Izvērtē citu specifikāciju pēc kritērijiem un sniedz konkrētu atgriezenisko saiti. |
| 12-103 | Specifikācijas labošana pēc recenzijām. | Ievieš uzlabojumus, pamatojoties uz saņemto atgriezenisko saiti. |
| 12-104 | Projekta riski un pieņēmumi. | Nosaka projekta riskus un plāno rīcību to iestāšanās gadījumā. |
| 12-105 | Analīzes un specifikācijas aizstāvēšanas sagatavošana. | Sagatavo savas izpētes un lēmumu pamatojumu. |
| 12-106 | Analīzes un specifikācijas aizstāvēšana. | Pamato procesa analīzi, problēmas definējumu, prasības un izvēles. |

<!-- TABULA:BEIGAS -->

---

## 12-089 · Sprints: procesa izvēle
`[A]` `teorija`

**Tēma:** Reāla procesa izvēle analīzei.
**SR:** Atrod reālu procesu, kurā ir automatizācijas potenciāls.
**Standarts:** T.A.2.4.1.

**Uzdevumi**
1. Nedēļas laikā novēro trīs reālus procesus (skolā, mājās, darbā, pulciņā) un pieraksti,
   kas katrā notiek soli pa solim.
2. Katram pieraksti, cik ilgi tas aizņem un cik bieži notiek.
3. Izvēlies vienu un pamato, kāpēc tieši tas ir vērts automatizēt.
4. ★ Pieraksti, cik daudz laika gadā ietaupītu, ja process būtu divreiz ātrāks.

**Sprints:** `process.md` ar trim aprakstiem un izvēli

## 12-090 · Sprints: procesa kartēšana
`[A]` `prakse`

**Tēma:** Procesa attēlošana shēmā.
**SR:** Attēlo pašreizējo procesu shēmā ar soļiem, lēmumiem un iesaistītajiem.
**Standarts:** T.A.2.4.1.

**Uzdevumi**
5. Uzzīmē izvēlētā procesa shēmu: soļi, lēmumu punkti, kas ko dara.
6. Atzīmē shēmā vietas, kur notiek manuāla datu pārrakstīšana.
7. Atzīmē vietas, kur visbiežāk rodas kļūdas.
8. ★ Atzīmē, cik ilgi aizņem katrs solis, un atrodi šaurāko vietu.

**Sprints:** procesa shēma repozitorijā

## 12-091 · Procesu analīzes metodes
`[K]` `teorija` · `teorija.md` §1

**Tēma:** Ikdienas procesu izpēte un analīze.
**SR:** Izvēlas procesa izpētes metodi un pamato izvēli.
**Standarts:** T.A.2.4.1.

**Gaita**
- 10' — četri jautājumi par jebkuru procesu: kas tas ir, ko var automatizēt, kāpēc tas
  vajadzīgs, kam būs ieguvums
- 15' — metodes: novērojums, intervija, dokumentu analīze, laika mērīšana
- 10' — kopīgi: viena skolēna process uz tāfeles, klase uzdod jautājumus
- 5' — izpētes plāns

**Uzdevumi**
9. Aizpildi četru jautājumu tabulu par savu procesu.
10. Izvēlies divas izpētes metodes un pamato.
11. Uzraksti izpētes plānu: ar ko runāsi, ko mērīsi, ko dokumentēsi.
12. ★ Pieraksti, kāda informācija tev pietrūkst un kā to iegūsi.

**Mājasdarbs:** 11. uzdevums

## 12-092 · Automatizācijas potenciāls
`[K]` `jaukta` · `teorija.md` §2

**Tēma:** Automatizācijas iespēju noteikšana.
**SR:** Nosaka, kuras procesa daļas ir automatizējamas un kuras nav.
**Standarts:** T.A.2.4.1.

**Gaita**
- 10' — kas ir labs automatizācijas kandidāts: atkārtojas, ir likumsakarīgs, prasa daudz laika
- 10' — kas nav: reti, prasa spriedumu, mainās katru reizi
- 15' — uzdevumi
- 5' — kļūda, ko izdara visi: automatizēt to, kas ir interesanti, ne to, kas sāp

**Uzdevumi**
13. Sadali sava procesa soļus trīs grupās: pilnībā automatizējams, daļēji, nav.
14. Katram pamato ar konkrētu iemeslu.
15. Novērtē ieguvumu: cik laika vai kļūdu ietaupītu katrā gadījumā.
16. ★ Atrodi soli, kurš izskatās automatizējams, bet nav, un paskaidro, kāpēc.

**Mājasdarbs:** 13. uzdevums

## 12-093 · Problēmas un darba uzdevuma definēšana
`[K]` `jaukta` · FV7 (papīrs) · `teorija.md` §3

**Tēma:** Problēmas precīza formulēšana. Darba uzdevums.
**SR:** Formulē risināmo problēmu izmērāmi un pārvērš to darba uzdevumā.
**Standarts:** T.A.2.4.1.

**Gaita**
- 15' — **FV7** uz papīra, datori aizvērti
- 10' — «process ir neefektīvs» nav formulējums; laba formulējuma pazīmes
- 10' — ar ko darba uzdevums atšķiras no problēmas un no specifikācijas
- 5' — apjoms: kas ietilpst un kas neietilpst

**Uzdevumi**
17. Uzraksti savas problēmas formulējumu, kurā ir skaitlis.
18. Iedod to sola biedram; viņš pieraksta, kas viņam nav skaidrs, un tu pārraksti.
19. Uzraksti savu darba uzdevumu vienā rindkopā.
20. Uzraksti sarakstu, kas neietilpst apjomā, ar pamatojumu.
21. ★ Uzraksti, kā tu izmērīsi, vai problēma ir atrisināta.

**Mājasdarbs:** 19. uzdevums

## 12-094 · Prasību specifikācija
`[K]` `jaukta` · `teorija.md` §§4–5

**Tēma:** Programmatūras prasību specifikācijas saturs un uzbūve.
**SR:** Nosauc specifikācijas daļas un raksta pārbaudāmas prasības.
**Standarts:** T.A.2.4.4.

**Gaita**
- 10' — sešas specifikācijas daļas pēc standarta
- 10' — funkcionālās un nefunkcionālās prasības; kas ir pārbaudāma prasība
- 15' — uzdevumi: pirmās prasības kopā uz tāfeles, tad katrs savas
- 5' — apjoma pārbaude: vai tas ietilpst 30 stundās?

**Uzdevumi**
22. Sāc aizpildīt veidni: problēma, mērķis, lietotāju lomas.
23. Uzraksti piecas funkcionālās prasības un katrai pārbaudes veidu.
24. Novērtē, cik stundu izstrāde aizņems, un salīdzini ar 05. bloka 30 stundām.
25. ★ Ja tavs uzdevums neietilpst 30 stundās, samazini to un pieraksti, ko izmet.

**Mājasdarbs:** 23. uzdevums

## 12-095 · Sprints: prasību rakstīšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: pilns prasību saraksts.
**SR:** Uzraksta pilnu funkcionālo un nefunkcionālo prasību sarakstu.
**Standarts:** T.A.2.4.4.

**Uzdevumi**
26. Uzraksti vismaz 12 funkcionālās prasības ar pārbaudes veidu katrai.
27. Uzraksti vismaz 4 nefunkcionālās prasības.
28. Katrai prasībai pieraksti prioritāti: obligāta, vēlama, ja paliek laiks.
29. ★ Pārbaudi katru prasību: vai to var pārbaudīt, nezinot, kā tā realizēta?

**Sprints:** prasību saraksts specifikācijā

## 12-096 · Sprints: datu klases un modelis
`[A]` `prakse`

**Tēma:** Datu klases specifikācijā. Datu modelis.
**SR:** Nosaka, kādi dati sistēmā jāglabā, un attēlo tos modelī.
**Standarts:** T.A.2.4.4. · T.A.2.3.2.

**Uzdevumi**
30. Izraksti no savām prasībām visas lietas, par kurām jāglabā dati.
31. Uzzīmē ER modeli un pārvērs to tabulās.
32. Pārbaudi katru prasību: vai dati tās izpildei ir modelī?
33. ★ Atrodi prasību, kurai vajadzīgi dati, ko tu nevari iegūt, un pieraksti risinājumu.

**Sprints:** ER modelis un tabulas specifikācijā

## 12-097 · Prototips
`[K]` `prakse` · `teorija.md` §7

**Tēma:** Lietotāja saskarnes prototips. Struktūrskices.
**SR:** Izveido saskarnes prototipu, kas parāda galvenos ekrānus un pārejas.
**Standarts:** T.A.2.4.4.

**Gaita**
- 5' — prototips nav dizains; tā mērķis ir pārbaudīt loģiku
- 15' — ekrānu saraksts un pārejas starp tiem
- 15' — uzdevumi
- 5' — prototipa pārbaude: iedod cilvēkam un vēro, kur viņš apstājas

**Uzdevumi**
34. Uzskaiti visus ekrānus, kas sistēmai vajadzīgi.
35. Uzzīmē katram struktūrskici un atzīmē, kas notiek pēc katras darbības.
36. Uzzīmē pāreju shēmu starp ekrāniem.
37. ★ Parādi prototipu cilvēkam, kas tavu ideju nezina, un pieraksti, kur viņš apjuka.

**Mājasdarbs:** 34. uzdevums

## 12-098 · Izstrādes modeļa izvēle
`[K]` `teorija` · `teorija.md` §8

**Tēma:** Programmatūras izstrādes modeļi.
**SR:** Salīdzina izstrādes modeļus un pamato izvēli savam projektam.
**Standarts:** T.A.2.4.2.

**Gaita**
- 15' — ūdenskrituma, V-modelis, iteratīvais, pakāpeniskais, Agile: kā katrs strādā
- 10' — kad kurš der; kāpēc ūdenskritums nav automātiski slikts
- 10' — uzdevumi
- 5' — kāds modelis ir mūsu 05. un 06. blokam un kāpēc

**Uzdevumi**
38. Aizpildi salīdzinājuma tabulu par pieciem modeļiem.
39. Izvēlies modeli savam projektam un pamato ar diviem argumentiem.
40. Pieraksti, kāds modelis būtu piemērots lidmašīnas vadības programmatūrai un kāpēc.
41. ★ Pieraksti, kas notiek, ja Agile pieeju lieto projektā ar fiksētu līgumu un termiņu.

**Mājasdarbs:** 38. uzdevums

## 12-099 · Valodas un vides izvēle
`[K]` `jaukta` · `teorija.md` §9

**Tēma:** Programmēšanas valodas un izstrādes vides izvēle.
**SR:** Pamato valodas, bibliotēku un vides izvēli konkrētam uzdevumam.
**Standarts:** T.A.2.4.12.

**Gaita**
- 10' — kritēriji: uzdevuma tips, bibliotēkas, tava pieredze, uzturēšana
- 10' — kad izvēle ir principiāla un kad tā ir gaumes jautājums
- 15' — uzdevumi
- 5' — «izvēlējos, jo protu» ir derīgs arguments, ja to pasaka godīgi

**Uzdevumi**
42. Izvēlies valodu, bibliotēkas un vidi savam projektam un pamato katru izvēli.
43. Pieraksti vienu alternatīvu un kāpēc to neizvēlējies.
44. ★ Pieraksti, kas mainītos, ja sistēmai būtu 10 000 lietotāju, nevis 10.

**Mājasdarbs:** 42. uzdevums

## 12-100 · Plānošana
`[K]` `prakse` · `teorija.md` §10

**Tēma:** Darba plānošana. Uzdevumu sadalīšana un termiņi.
**SR:** Sadala izstrādi uzdevumos un izplāno 30 stundu darbu.
**Standarts:** T.A.2.4.2.

**Gaita**
- 10' — 30 stundas: kā tās reāli sadalās starp izstrādi, testēšanu un dokumentāciju
- 10' — uzdevumu izmērs un atkarības
- 15' — uzdevumi
- 5' — rezerve plānā: kāpēc 20 % un kāpēc tā vienmēr izlietojas

**Uzdevumi**
45. Sadali savu projektu vismaz 20 uzdevumos, katrs vienas stundas apjomā.
46. Atzīmē atkarības: kas jāizdara pirms kā.
47. Izveido laika plānu 05. bloka 30 stundām ar diviem starpposmiem.
48. Uzraksti sarakstu «ko izmetīšu», ja pietrūks laika.
49. ★ Ievieto uzdevumus GitHub Projects dēlī ar termiņiem.

**Mājasdarbs:** 46. uzdevums

## 12-101 · Sprints: specifikācijas pabeigšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: specifikācijas pabeigšana.
**SR:** Pabeidz specifikāciju atbilstoši veidnei.
**Standarts:** T.A.2.4.4.

**Uzdevumi**
50. Pabeidz visas specifikācijas daļas.
51. Pievieno prototipu, datu modeli un plānu.
52. ★ Pievieno sadaļu par riskiem: kas var neizdoties un ko darīsi tad.

**Sprints:** `SPECIFIKACIJA.md` repozitorijā

## 12-102 · Sprints: savstarpējā recenzēšana
`[A]` `prakse`

**Tēma:** Cita specifikācijas recenzēšana.
**SR:** Izvērtē citu specifikāciju pēc kritērijiem un sniedz konkrētu atgriezenisko saiti.
**Standarts:** T.A.2.4.4. · Ieradumi

**Uzdevumi**
53. Recenzē divas specifikācijas pēc dotajiem kritērijiem.
54. Katrai uzraksti trīs jautājumus, uz kuriem tā neatbild.
55. ★ Atrodi prasību, kas nav pārbaudāma, un piedāvā pārrakstījumu.

**Sprints:** recenzijas klasesbiedru repozitorijos

## 12-103 · Specifikācijas uzlabošana
`[K]` `prakse`

**Tēma:** Specifikācijas labošana pēc recenzijām.
**SR:** Ievieš uzlabojumus, pamatojoties uz saņemto atgriezenisko saiti.
**Standarts:** T.A.2.4.4.

**Gaita**
- 10' — saņemto piezīmju apskats; kuras pieņemt un kuras ne
- 25' — labošana
- 5' — commit ar aprakstu, kas mainīts

**Uzdevumi**
56. Izlabo specifikāciju pēc recenzijām un pieraksti, ko mainīji.
57. Vienai piezīmei, ko nepieņēmi, pieraksti pamatojumu.
58. ★ Pārbaudi, ka katrai prasībai ir pārbaudes veids.

**Mājasdarbs:** commit ar labojumiem

## 12-104 · Riski un pieņēmumi
`[K]` `jaukta` · `teorija.md` §11

**Tēma:** Projekta riski un pieņēmumi.
**SR:** Nosaka projekta riskus un plāno rīcību to iestāšanās gadījumā.
**Standarts:** T.A.2.4.2.

**Gaita**
- 10' — kas ir risks un kas — pieņēmums; kāpēc abus pieraksta
- 10' — riska novērtējums: varbūtība un ietekme
- 15' — uzdevumi
- 5' — biežākais risks skolas projektos: apjoms ir par lielu

**Uzdevumi**
59. Uzskaiti vismaz piecus sava projekta riskus.
60. Novērtē katru pēc varbūtības un ietekmes.
61. Trim lielākajiem pieraksti rīcības plānu.
62. ★ Uzskaiti pieņēmumus, uz kuriem balstās tavs plāns, un pieraksti, kas notiks, ja kāds
    izrādīsies nepatiess.

**Mājasdarbs:** 60. uzdevums

## 12-105 · Gatavošanās aizstāvēšanai
`[K]` `jaukta`

**Tēma:** Analīzes un specifikācijas aizstāvēšanas sagatavošana.
**SR:** Sagatavo savas izpētes un lēmumu pamatojumu.
**Standarts:** T.A.2.4.1. · T.A.2.4.4.

**Gaita**
- 10' — biļešu tēmas un kritēriji
- 20' — pāros: viens velk izmēģinājuma biļeti, otrs jautā
- 10' — biežākās nepilnības atbildēs

**Uzdevumi**
63. Sagatavo atbildi uz jautājumu «kā tu noteici, ka šo procesu ir vērts automatizēt».
64. Sagatavo atbildi uz jautājumu «kāpēc izvēlējies tieši šo izstrādes modeli».
65. ★ Sagatavo atbildi uz jautājumu «kas tavā plānā ir riskantākais».

**Mājasdarbs:** gatavoties SV4

## 12-106 · SV4: aizstāvēšana
`[K]` `pārbaudes darbs`

**Tēma:** Analīzes un specifikācijas aizstāvēšana.
**SR:** Pamato procesa analīzi, problēmas definējumu, prasības un izvēles.
**Standarts:** komplekss SR

**Gaita**
- 40' — biļetes: divi jautājumi katram, atbilde 5 min, rādot savu dokumentu

**Materiāli:** SV4 biļetes un kritēriji (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Atšķirība no 11. klases specifikācijas ir procesa analīze.** 11. klasē skolēns jautāja
  lietotājam, ko viņš grib. Šeit viņš novēro procesu un atrod, kur ir lieks darbs. Standarts
  to formulē kā «saskatīt automatizācijas iespējas dažādos ikdienas darba procesos».
- **12-089 un 12-090 ir sprinti ar nolūku.** Procesu nevar novērot klasē — tas jādara nedēļas
  laikā, tur, kur process notiek.
- **Apjoms ir galvenais risks.** 12-094 23. uzdevums (novērtē stundas) un 12-100 48. uzdevums
  (ko izmetīšu) ir tie divi, kas pasargā 05. bloku. Ja skolēna plāns neietilpst 30 stundās,
  to labo tagad, ne martā.
- **Šis bloks sedz eksāmena 1. daļu.** Dzīvescikls, izstrādes modeļi, prasību veidi un
  problēmas definēšana — tur tie parādās kā izvērsto atbilžu uzdevumi, ne kā kods.
