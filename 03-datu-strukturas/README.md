# 03. Datu struktūras, programmsaskarne, mašīnmācīšanās

**32 stundas (12-057 – 12-088)** · Standarta 3. temats · **SV3 īpatsvars: 15 %**

**Bloka mērķis:** izmantojot dažādas datu struktūras, atvērtā koda bibliotēkas un
programmsaskarnes, izstrādāt risinājumu un pamatot izvēlēto struktūru un algoritmu.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Noslēgums:** SV3 — programmprodukts (12-087, 12-088)

**Eksāmenā:** 4. daļa, 35 % no punktiem — lielākā daļa visā darbā.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 03-datu-strukturas/README.md && python3 bin/darbafails.py 03-datu-strukturas -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 12-057 | Datu struktūru veidi un to izvēle. | Nosauc galvenās datu struktūras un pamato, kura kuram uzdevumam ir piemērota. |  |
| 12-058 | Saraksts. Darbību izmaksas. | Novērtē saraksta darbību izmaksas un izvēlas darbību, kas ir lētāka. |  |
| 12-059 | Patstāvīgs darbs: algoritma izpildes laika mērīšana. | Izmēra algoritma izpildes laiku pie dažādiem datu apjomiem un attēlo rezultātu. |  |
| 12-060 | Mērījumu rezultātu izvērtēšana. | Formulē secinājumus par algoritma uzvedību pie datu apjoma pieauguma. |  |
| 12-061 | Kopa (set). Unikālas vērtības un kopu darbības. | Lieto kopu, kur svarīga unikalitāte un ātra piederības pārbaude. |  |
| 12-062 | Ieraksts kā datu struktūra. Vārdnīca, `namedtuple` un `dataclass`. | Izvēlas piemērotu veidu strukturēta ieraksta glabāšanai un pamato izvēli. |  |
| 12-063 | Steks (stack). Pēdējais iekšā — pirmais ārā. | Realizē steku un lieto to uzdevumam, kur svarīga apgrieztā secība. |  |
| 12-064 | Rinda (queue). Pirmais iekšā — pirmais ārā. | Realizē rindu un lieto to uzdevumam, kur svarīga sākotnējā secība. |  |
| 12-065 | Patstāvīgs darbs: steka un rindas pielietojums. | Izvēlas un lieto steku vai rindu reālam uzdevumam. |  |
| 12-066 | Cita risinājuma pārskatīšana. | Izvērtē cita risinājumu pēc struktūras izvēles un efektivitātes. |  |
| 12-067 | Saistītais saraksts. Mezgli un norādes. | Realizē saistīto sarakstu un salīdzina to ar masīvu. |  |
| 12-068 | Koks. Hierarhiska struktūra. | Realizē binārā meklēšanas koka pamatdarbības. | **FV5** (dators) |
| 12-069 | Koka apstaigāšana. Rekursija. | Apstaigā koku rekursīvi un skaidro apstaigāšanas secību. |  |
| 12-070 | Grafs. Virsotnes un šķautnes. | Attēlo grafu programmā un apstaigā to. |  |
| 12-071 | Patstāvīgs darbs: grafa algoritms reālam uzdevumam. | Modelē reālu situāciju kā grafu un atrisina uzdevumu. |  |
| 12-072 | Datu struktūru izvēles dokumentēšana. | Pamato rakstiski, kāpēc katrā vietā izvēlēta konkrēta struktūra. |  |
| 12-073 | Lineārā un binārā meklēšana. | Realizē abus meklēšanas algoritmus un salīdzina to efektivitāti. |  |
| 12-074 | Kārtošanas algoritmi un to salīdzinājums. | Realizē vienkāršu kārtošanas algoritmu un salīdzina to ar iebūvēto. |  |
| 12-075 | Algoritma sarežģītība. O apzīmējums. | Novērtē algoritma sarežģītību un pamato novērtējumu. |  |
| 12-076 | Praktikums: pareizās struktūras izvēle uzdevumam. | Izvēlas un realizē uzdevumam efektīvāko datu struktūru. |  |
| 12-077 | Patstāvīgs darbs: algoritmu salīdzinājums. | Salīdzina vairākus risinājumus pēc laika un atmiņas. |  |
| 12-078 | Bloka pirmās daļas izvērtējums. | Nosaka, kuras datu struktūras vēl nav droši apgūtas. |  |
| 12-079 | Programmsaskarnes lietošana. Atvērtā koda bibliotēku riski. | Lieto svešu API un izvērtē ārējas bibliotēkas pievienošanas riskus. |  |
| 12-080 | Savas programmsaskarnes izveide. | Izveido API galapunktu, kas atbild uz pieprasījumu izvēlētā formātā. |  |
| 12-081 | API atslēgas un drošība. | Skaidro API atslēgas nozīmi un glabā to droši. | **FV6** (papīrs) |
| 12-082 | Mašīnmācīšanās pamatprincipi. Vadītā un nevadītā mācīšanās. | Skaidro mašīnmācīšanās principus un atšķir tos no algoritmiskas pieejas. |  |
| 12-083 | Patstāvīgs darbs: gatava mašīnmācīšanās modeļa izmantošana. | Lieto gatavu modeli sava uzdevuma risināšanā. |  |
| 12-084 | Modeļa rezultātu izvērtēšana. | Izvērtē modeļa precizitāti un tā lietojuma robežas. |  |
| 12-085 | Summatīvā darba specifikācija un plānošana. | Izprot darba prasības un izplāno izpildi. |  |
| 12-086 | Summatīvā darba izstrāde. | Realizē risinājumu atbilstoši specifikācijai. |  |
| 12-087 | Summatīvais darbs: datu struktūras, API un mašīnmācīšanās. | Pabeidz risinājumu atbilstoši specifikācijai. | **SV3** |
| 12-088 | Summatīvā darba demonstrācija un aizstāvēšana. | Pamato datu struktūru izvēli un novērtē risinājuma sarežģītību. | **SV3** |

<!-- TABULA:BEIGAS -->

---

## 12-057 · Datu struktūru pārskats
`[K]` `teorija` · `teorija.py` §1

**Tēma:** Datu struktūru veidi un to izvēle.
**SR:** Nosauc galvenās datu struktūras un pamato, kura kuram uzdevumam ir piemērota.
**Standarts:** T.A.2.4.14.

**Gaita**
- 10' — viens uzdevums, četras struktūras: kā mainās risinājums
- 15' — pārskats: saraksts, kopa, vārdnīca, steks, rinda, koks, grafs
- 10' — divi jautājumi, pēc kuriem izvēlas: vai secība ir svarīga? kā meklēšu?
- 5' — kur to redzēsim eksāmenā

**Uzdevumi**
1. Burtnīcā: sešiem dotajiem uzdevumiem izvēlies struktūru un pamato vienā teikumā.
2. Burtnīcā: vienam uzdevumam apraksti, kā risinājums izskatītos ar divām dažādām struktūrām.
3. ★ Atrodi savā 11. klases projektā vietu, kur cita struktūra būtu bijusi labāka.

**Mājasdarbs:** 1. uzdevums

## 12-058 · Saraksts un tā cena
`[K]` `prakse` · `teorija.py` §2

**Tēma:** Saraksts. Darbību izmaksas.
**SR:** Novērtē saraksta darbību izmaksas un izvēlas darbību, kas ir lētāka.
**Standarts:** T.A.2.4.14. · T.A.2.4.16.

**Gaita**
- 5' — kāpēc `insert(0, x)` ir dārgāks par `append(x)`
- 15' — demo §2: darbību izmaksas tabula; mērīšana ar `time`
- 15' — uzdevumi
- 5' — kad tas sāk būt svarīgi: pie 100 elementiem nekad, pie miljona vienmēr

**Uzdevumi**
4. Izmēri, cik ilgi aizņem 100 000 `append` un 100 000 `insert(0, ...)` darbību.
5. Pieraksti rezultātu attiecību un paskaidro, kāpēc tā ir tāda.
6. Izmēri, cik ilgi aizņem elementa meklēšana sarakstā ar 1 000 000 elementu.
7. ★ Uzraksti funkciju, kas noņem dublikātus no saraksta, un salīdzini divus risinājumus:
   ar sarakstu un ar kopu.

**Mājasdarbs:** 5. uzdevums

## 12-059 · Sprints: sarežģītības mērīšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: algoritma izpildes laika mērīšana.
**SR:** Izmēra algoritma izpildes laiku pie dažādiem datu apjomiem un attēlo rezultātu.
**Standarts:** T.A.2.4.16.

**Uzdevumi**
8. Uzraksti funkciju, kas meklē elementu sarakstā, un izmēri tās laiku pie 1 000, 10 000,
   100 000 un 1 000 000 elementiem.
9. Saglabā rezultātus CSV un izveido diagrammu.
10. Pieraksti, kā mainās laiks, kad datu apjoms pieaug desmitkārt.
11. ★ Atkārto to pašu ar kopu un salīdzini abas līknes.

**Sprints:** `merijumi.py`, CSV un diagramma

## 12-060 · Sprints: secinājumi
`[A]` `teorija`

**Tēma:** Mērījumu rezultātu izvērtēšana.
**SR:** Formulē secinājumus par algoritma uzvedību pie datu apjoma pieauguma.
**Standarts:** T.A.2.4.16.

**Uzdevumi**
12. Pieraksti trīs secinājumus no saviem mērījumiem.
13. Prognozē, cik ilgi darbība aizņemtu pie 10 000 000 elementiem, un pamato.
14. ★ Atrodi savā mērījumā vietu, kur rezultāts neatbilda gaidītajam, un izdomā, kāpēc.

**Sprints:** `secinajumi.md`

## 12-061 · Kopa
`[K]` `prakse` · `teorija.py` §3

**Tēma:** Kopa (set). Unikālas vērtības un kopu darbības.
**SR:** Lieto kopu, kur svarīga unikalitāte un ātra piederības pārbaude.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kāpēc `x in kopa` ir tikpat ātrs pie 10 un pie 10 miljoniem
- 15' — demo §3: izveide, `add`, `in`, apvienojums, šķēlums, starpība
- 15' — uzdevumi
- 5' — ko kopa nedod: secību un dublikātus

**Uzdevumi**
15. No divu klašu skolēnu sarakstiem atrodi tos, kas ir abās, tikai vienā un vismaz vienā.
16. Noņem dublikātus no saraksta, saglabājot secību, un pieraksti, kāpēc tikai kopa te nepietiek.
17. Pārbaudi, vai divi teksti sastāv no vieniem un tiem pašiem burtiem.
18. ★ Uzraksti funkciju, kas atrod, kuri elementi ir tikai pirmajā no trim sarakstiem.

**Mājasdarbs:** 15. uzdevums

## 12-062 · Ieraksts
`[K]` `prakse` · `teorija.py` §4

**Tēma:** Ieraksts kā datu struktūra. Vārdnīca, `namedtuple` un `dataclass`.
**SR:** Izvēlas piemērotu veidu strukturēta ieraksta glabāšanai un pamato izvēli.
**Standarts:** T.A.2.4.14. · T.A.2.4.15.

**Gaita**
- 5' — trīs veidi, kā glabāt «skolēnu»: vārdnīca, tuple, klase
- 15' — demo §4: `namedtuple`, `dataclass`, kad kurš
- 15' — uzdevumi
- 5' — kāpēc `dati[2]` pēc mēneša nevienam nav saprotams

**Uzdevumi**
19. Vienam un tam pašam ierakstam izveido trīs versijas: vārdnīca, `namedtuple`, `dataclass`.
20. Pieraksti katras plusus un mīnusus.
21. Pārraksti dotu programmu, kas lieto `tuple` indeksus, uz `dataclass`.
22. ★ Pievieno `dataclass` metodi un pieraksti, ar ko tā tagad atšķiras no parastas klases.

**Mājasdarbs:** 21. uzdevums

## 12-063 · Steks
`[K]` `prakse` · `teorija.py` §5

**Tēma:** Steks (stack). Pēdējais iekšā — pirmais ārā.
**SR:** Realizē steku un lieto to uzdevumam, kur svarīga apgrieztā secība.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kur steks ir ikdienā: atsaukšana, pārlūka vēsture, izsaukumu steks
- 15' — demo §5: `push`, `pop`, `peek`; realizācija ar sarakstu un ar klasi
- 15' — uzdevumi
- 5' — kļūda, ko visi izdara: `pop` no tukša steka

**Uzdevumi**
23. Realizē klasi `Steks` ar metodēm `pievienot`, `iznemt`, `apskatit`, `ir_tukss`.
24. Uzraksti funkciju, kas pārbauda, vai iekavas izteiksmē ir pareizi sabalansētas.
25. Uzraksti funkciju, kas apgriež vārdu, izmantojot steku.
26. Pievieno savam stekam kļūdas apstrādi, ja mēģina izņemt no tukša.
27. ★ Uzraksti vienkāršu kalkulatoru pēcvārda pierakstam (`3 4 +`), izmantojot steku.

**Mājasdarbs:** 24. uzdevums

## 12-064 · Rinda
`[K]` `prakse` · `teorija.py` §6

**Tēma:** Rinda (queue). Pirmais iekšā — pirmais ārā.
**SR:** Realizē rindu un lieto to uzdevumam, kur svarīga sākotnējā secība.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kur rinda ir ikdienā: drukas uzdevumi, apkalpošana, ziņu apstrāde
- 15' — demo §6: `deque` un kāpēc ne parasts saraksts
- 15' — uzdevumi
- 5' — prioritātes rinda: kad kārta nav pēc ierašanās laika

**Uzdevumi**
28. Realizē klasi `Rinda` ar `deque` pamatā.
29. Modelē apkalpošanas rindu: pievieno klientus, apkalpo un izvadi apkalpošanas secību.
30. Salīdzini `deque.popleft()` un `saraksts.pop(0)` ātrumu pie 100 000 elementiem.
31. ★ Realizē prioritātes rindu, kur katram elementam ir svarīgums.

**Mājasdarbs:** 29. uzdevums

## 12-065 · Sprints: steks un rinda praksē
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: steka un rindas pielietojums.
**SR:** Izvēlas un lieto steku vai rindu reālam uzdevumam.
**Standarts:** T.A.2.4.14.

**Uzdevumi**
32. Uzraksti programmu, kas modelē pārlūka «atpakaļ» un «uz priekšu» pogas ar diviem stekiem.
33. Uzraksti programmu, kas apstrādā uzdevumu rindu ar prioritātēm.
34. ★ Pieraksti, kāpēc katrā gadījumā izvēlējies tieši šo struktūru.

**Sprints:** abas programmas repozitorijā

## 12-066 · Sprints: koda pārskatīšana
`[A]` `prakse`

**Tēma:** Cita risinājuma pārskatīšana.
**SR:** Izvērtē cita risinājumu pēc struktūras izvēles un efektivitātes.
**Standarts:** T.A.2.4.16. · T.A.2.4.8.

**Uzdevumi**
35. Pārskati klasesbiedra 12-065 risinājumu un pieraksti trīs piezīmes.
36. Atrodi vietu, kur cita struktūra būtu bijusi ātrāka, un pamato.
37. ★ Piedāvā konkrētu labojumu koda fragmenta veidā.

**Sprints:** `parskats.md`

## 12-067 · Saistītais saraksts
`[K]` `prakse` · `teorija.py` §7

**Tēma:** Saistītais saraksts. Mezgli un norādes.
**SR:** Realizē saistīto sarakstu un salīdzina to ar masīvu.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kāpēc vispār kaut kas cits, ja jau ir saraksts?
- 15' — demo §7: mezgls, `next`, pievienošana un izņemšana
- 15' — uzdevumi
- 5' — kur to redzam praksē: rindas, atmiņas pārvaldība

**Uzdevumi**
38. Realizē klasi `Mezgls` un klasi `SaistitaisSaraksts` ar `pievienot` un `izvadit`.
39. Pievieno metodi, kas atrod elementu un atgriež tā pozīciju.
40. Pievieno metodi, kas izņem elementu pēc vērtības.
41. Pieraksti tabulu: pievienošana, izņemšana un meklēšana masīvā pret saistīto sarakstu.
42. ★ Realizē divvirzienu saistīto sarakstu.

**Mājasdarbs:** 41. uzdevums

## 12-068 · Koks
`[K]` `prakse` · FV5 (dators) · `teorija.py` §8

**Tēma:** Koks. Hierarhiska struktūra.
**SR:** Realizē binārā meklēšanas koka pamatdarbības.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kur koks ir ikdienā: katalogi, izvēlnes, XML, ģimenes koks
- 10' — demo §8: sakne, mezgls, lapa, dziļums; binārais meklēšanas koks
- 15' — uzdevumi
- 10' — **FV5** pie datora

**Uzdevumi**
43. Realizē binārā meklēšanas koka klasi ar metodi `pievienot`.
44. Pievieno metodi `mekle`, kas atgriež `True` vai `False`.
45. Pieraksti, cik salīdzinājumu vajag, lai atrastu elementu kokā ar 1 000 mezgliem.
46. ★ Pievieno metodi, kas atgriež koka dziļumu.

**Mājasdarbs:** 44. uzdevums

## 12-069 · Koka apstaigāšana
`[K]` `prakse` · `teorija.py` §9

**Tēma:** Koka apstaigāšana. Rekursija.
**SR:** Apstaigā koku rekursīvi un skaidro apstaigāšanas secību.
**Standarts:** T.A.2.4.14. · T.A.2.4.19.

**Gaita**
- 10' — rekursija: funkcija, kas izsauc pati sevi; bāzes gadījums
- 10' — demo §9: trīs apstaigāšanas veidi un kāpēc viens no tiem dod sakārtotu virkni
- 15' — uzdevumi
- 5' — kad rekursija ir slikta ideja: dziļums un atmiņa

**Uzdevumi**
47. Realizē koka apstaigāšanu `in-order` un pārbaudi, ka rezultāts ir sakārtots.
48. Realizē `pre-order` un `post-order` un salīdzini rezultātus.
49. Uzraksti rekursīvu funkciju, kas saskaita mezglu skaitu.
50. ★ Uzraksti to pašu bez rekursijas, izmantojot steku.

**Mājasdarbs:** 47. uzdevums

## 12-070 · Grafs
`[K]` `prakse` · `teorija.py` §10

**Tēma:** Grafs. Virsotnes un šķautnes.
**SR:** Attēlo grafu programmā un apstaigā to.
**Standarts:** T.A.2.4.14.

**Gaita**
- 5' — kur grafs ir ikdienā: draugi, maršruti, atkarības
- 15' — demo §10: blakusesamības saraksts; BFS un DFS
- 15' — uzdevumi
- 5' — ar ko grafs atšķiras no koka

**Uzdevumi**
51. Attēlo doto grafu kā vārdnīcu un izvadi katras virsotnes kaimiņus.
52. Realizē apstaigāšanu plašumā (BFS) un izvadi apmeklēšanas secību.
53. Realizē apstaigāšanu dziļumā (DFS).
54. Uzraksti funkciju, kas pārbauda, vai starp divām virsotnēm ir ceļš.
55. ★ Uzraksti funkciju, kas atrod īsāko ceļu starp divām virsotnēm.

**Mājasdarbs:** 52. uzdevums

## 12-071 · Sprints: grafa uzdevums
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: grafa algoritms reālam uzdevumam.
**SR:** Modelē reālu situāciju kā grafu un atrisina uzdevumu.
**Standarts:** T.A.2.4.14. · T.A.2.4.19.

**Uzdevumi**
56. Modelē skolas telpu plānu kā grafu un atrodi īsāko ceļu starp divām telpām.
57. Pieraksti, kā tu izvēlējies virsotnes un šķautnes.
58. ★ Papildini uzdevumu ar šķautņu svariem (attālumiem) un atrodi īsāko ceļu pēc attāluma.

**Sprints:** `grafs.py` un apraksts

## 12-072 · Sprints: dokumentēšana
`[A]` `prakse`

**Tēma:** Datu struktūru izvēles dokumentēšana.
**SR:** Pamato rakstiski, kāpēc katrā vietā izvēlēta konkrēta struktūra.
**Standarts:** T.A.2.4.14.

**Uzdevumi**
59. Uzraksti `STRUKTURAS.md`: kur savā kodā lieto kuru struktūru un kāpēc.
60. Katrai pieraksti, kā mainītos programma, ja izvēlētos citu.
61. ★ Pieraksti vienu vietu, kur tava izvēle, godīgi sakot, nav labākā, un kāpēc to atstāji.

**Sprints:** `STRUKTURAS.md`

## 12-073 · Meklēšanas algoritmi
`[K]` `prakse` · `teorija.py` §11

**Tēma:** Lineārā un binārā meklēšana.
**SR:** Realizē abus meklēšanas algoritmus un salīdzina to efektivitāti.
**Standarts:** T.A.2.4.19. · T.A.2.4.16.

**Gaita**
- 5' — kā tu meklē vārdu vārdnīcā? Ne no pirmās lapas
- 15' — demo §11: lineārā un binārā meklēšana; kāpēc jābūt sakārtotam
- 15' — uzdevumi
- 5' — cik soļu vajag miljonam elementu? 20

**Uzdevumi**
62. Realizē lineāro meklēšanu un saskaiti salīdzinājumus.
63. Realizē bināro meklēšanu un saskaiti salīdzinājumus.
64. Salīdzini abus pie 1 000, 100 000 un 1 000 000 elementiem.
65. ★ Realizē bināro meklēšanu rekursīvi.

**Mājasdarbs:** 63. uzdevums

## 12-074 · Kārtošanas algoritmi
`[K]` `prakse` · `teorija.py` §12

**Tēma:** Kārtošanas algoritmi un to salīdzinājums.
**SR:** Realizē vienkāršu kārtošanas algoritmu un salīdzina to ar iebūvēto.
**Standarts:** T.A.2.4.19. · T.A.2.4.16.

**Gaita**
- 5' — kāpēc kārtošana ir dārgāka par meklēšanu
- 15' — demo §12: burbuļkārtošana, ievietošanas kārtošana, sapludināšanas kārtošana
- 15' — uzdevumi
- 5' — kāpēc praksē vienmēr lieto iebūvēto

**Uzdevumi**
66. Realizē burbuļkārtošanu un saskaiti apmaiņas.
67. Realizē ievietošanas kārtošanu un salīdzini ar burbuļkārtošanu.
68. Salīdzini abas ar `sorted()` pie 10 000 elementiem.
69. Pieraksti, kāpēc atšķirība ir tik liela.
70. ★ Realizē sapludināšanas kārtošanu rekursīvi.

**Mājasdarbs:** 68. uzdevums

## 12-075 · Algoritma sarežģītība
`[K]` `jaukta` · `teorija.py` §13

**Tēma:** Algoritma sarežģītība. O apzīmējums.
**SR:** Novērtē algoritma sarežģītību un pamato novērtējumu.
**Standarts:** T.A.2.4.16.

**Gaita**
- 10' — no mērījumiem uz apzīmējumu: O(1), O(log n), O(n), O(n log n), O(n²)
- 10' — kā to nolasīt no koda: cikls, ligzdots cikls, dalīšana uz pusēm
- 15' — uzdevumi burtnīcā
- 5' — kāpēc konstantes neraksta

**Uzdevumi**
71. Burtnīcā: astoņiem koda fragmentiem nosaki sarežģītību un pamato.
72. Burtnīcā: sakārto piecus algoritmus pēc ātruma pie liela n.
73. Novērtē savu 12-071 grafa risinājuma sarežģītību.
74. ★ Atrodi savā kodā vietu ar O(n²) un pieraksti, kā to varētu uzlabot.

**Mājasdarbs:** 73. uzdevums

## 12-076 · Praktikums: struktūras izvēle
`[K]` `prakse`

**Tēma:** Praktikums: pareizās struktūras izvēle uzdevumam.
**SR:** Izvēlas un realizē uzdevumam efektīvāko datu struktūru.
**Standarts:** T.A.2.4.14. · T.A.2.4.16.

**Gaita**
- 5' — uzdevumu nolasīšana
- 30' — patstāvīgs darbs
- 5' — divi risinājumi uz ekrāna, salīdzinām izvēles

**Uzdevumi**
75. Dotam uzdevumam ar 500 000 ierakstiem izvēlies struktūru un realizē risinājumu tā, lai
    tas izpildās mazāk nekā sekundē.
76. Pieraksti, kāpēc naivais risinājums būtu par lēnu.
77. ★ Uzlabo savu risinājumu vēl divkārt un izmēri starpību.

**Mājasdarbs:** pabeigt

## 12-077 · Sprints: algoritmu salīdzināšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: algoritmu salīdzinājums.
**SR:** Salīdzina vairākus risinājumus pēc laika un atmiņas.
**Standarts:** T.A.2.4.16.

**Uzdevumi**
78. Vienam uzdevumam uzraksti trīs risinājumus ar dažādām struktūrām.
79. Izmēri katra laiku un pieraksti sarežģītību.
80. ★ Izmēri arī atmiņas patēriņu un pieraksti, kur ir kompromiss.

**Sprints:** `salidzinajums.md` ar mērījumiem

## 12-078 · Sprints: refleksija
`[A]` `teorija`

**Tēma:** Bloka pirmās daļas izvērtējums.
**SR:** Nosaka, kuras datu struktūras vēl nav droši apgūtas.
**Standarts:** T.A.2.4.14.

**Uzdevumi**
81. Aizpildi paštestu: septiņas struktūras, katrai atzīmē — protu, protu daļēji, neprotu.
82. Katrai «neprotu» pozīcijai atrodi vienu uzdevumu un izpildi to.
83. ★ Uzraksti sev atgādni ar septiņu struktūru izvēles kritērijiem vienā lapā.

**Sprints:** `pastests.md` un atgādne

## 12-079 · API lietošana un riski
`[K]` `prakse` · `teorija.py` §14

**Tēma:** Programmsaskarnes lietošana. Atvērtā koda bibliotēku riski.
**SR:** Lieto svešu API un izvērtē ārējas bibliotēkas pievienošanas riskus.
**Standarts:** T.A.2.4.11.

**Gaita**
- 10' — kas notiek, ja bibliotēka, ko lieto tavs projekts, tiek pamesta vai uzlauzta
- 10' — demo §14: API pieprasījums, atbildes apstrāde, ierobežojumi
- 15' — uzdevumi
- 5' — ko darīt, ja API mainās

**Uzdevumi**
84. Iegūsti datus no publiskas API un apstrādā tos ar piemērotu datu struktūru.
85. Apstrādā gadījumus: nav interneta, statusa kods nav 200, trūkst lauka.
86. Pieraksti trīs riskus, ko rada svešas bibliotēkas pievienošana.
87. ★ Pieraksti, ko darītu, ja API, uz kuras balstās tavs projekts, rīt pārstātu strādāt.

**Mājasdarbs:** 85. uzdevums

## 12-080 · Savs API galapunkts
`[K]` `prakse` · `teorija.py` §15

**Tēma:** Savas programmsaskarnes izveide.
**SR:** Izveido API galapunktu, kas atbild uz pieprasījumu izvēlētā formātā.
**Standarts:** T.A.2.4.11.

**Gaita**
- 5' — līdz šim tu lietoji svešas API; tagad būsi tas, kurš atbild
- 15' — demo §15: galapunkts, parametri, atbildes struktūra, statusa kodi
- 15' — uzdevumi
- 5' — kas ir laba API atbilde: paredzama struktūra un skaidra kļūda

**Uzdevumi**
88. Izveido galapunktu, kas atgriež datus no tavas 02. bloka datubāzes.
89. Pievieno parametrus filtrēšanai un kārtošanai.
90. Pievieno kļūdu apstrādi ar pareiziem statusa kodiem.
91. Dokumentē savu API: adrese, parametri, atbildes piemērs.
92. ★ Pievieno lappušošanu (`limit` un `offset`) un pamato, kāpēc tā vajadzīga.

**Mājasdarbs:** 91. uzdevums

## 12-081 · API drošība
`[K]` `jaukta` · FV6 (papīrs) · `teorija.py` §16

**Tēma:** API atslēgas un drošība.
**SR:** Skaidro API atslēgas nozīmi un glabā to droši.
**Standarts:** T.A.2.4.11. · T.A.3.1.2.

**Gaita**
- 15' — **FV6** uz papīra, datori aizvērti
- 10' — API atslēga: kas tā ir, ko tā aizsargā, kas notiek, ja tā noplūst
- 10' — pieprasījumu ierobežošana un kāpēc tā ir drošības jautājums
- 5' — kā atslēgas glabā komandas projektā

**Uzdevumi**
93. Pārnes savas API atslēgas uz `.env` un pārbaudi, ka tās nav repozitorijā.
94. Pievieno savai API vienkāršu atslēgas pārbaudi.
95. ★ Pieraksti, kā tu atslēgu nodotu komandas biedram, nenosūtot to čatā.

**Mājasdarbs:** 94. uzdevums

## 12-082 · Mašīnmācīšanās principi
`[K]` `teorija` · `teorija.py` §17

**Tēma:** Mašīnmācīšanās pamatprincipi. Vadītā un nevadītā mācīšanās.
**SR:** Skaidro mašīnmācīšanās principus un atšķir tos no algoritmiskas pieejas.
**Standarts:** T.A.2.4.18. · T.A.3.2.5.

**Gaita**
- 10' — algoritms: mēs uzrakstām likumus. Modelis: mēs dodam piemērus
- 10' — vadītā un nevadītā mācīšanās; apmācības un pārbaudes dati
- 15' — kāpēc ievaddati izšķir visu; pārmācīšanās (overfitting)
- 5' — ētikas jautājumi: neobjektivitāte, atbildība, caurspīdīgums

**Uzdevumi**
96. Burtnīcā: sešiem uzdevumiem atzīmē, kuram der algoritms un kuram — modelis.
97. Burtnīcā: apraksti, kādi dati būtu vajadzīgi vienam no tiem un cik daudz.
98. ★ Pieraksti piemēru, kur modeļa kļūda radītu reālu netaisnību, un kas par to atbild.

**Mājasdarbs:** 97. uzdevums

## 12-083 · Sprints: gatava modeļa lietošana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: gatava mašīnmācīšanās modeļa izmantošana.
**SR:** Lieto gatavu modeli sava uzdevuma risināšanā.
**Standarts:** T.A.2.4.18.

**Uzdevumi**
99. Izmanto gatavu modeli vai bibliotēku, lai klasificētu datus (piemēram, tekstu vai attēlus).
100. Pārbaudi to ar vismaz desmit piemēriem un pieraksti, cik reižu tas kļūdījās.
101. ★ Pieraksti, kāda veida piemēros tas kļūdās biežāk.

**Sprints:** programma un rezultātu tabula

## 12-084 · Sprints: rezultātu izvērtēšana
`[A]` `teorija`

**Tēma:** Modeļa rezultātu izvērtēšana.
**SR:** Izvērtē modeļa precizitāti un tā lietojuma robežas.
**Standarts:** T.A.2.4.18. · T.A.3.2.5.

**Uzdevumi**
102. Aprēķini, cik procentu tavu piemēru modelis klasificēja pareizi.
103. Pieraksti, kādos gadījumos tam nedrīkstētu uzticēties.
104. ★ Pieraksti, kā tu pārbaudītu, vai modelis nav neobjektīvs.

**Sprints:** `modelis.md`

## 12-085 · SV3 uzdevuma izsniegšana
`[K]` `teorija`

**Tēma:** Summatīvā darba specifikācija un plānošana.
**SR:** Izprot darba prasības un izplāno izpildi.
**Standarts:** T.A.2.4.4.

**Gaita**
- 15' — specifikācijas nolasīšana un jautājumi
- 15' — vērtēšanas kritēriji: uzsvars uz struktūras izvēles pamatojumu
- 10' — katrs pieraksta, kuras struktūras lietos un kāpēc

**Uzdevumi**
105. Izlasi SV3 specifikāciju un uzraksti plānu.
106. Pieraksti, kuras datu struktūras lietosi un kāpēc.
107. ★ Novērtē sava plānotā risinājuma sarežģītību pirms koda rakstīšanas.

**Mājasdarbs:** plāns repozitorijā

## 12-086 · SV3 izstrāde
`[K]` `prakse`

**Tēma:** Summatīvā darba izstrāde.
**SR:** Realizē risinājumu atbilstoši specifikācijai.
**Standarts:** T.A.2.4.14. · T.A.2.4.11.

**Gaita**
- 35' — izstrāde, individuālas konsultācijas
- 5' — commit

**Stundas beigās:** datu ieguve un apstrāde strādā.

**Mājasdarbs:** commit ar paveikto

## 12-087 · SV3: pabeigšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvais darbs: datu struktūras, API un mašīnmācīšanās.
**SR:** Pabeidz risinājumu atbilstoši specifikācijai.
**Standarts:** T.A.2.4.14. · T.A.2.4.11. · T.A.2.4.18.

**Gaita**
- 35' — pabeigšana pie datora, bez AI rīkiem
- 5' — iesniegšana

**Materiāli:** SV3 specifikācija (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

## 12-088 · SV3: aizstāvēšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvā darba demonstrācija un aizstāvēšana.
**SR:** Pamato datu struktūru izvēli un novērtē risinājuma sarežģītību.
**Standarts:** komplekss SR

**Gaita**
- 40' — aizstāvēšanās: demonstrācija, jautājumi par struktūru izvēli, izmaiņa uz vietas

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šis ir eksāmena lielākais bloks** — 4. daļa ir 35 % no punktiem, un tur ir tieši datu
  struktūras un programmsaskarnes. Ja kaut kur jāatvēl papildu laiks, tad šeit.
- **Sarežģītību māca ar mērījumiem, ne ar formulām.** 12-058 un 12-059 skolēns pats izmēra,
  ka `insert(0, x)` ir daudz lēnāks, un tikai 12-075 tam parādās apzīmējums O(n). Otrādi
  tas nestrādā — O apzīmējums bez mērījumiem paliek burti.
- **Rekursija 12-069 ir vieta, kur puse klases apstājas.** Bāzes gadījums jāatkārto katrā
  piemērā: «kad funkcija beidz sevi izsaukt?»
- **12-063 līdz 12-070 ir tieši tās struktūras, ko standarts uzskaita:** masīvi, kopas,
  ieraksti, steki, rindas, saraksti, koki, grafi, datnes. Neviena nav izlaista.
- **Mašīnmācīšanās šeit ir lietojums, ne teorija.** Standarts prasa «izmanto gatavu
  algoritmu», ne uzbūvēt savu. 12-084 svarīgākais uzdevums ir izvērtēt, kad modelim
  nedrīkst uzticēties.
