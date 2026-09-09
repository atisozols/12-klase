# 05. Programmatūras izstrāde

**30 stundas (12-107 – 12-136)** · Standarta 5. temats · **SV5 īpatsvars: 20 %**

**Bloka mērķis:** strukturējot programmas kodu, izstrādāt programmatūru pēc savas
specifikācijas, izmantojot izstrādes labās prakses principus un veicot testēšanu.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Darba uzdevums:** tava specifikācija no 04. bloka
**Noslēgums:** SV5 — individuāls programmprodukts (12-135, 12-136)

> Specifikācijai jābūt **apstiprinātai** pēc SV4. Ja tā vēl nav, pirmais sprints paiet, to
> sakārtojot.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 05-izstrade/README.md && python3 bin/darbafails.py 05-izstrade -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 12-107 | Izstrādes vides un repozitorija sagatavošana. | Sagatavo projekta vidi, kurā var sākt izstrādi. |  |
| 12-108 | Projekta struktūras izveide. | Izveido mapju un moduļu struktūru pirms koda rakstīšanas. |  |
| 12-109 | Koda sadalīšana moduļos un slāņos. | Sadala programmu slāņos tā, ka loģika nav atkarīga no saskarnes. |  |
| 12-110 | Koda pieraksta un strukturēšanas labās prakses principi. | Piemēro labās prakses principus un pamato, kāpēc katrs ir vajadzīgs. |  |
| 12-111 | Zari, apvienošana un konflikti. | Strādā ar zariem un atrisina apvienošanas konfliktu. |  |
| 12-112 | Projekta izstrāde: datu slānis. | Realizē datu glabāšanas daļu atbilstoši specifikācijai. |  |
| 12-113 | Patstāvīga izstrāde pēc plāna. | Izpilda plānotos uzdevumus un dokumentē progresu. |  |
| 12-114 | Patstāvīga izstrāde: loģikas slānis. | Realizē galveno programmas loģiku. |  |
| 12-115 | Vienībtesti. Automatizēta funkciju pārbaude. | Uzraksta vienībtestus savām funkcijām un palaiž tos automātiski. | **FV8** (dators) |
| 12-116 | Robežgadījumi un negatīvie testi. | Nosaka funkcijas robežgadījumus un uzraksta testus tiem. |  |
| 12-117 | Projekta izstrāde: saskarnes slānis. | Realizē lietotāja saskarni atbilstoši prototipam. |  |
| 12-118 | Starpposma demonstrācija. | Demonstrē paveikto un koriģē plānu. |  |
| 12-119 | Uzlabojumi pēc atgriezeniskās saites. | Ievieš uzlabojumus un pārbauda tos ar testiem. |  |
| 12-120 | Patstāvīga izstrāde. | Realizē nākamās prasības pēc plāna. |  |
| 12-121 | Sistemātiska atkļūdošana. | Atrod kļūdas cēloni sistemātiski, nevis minot. |  |
| 12-122 | Refaktorēšana. Koda uzlabošana, nemainot uzvedību. | Uzlabo koda struktūru, saglabājot funkcionalitāti un pārbaudot to ar testiem. |  |
| 12-123 | Projekta izstrāde. | Realizē atlikušās obligātās prasības. |  |
| 12-124 | Projekta izstrāde un kļūdu labošana. | Pabeidz obligāto funkcionalitāti. |  |
| 12-125 | Patstāvīga izstrāde. | Pabeidz atlikušos uzdevumus. |  |
| 12-126 | Testu komplekta papildināšana. | Panāk, ka testi aptver visas galvenās funkcijas. |  |
| 12-127 | Integrācijas testēšana. Vienību sadarbība. | Testē vairāku komponenšu sadarbību, ne tikai atsevišķas funkcijas. | **FV9** (dators) |
| 12-128 | Otrā demonstrācija un gatavības izvērtējums. | Demonstrē gandrīz gatavu risinājumu un plāno atlikušo darbu. |  |
| 12-129 | Akcepttestēšana pret specifikāciju. | Pārbauda katru specifikācijas prasību un dokumentē rezultātu. |  |
| 12-130 | Akcepttestēšanā atrasto kļūdu labošana. | Novērš atrastās neatbilstības un atkārtoti pārbauda. |  |
| 12-131 | Patstāvīgs darbs: projekta pabeigšana. | Pabeidz risinājumu un novērš atlikušās kļūdas. |  |
| 12-132 | Projekta dokumentācija. | Uzraksta lietotāja un izstrādātāja dokumentāciju. |  |
| 12-133 | Programmatūras izvēršana un uzturēšana. | Izstrādā izvēršanas un uzturēšanas plānu. |  |
| 12-134 | Darba pašpārbaude pirms iesniegšanas. | Pārbauda darba atbilstību specifikācijai un vērtēšanas kritērijiem. |  |
| 12-135 | Summatīvais darbs: individuāls programmprodukts. | Iesniedz pabeigtu risinājumu ar testiem un dokumentāciju. | **SV5** |
| 12-136 | Summatīvā darba demonstrācija un aizstāvēšana. | Demonstrē risinājumu, pamato izvēles un veic izmaiņu uz vietas. | **SV5** |

<!-- TABULA:BEIGAS -->

---

## 12-107 · Sprints: vides sagatavošana
`[A]` `prakse`

**Tēma:** Izstrādes vides un repozitorija sagatavošana.
**SR:** Sagatavo projekta vidi, kurā var sākt izstrādi.
**Standarts:** T.A.2.4.9.

**Uzdevumi**
1. Izveido projekta repozitoriju ar `README.md`, `.gitignore` un `SPECIFIKACIJA.md`.
2. Izveido virtuālo vidi un `requirements.txt`.
3. Pārnes savus uzdevumus no plāna uz GitHub Projects dēli.
4. ★ Pievieno `Makefile` vai skriptu, kas palaiž projektu ar vienu komandu.

**Sprints:** gatavs repozitorijs ar pirmo commit

## 12-108 · Sprints: projekta skelets
`[A]` `prakse`

**Tēma:** Projekta struktūras izveide.
**SR:** Izveido mapju un moduļu struktūru pirms koda rakstīšanas.
**Standarts:** T.A.2.4.8.

**Uzdevumi**
5. Izveido mapju struktūru: dati, loģika, saskarne, testi.
6. Katrā modulī izveido tukšas funkcijas ar aprakstiem — bez realizācijas.
7. Pārbaudi, ka viss importējas bez kļūdām.
8. ★ Uzzīmē moduļu atkarību shēmu un pieraksti, kurš modulis no kura ir atkarīgs.

**Sprints:** projekta skelets repozitorijā

## 12-109 · Koda strukturēšana
`[K]` `prakse` · `teorija.py` §1

**Tēma:** Koda sadalīšana moduļos un slāņos.
**SR:** Sadala programmu slāņos tā, ka loģika nav atkarīga no saskarnes.
**Standarts:** T.A.2.4.8.

**Gaita**
- 10' — trīs slāņi: dati, loģika, saskarne; kāpēc atkarībai jāiet vienā virzienā
- 10' — demo §1: viens fails pret trim moduļiem
- 15' — uzdevumi
- 5' — pārbaude: vai loģiku var notestēt bez saskarnes?

**Uzdevumi**
9. Sadali savu projektu trīs slāņos un pieraksti, kas kurā ietilpst.
10. Pārbaudi, ka loģikas modulis neimportē neko no saskarnes.
11. Pārraksti vienu funkciju, kurā ir sajaukta loģika un izvade.
12. ★ Atrodi savā kodā apļveida atkarību vai pierādi, ka tādas nav.

**Mājasdarbs:** 10. uzdevums

## 12-110 · Labās prakses principi
`[K]` `jaukta` · `teorija.py` §2

**Tēma:** Koda pieraksta un strukturēšanas labās prakses principi.
**SR:** Piemēro labās prakses principus un pamato, kāpēc katrs ir vajadzīgs.
**Standarts:** T.A.2.4.8.

**Gaita**
- 10' — seši principi no eksāmena programmas un kā tos vērtē
- 10' — nosaukumi, funkciju garums, komentāri, kas skaidro «kāpēc»
- 15' — uzdevumi: pārraksta doto kodu
- 5' — kāpēc tas ir 3 % no eksāmena, bet 100 % no tā, vai pats saprastu pēc mēneša

**Uzdevumi**
13. Pārraksti doto koda fragmentu, ievērojot visus sešus principus.
14. Atrodi savā kodā funkciju, kas garāka par 30 rindām, un sadali to.
15. Atrodi komentāru, kas atkārto kodu, un pārraksti to par tādu, kas skaidro iemeslu.
16. ★ Pieraksti savam projektam koda stila vienošanos vienā lapā.

**Mājasdarbs:** 14. uzdevums

## 12-111 · Versiju pārvaldība
`[K]` `prakse` · `teorija.py` §3

**Tēma:** Zari, apvienošana un konflikti.
**SR:** Strādā ar zariem un atrisina apvienošanas konfliktu.
**Standarts:** T.A.2.4.9.

**Gaita**
- 10' — kāpēc zari: nepabeigts darbs neaizķer galveno versiju
- 10' — demo §3: `branch`, `merge`, konflikts un tā atrisināšana
- 15' — uzdevumi
- 5' — labs commit apraksts: ko un kāpēc, ne «update»

**Uzdevumi**
17. Izveido zaru, izdari izmaiņas, apvieno to ar galveno.
18. Ar nodomu izraisi konfliktu un atrisini to.
19. Apskati savu vēsturi ar `git log --oneline --graph` un pieraksti, ko redzi.
20. Pārraksti savus pēdējos piecus commit aprakstus tā, kā tie būtu jāraksta.
21. ★ Uzzini, ko dara `git revert`, un pieraksti, ar ko tas atšķiras no `git reset`.

**Mājasdarbs:** 20. uzdevums

## 12-112 · Izstrāde
`[K]` `prakse`

**Tēma:** Projekta izstrāde: datu slānis.
**SR:** Realizē datu glabāšanas daļu atbilstoši specifikācijai.
**Standarts:** T.A.2.4.13.

**Gaita**
- 35' — izstrāde, individuālas konsultācijas
- 5' — commit

**Stundas beigās:** datubāze vai datņu struktūra izveidota, dati saglabājas un nolasās.

**Mājasdarbs:** commit ar paveikto

## 12-113 · Sprints: izstrāde
`[A]` `prakse`

**Tēma:** Patstāvīga izstrāde pēc plāna.
**SR:** Izpilda plānotos uzdevumus un dokumentē progresu.
**Standarts:** T.A.2.4.13.

**Uzdevumi**
22. Izpildi nākamos uzdevumus no sava dēļa.
23. Pieraksti, kur iestrēgi, lai nākamajā klātienes stundā to atrisinātu ātri.
24. ★ Ja esi priekšā plānam, paņem uzdevumu no saraksta «vēlams».

**Sprints:** commit un atjaunināts dēlis

## 12-114 · Sprints: izstrāde
`[A]` `prakse`

**Tēma:** Patstāvīga izstrāde: loģikas slānis.
**SR:** Realizē galveno programmas loģiku.
**Standarts:** T.A.2.4.13.

**Uzdevumi**
25. Realizē vismaz divas specifikācijas funkcionālās prasības.
26. Pārbaudi katru ar vismaz trim ievades gadījumiem.
27. ★ Pieraksti, kura prasība izrādījās sarežģītāka, nekā izskatījās.

**Sprints:** commit ar strādājošu loģiku

## 12-115 · Vienībtestēšana
`[K]` `prakse` · FV8 (dators) · `teorija.py` §4

**Tēma:** Vienībtesti. Automatizēta funkciju pārbaude.
**SR:** Uzraksta vienībtestus savām funkcijām un palaiž tos automātiski.
**Standarts:** T.A.2.4.6.

**Gaita**
- 10' — kāpēc automātisks tests ir labāks par `print`
- 10' — demo §4: `unittest`, `assert`, testu palaišana
- 15' — **FV8** pie datora
- 5' — testu nosaukumi: tests ir dokumentācija par to, kā funkcija strādā

**Uzdevumi**
28. Uzraksti vienībtestus vismaz trim savām funkcijām.
29. Katrai iekļauj pareizu ievadi, nepareizu ievadi un robežgadījumu.
30. Palaid visus testus ar vienu komandu.
31. Ar nodomu salauz vienu funkciju un pārbaudi, ka tests to pamana.
32. ★ Pievieno testu, kas pārbauda, ka funkcija met izņēmumu, kad vajag.

**Mājasdarbs:** 28. uzdevums

## 12-116 · Robežgadījumi
`[K]` `prakse` · `teorija.py` §5

**Tēma:** Robežgadījumi un negatīvie testi.
**SR:** Nosaka funkcijas robežgadījumus un uzraksta testus tiem.
**Standarts:** T.A.2.4.6.

**Gaita**
- 10' — kur rodas kļūdas: robežas, tukšums, nulle, negatīvs, pārāk daudz
- 10' — ekvivalences klases: kāpēc nav jātestē visi 1000 gadījumi
- 15' — uzdevumi
- 5' — kļūda, kas atrasta testā, maksā daudz mazāk nekā kļūda, ko atrod lietotājs

**Uzdevumi**
33. Katrai savai funkcijai uzskaiti robežgadījumus.
34. Uzraksti testus vismaz pieciem no tiem.
35. Pārbaudi, kas notiek ar tukšu ievadi visur, kur tas iespējams.
36. ★ Atrodi savā programmā vietu, kas avarē pie kāda robežgadījuma, un salabo.

**Mājasdarbs:** 34. uzdevums

## 12-117 · Izstrāde
`[K]` `prakse`

**Tēma:** Projekta izstrāde: saskarnes slānis.
**SR:** Realizē lietotāja saskarni atbilstoši prototipam.
**Standarts:** T.A.2.4.13.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** lietotājs var veikt vismaz vienu pilnu darbību no sākuma līdz beigām.

**Mājasdarbs:** commit ar paveikto

## 12-118 · Pirmais starpposms
`[K]` `jaukta`

**Tēma:** Starpposma demonstrācija.
**SR:** Demonstrē paveikto un koriģē plānu.
**Standarts:** T.A.2.4.3.

**Gaita**
- 20' — katrs 3 minūtēs parāda, kas strādā un kas vēl nē
- 15' — atgriezeniskā saite un tehniski ieteikumi
- 5' — plāna korekcija

**Uzdevumi**
37. Demonstrē projektu un pieraksti saņemtās piezīmes.
38. Salīdzini paveikto ar plānu: vai esi grafikā?
39. Ja neesi, izlem, ko izmetīsi, un pieraksti to specifikācijā.
40. ★ Sniedz vienam klasesbiedram konkrētu tehnisku ieteikumu.

**Mājasdarbs:** atjaunināts plāns

## 12-119 · Sprints: uzlabojumi
`[A]` `prakse`

**Tēma:** Uzlabojumi pēc atgriezeniskās saites.
**SR:** Ievieš uzlabojumus un pārbauda tos ar testiem.
**Standarts:** T.A.2.4.6.

**Uzdevumi**
41. Ievies vismaz divus uzlabojumus no piezīmēm.
42. Pārbaudi, ka esošie testi joprojām iet cauri.
43. ★ Pievieno testu tam, ko tikko izlaboji.

**Sprints:** commit ar uzlabojumiem

## 12-120 · Sprints: izstrāde
`[A]` `prakse`

**Tēma:** Patstāvīga izstrāde.
**SR:** Realizē nākamās prasības pēc plāna.
**Standarts:** T.A.2.4.13.

**Uzdevumi**
44. Izpildi nākamos uzdevumus.
45. Atjaunini uzdevumu dēli un pieraksti progresu.
46. ★ Pārbaudi, vai kāds uzdevums «Procesā» stāv ilgāk par nedēļu, un izlem, ko ar to darīt.

**Sprints:** commit un dēlis

## 12-121 · Atkļūdošana
`[K]` `prakse` · `teorija.py` §6

**Tēma:** Sistemātiska atkļūdošana.
**SR:** Atrod kļūdas cēloni sistemātiski, nevis minot.
**Standarts:** T.A.2.4.6.

**Gaita**
- 10' — atkļūdošana kā izmeklēšana: hipotēze, pārbaude, secinājums
- 10' — demo §6: atkļūdotājs, pārtraukumpunkti, žurnalēšana
- 15' — uzdevumi ar dotām kļūdainām programmām
- 5' — kad apstāties un pajautāt

**Uzdevumi**
47. Atrodi kļūdu dotajā programmā, izmantojot atkļūdotāju, un pieraksti soļus.
48. Pievieno savai programmai žurnalēšanu vietās, kur kaut kas var noiet greizi.
49. Uzraksti savu atkļūdošanas gaitu vienai reālai kļūdai: hipotēze, pārbaude, rezultāts.
50. ★ Atrodi kļūdu, kas parādās tikai konkrētā datu kombinācijā, un uzraksti tai testu.

**Mājasdarbs:** 49. uzdevums

## 12-122 · Refaktorēšana
`[K]` `prakse` · `teorija.py` §7

**Tēma:** Refaktorēšana. Koda uzlabošana, nemainot uzvedību.
**SR:** Uzlabo koda struktūru, saglabājot funkcionalitāti un pārbaudot to ar testiem.
**Standarts:** T.A.2.4.8.

**Gaita**
- 10' — kas ir refaktorēšana un kāpēc bez testiem to nedara
- 10' — biežākie paņēmieni: funkcijas izdalīšana, atkārtojuma novēršana, nosaukumu maiņa
- 15' — uzdevumi
- 5' — kad refaktorēt un kad atstāt mierā

**Uzdevumi**
51. Atrodi savā kodā atkārtojumu un izdali to funkcijā.
52. Pēc katras izmaiņas palaid testus un pārbaudi, ka nekas nav salūzis.
53. Pārsauc trīs neskaidrus nosaukumus.
54. ★ Atrodi funkciju, kas dara divas lietas, un sadali to divās.

**Mājasdarbs:** 51. uzdevums

## 12-123 · Izstrāde
`[K]` `prakse`

**Tēma:** Projekta izstrāde.
**SR:** Realizē atlikušās obligātās prasības.
**Standarts:** T.A.2.4.13.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** vismaz 70 % obligāto prasību ir izpildītas.

**Mājasdarbs:** commit ar paveikto

## 12-124 · Izstrāde
`[K]` `prakse`

**Tēma:** Projekta izstrāde un kļūdu labošana.
**SR:** Pabeidz obligāto funkcionalitāti.
**Standarts:** T.A.2.4.13.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** visas obligātās prasības strādā vismaz pamata līmenī.

**Mājasdarbs:** commit ar paveikto

## 12-125 · Sprints: izstrāde
`[A]` `prakse`

**Tēma:** Patstāvīga izstrāde.
**SR:** Pabeidz atlikušos uzdevumus.
**Standarts:** T.A.2.4.13.

**Uzdevumi**
55. Izpildi atlikušos obligātos uzdevumus.
56. Papildini testus jaunajām funkcijām.
57. ★ Pievieno vienu prasību no saraksta «vēlams», ja laiks atļauj.

**Sprints:** commit

## 12-126 · Sprints: testu papildināšana
`[A]` `prakse`

**Tēma:** Testu komplekta papildināšana.
**SR:** Panāk, ka testi aptver visas galvenās funkcijas.
**Standarts:** T.A.2.4.6.

**Uzdevumi**
58. Pārbaudi, kurām funkcijām vēl nav testu, un uzraksti tos.
59. Palaid visu komplektu un pieraksti rezultātu.
60. ★ Noskaidro, kas ir koda pārklājums (coverage), un izmēri savu.

**Sprints:** testu komplekts un rezultāts

## 12-127 · Integrācijas testēšana
`[K]` `prakse` · FV9 (dators) · `teorija.py` §8

**Tēma:** Integrācijas testēšana. Vienību sadarbība.
**SR:** Testē vairāku komponenšu sadarbību, ne tikai atsevišķas funkcijas.
**Standarts:** T.A.2.4.6.

**Gaita**
- 10' — katra funkcija strādā, bet kopā nestrādā: kāpēc
- 10' — demo §8: integrācijas tests, testa dati, sagatavošana un sakopšana
- 15' — **FV9** pie datora
- 5' — testu piramīda: daudz vienībtestu, mazāk integrācijas testu

**Uzdevumi**
61. Uzraksti integrācijas testu, kas pārbauda pilnu ceļu: ievade, apstrāde, saglabāšana.
62. Uzraksti testu, kas pārbauda, ka dati pēc restartēšanas ir vietā.
63. ★ Uzraksti testu, kas izmanto atsevišķu testa datubāzi, lai nesabojātu īsto.

**Mājasdarbs:** 61. uzdevums

## 12-128 · Otrais starpposms
`[K]` `jaukta`

**Tēma:** Otrā demonstrācija un gatavības izvērtējums.
**SR:** Demonstrē gandrīz gatavu risinājumu un plāno atlikušo darbu.
**Standarts:** T.A.2.4.3.

**Gaita**
- 20' — demonstrācijas ar uzsvaru uz lietojamību
- 15' — savstarpēja testēšana: katrs izmēģina divus citu projektus
- 5' — atlikušo astoņu stundu plāns

**Uzdevumi**
64. Demonstrē projektu un pieraksti piezīmes.
65. Notestē divus citu projektus un uzraksti kļūdas ziņojumus.
66. Uzraksti, kas obligāti jāpaspēj atlikušajās stundās.
67. ★ Iedod projektu cilvēkam, kas to nav redzējis, un vēro, kur viņš apstājas.

**Mājasdarbs:** atjaunināts plāns

## 12-129 · Akcepttestēšana
`[K]` `prakse` · `teorija.py` §9

**Tēma:** Akcepttestēšana pret specifikāciju.
**SR:** Pārbauda katru specifikācijas prasību un dokumentē rezultātu.
**Standarts:** T.A.2.4.6.

**Gaita**
- 10' — akcepttests atbild uz vienu jautājumu: vai prasība ir izpildīta?
- 10' — testa plāna tabula: prasība, soļi, sagaidāmais, faktiskais
- 15' — uzdevumi
- 5' — godīga tabula ir vērtīgāka par skaistu

**Uzdevumi**
68. Izveido akcepttestu plānu: pa vienam testam katrai funkcionālajai prasībai.
69. Izpildi to un aizpildi faktisko rezultātu kolonnu.
70. Pieraksti, kuras prasības nav izpildītas un kāpēc.
71. ★ Pievieno testus arī nefunkcionālajām prasībām, kur tas iespējams.

**Mājasdarbs:** pabeigt `TESTI.md`

## 12-130 · Izstrāde un labošana
`[K]` `prakse`

**Tēma:** Akcepttestēšanā atrasto kļūdu labošana.
**SR:** Novērš atrastās neatbilstības un atkārtoti pārbauda.
**Standarts:** T.A.2.4.6.

**Gaita**
- 35' — labošana; pēc katras izmaiņas testi jāpalaiž vēlreiz
- 5' — `TESTI.md` atjaunināšana

**Mājasdarbs:** commit ar labojumiem

## 12-131 · Sprints: pabeigšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: projekta pabeigšana.
**SR:** Pabeidz risinājumu un novērš atlikušās kļūdas.
**Standarts:** T.A.2.4.13.

**Uzdevumi**
72. Izlabo atlikušās kļūdas no testēšanas.
73. Pārbaudi, ka visi testi iet cauri.
74. ★ Pārskati savu kodu ar svaigu skatu un atrodi vienu vietu, ko uzlabot.

**Sprints:** commit

## 12-132 · Sprints: dokumentācija
`[A]` `prakse`

**Tēma:** Projekta dokumentācija.
**SR:** Uzraksta lietotāja un izstrādātāja dokumentāciju.
**Standarts:** T.A.2.4.7.

**Uzdevumi**
75. Uzraksti `README.md`: apraksts, ekrānuzņēmums, palaišanas instrukcija.
76. Uzraksti lietotāja ceļvedi ar galvenajām darbībām.
77. ★ Uzraksti izstrādātāja piezīmes: kā projekts sakārtots un kur ko meklēt.

**Sprints:** dokumentācija repozitorijā

## 12-133 · Uzturēšanas plāns
`[K]` `jaukta` · `teorija.py` §10

**Tēma:** Programmatūras izvēršana un uzturēšana.
**SR:** Izstrādā izvēršanas un uzturēšanas plānu.
**Standarts:** T.A.2.4.7.

**Gaita**
- 10' — kas notiek pēc tam, kad programma ir gatava
- 10' — izvēršanas plāns: kā to uzstāda no nulles
- 15' — uzdevumi
- 5' — rezerves kopijas un atjauninājumi

**Uzdevumi**
78. Uzraksti izvēršanas plānu: soļi, lai programmu palaistu citā datorā no nulles.
79. Uzraksti uzturēšanas plānu: kas jādara reizi mēnesī, kas — reizi gadā.
80. Pieraksti, kas notiktu, ja tev projekts būtu jānodod citam cilvēkam rīt.
81. ★ Pārbaudi savu izvēršanas plānu uz cita datora vai tīras vides.

**Mājasdarbs:** 78. uzdevums

## 12-134 · Pašpārbaude
`[K]` `prakse`

**Tēma:** Darba pašpārbaude pirms iesniegšanas.
**SR:** Pārbauda darba atbilstību specifikācijai un vērtēšanas kritērijiem.
**Standarts:** T.A.2.4.6.

**Gaita**
- 25' — pašpārbaudes tabulas aizpildīšana
- 10' — pēdējie labojumi
- 5' — commit

**Uzdevumi**
82. Aizpildi pašpārbaudes tabulu pret katru prasību un norādi vietu kodā.
83. Pārbaudi commit vēsturi: vai no tās var saprast, kā projekts auga?
84. ★ Pārbaudi, ka projekts palaižas tīrā vidē pēc tavas instrukcijas.

**Mājasdarbs:** `PASPARBAUDE.md`

## 12-135 · SV5: iesniegšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvais darbs: individuāls programmprodukts.
**SR:** Iesniedz pabeigtu risinājumu ar testiem un dokumentāciju.
**Standarts:** T.A.2.4.13. · T.A.2.4.6.

**Gaita**
- 35' — pēdējie labojumi pie datora, bez AI rīkiem
- 5' — iesniegšana

**Mājasdarbs:** —

## 12-136 · SV5: aizstāvēšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvā darba demonstrācija un aizstāvēšana.
**SR:** Demonstrē risinājumu, pamato izvēles un veic izmaiņu uz vietas.
**Standarts:** komplekss SR

**Gaita**
- 40' — aizstāvēšanās: demonstrācija, jautājumi par kodu un testiem, izmaiņa uz vietas

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šis bloks ir 20 % no gada vērtējuma un otrs lielākais pēc apjoma.** Tā serde ir nevis
  jauna viela, bet disciplīna: katrai stundai ir «stundas beigās», katram sprintam —
  nododams rezultāts.
- **Testi šeit nav papildinājums.** 12-115, 12-116, 12-127 un 12-129 sedz visus četrus
  testēšanas veidus, ko prasa standarts: vienību, integrācijas, akcept- un atkļūdošanu.
  Bez testiem 12-122 refaktorēšana nav iespējama — to skolēnam saka tieši.
- **Divi starpposmi ir obligāti.** 12-118 un 12-128. Tur atklājas, kurš ir iestrēdzis, un
  tur vēl var samazināt apjomu, izmantojot 04. blokā uzrakstīto sarakstu «ko izmetīšu».
- **Ja specifikācija nav apstiprināta, izstrādi nesāk.** Pirmais sprints paiet, to sakārtojot.
  Tas ir lētāk nekā desmit stundas nepareizā virzienā.
