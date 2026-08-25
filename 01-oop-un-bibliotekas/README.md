# 01. Objektorientētā programmēšana un ārējās bibliotēkas

**28 stundas (12-001 – 12-028)** · Standarta 1. temats · **SV1 īpatsvars: 15 %**

**Bloka mērķis:** izmantojot objektorientētas programmēšanas valodas pamatprincipus un
bibliotēkas, izstrādāt konkrētu programmatūras risinājumu ar grafisko lietotāja saskarni.

**Teorija un piemēri:** [`teorija.py`](teorija.py) · **Darba fails:** [`uzdevumi.py`](uzdevumi.py)
**Noslēgums:** SV1 — programmprodukts (12-027, 12-028)

**Eksāmenā:** 3. daļa, 31 % no punktiem.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 01-oop-un-bibliotekas/README.md && python3 bin/darbafails.py 01-oop-un-bibliotekas -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 12-001 | Kursa uzbūve un eksāmens. Objektorientētās programmēšanas atkārtojums. | Nosauc kursa prasības un eksāmena daļas; atkārto klases un objekta jēdzienus. |
| 12-002 | Klases uzbūve. Konstruktors un objekta izveide. | Definē klasi ar konstruktoru un izveido objektus ar dažādām sākuma vērtībām. |
| 12-003 | Vairāki objekta izveides veidi. Noklusējuma vērtības un klases metodes. | Izveido klasei vairākus objekta izveides veidus un pamato, kad kurš ir piemērots. |
| 12-004 | Iekapsulēšana. Iekšējie atribūti un piekļuves metodes. | Skaidro iekapsulēšanu un realizē to, izmantojot iekšējos atribūtus un `property`. |
| 12-005 | Patstāvīgs darbs: klase ar pilnu validāciju. | Patstāvīgi izstrādā klasi, kas neļauj izveidot nederīgu objektu. |
| 12-006 | Sprinta rezultātu izvērtēšana. | Izvērtē savu risinājumu un pieraksta, kas bija grūtākais. |
| 12-007 | Mantošana. Virsklase un apakšklase. | Veido klašu hierarhiju un lieto `super()`. |
| 12-008 | Polimorfisms. Viena saskarne, dažādas realizācijas. | Skaidro polimorfismu un izmanto to, lai apstrādātu dažādu klašu objektus vienādi. |
| 12-009 | Abstrakcija. Kopīgā saskarne un abstraktās metodes. | Definē abstraktu virsklasi, kas nosaka, kas apakšklasēm obligāti jārealizē. |
| 12-010 | Praktikums: abstrakcija, iekapsulēšana, mantošana, polimorfisms. | Izmanto visus četrus OOP pamatprincipus vienā risinājumā. |
| 12-011 | Patstāvīgs darbs: klašu hierarhijas projektēšana. | Projektē un realizē klašu hierarhiju dotam uzdevuma aprakstam. |
| 12-012 | Cita koda pārskatīšana. | Izvērtē cita risinājumu pēc OOP principiem un sniedz konkrētu atgriezenisko saiti. |
| 12-013 | Standarta bibliotēkas iespējas. Dokumentācijas lasīšana. | Atrod dokumentācijā vajadzīgo standarta bibliotēkas iespēju un lieto to. |
| 12-014 | Ārējo bibliotēku meklēšana, izvērtēšana un pievienošana. | Izvēlas uzdevumam piemērotu ārējo bibliotēku un pamato izvēli. |
| 12-015 | Grafiskā lietotāja saskarne. Logs, elementi, izkārtojums. | Izveido logu ar ievades laukiem un pogām. |
| 12-016 | Notikumu apstrāde. Poga izsauc funkciju. | Sasaista saskarnes elementus ar programmas loģiku. |
| 12-017 | Patstāvīgs darbs: grafiskā saskarne virs savas klases. | Savieno objektorientētu loģiku ar grafisko saskarni. |
| 12-018 | Sava risinājuma uzlabošana. | Atrod savā risinājumā vietas, kur loģika un saskarne ir sajauktas, un atdala tās. |
| 12-019 | Objektu saglabāšana un ielasīšana. CSV un JSON. | Saglabā objektus datnē un atjauno tos no tās. |
| 12-020 | Izņēmumu apstrāde un savi izņēmumu tipi. | Apstrādā izņēmumus un definē savu izņēmuma klasi. |
| 12-021 | OOP jēdzieni. Gatavošanās eksāmena 3. daļai. | Skaidro un atšķir četrus OOP pamatprincipus. |
| 12-022 | Summatīvā darba specifikācija un vērtēšanas kritēriji. | Izprot darba prasības un izplāno tā izpildi. |
| 12-023 | Summatīvā darba izstrāde: klašu modelis. | Realizē risinājuma klašu daļu atbilstoši specifikācijai. |
| 12-024 | Summatīvā darba izstrāde: saskarne un bibliotēka. | Pievieno grafisko saskarni un ārējās bibliotēkas funkcionalitāti. |
| 12-025 | Patstāvīgs darbs pie summatīvā darba. | Turpina izstrādi patstāvīgi. |
| 12-026 | Datu saglabāšana un atbilstības pārbaude. | Pabeidz saglabāšanas daļu un pārbauda darbu pret specifikāciju. |
| 12-027 | Summatīvais darbs: programmprodukta pabeigšana. | Pabeidz programmproduktu atbilstoši specifikācijai. |
| 12-028 | Summatīvā darba demonstrācija un aizstāvēšana. | Demonstrē risinājumu, pamato izvēles un veic izmaiņu uz vietas. |

<!-- TABULA:BEIGAS -->

---

## 12-001 · Kursa ievads un OOP atkārtojums
`[K]` `teorija` · `teorija.py` §1

**Tēma:** Kursa uzbūve un eksāmens. Objektorientētās programmēšanas atkārtojums.
**SR:** Nosauc kursa prasības un eksāmena daļas; atkārto klases un objekta jēdzienus.
**Standarts:** T.A.2.4.15.

**Gaita**
- 15' — kursa uzbūve, seši summatīvie darbi, īpatsvari, eksāmena uzbūve
- 10' — nedēļas ritms: 4 klātienē, 2 attālināti ar nododamo rezultātu
- 15' — kas palicis atmiņā no 11. klases: klase, objekts, konstruktors uz tāfeles

**Uzdevumi**
1. Izlasi [`kurss/eksamens.md`](../kurss/eksamens.md) un pieraksti, kura eksāmena daļa tev
   šķiet grūtākā un kāpēc.
2. Uzraksti klasi `Prece` ar konstruktoru un divām metodēm — bez ieskatīšanās vecajā kodā.
3. ★ Pieraksti, ko tu no 11. klases OOP nesaproti līdz galam. To risināsim šajā blokā.

**Sprints (nedēļas beigās):** repozitorijs izveidots, 2. uzdevums tajā

## 12-002 · Klase, objekts, konstruktors
`[K]` `prakse` · `teorija.py` §2

**Tēma:** Klases uzbūve. Konstruktors un objekta izveide.
**SR:** Definē klasi ar konstruktoru un izveido objektus ar dažādām sākuma vērtībām.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — atkārtojums: `__init__` un `self`
- 10' — demo §2: atribūti, metodes, objekta dzīves cikls
- 20' — uzdevumi
- 5' — kur klase sākas un kur beidzas atbildība

**Uzdevumi**
4. Izveido klasi `Rezervacija` ar konstruktoru (`vards`, `datums`, `vietu_skaits`) un metodi
   `apraksts()`.
5. Izveido trīs objektus un izvadi to aprakstus.
6. Pievieno metodi `mainit_vietas(jauns_skaits)`, kas neļauj skaitu padarīt negatīvu.
7. ★ Pievieno metodi, kas atgriež `True`, ja rezervācija ir šodienai.

**Mājasdarbs:** 6. uzdevums

## 12-003 · Vairāki konstruktori
`[K]` `prakse` · `teorija.py` §3

**Tēma:** Vairāki objekta izveides veidi. Noklusējuma vērtības un klases metodes.
**SR:** Izveido klasei vairākus objekta izveides veidus un pamato, kad kurš ir piemērots.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — Python nav vairāku konstruktoru, kā C# vai Java. Kā tad?
- 15' — demo §3: noklusējuma vērtības, `@classmethod` kā alternatīvs konstruktors
- 20' — uzdevumi

**Uzdevumi**
8. Pievieno `Rezervacija` konstruktoram noklusējuma vērtību vietu skaitam.
9. Izveido `@classmethod` `no_rindas(rinda)`, kas izveido objektu no CSV rindas.
10. Izveido `@classmethod` `tuksa()`, kas izveido objektu ar noklusējuma vērtībām.
11. Pārbaudi visus trīs izveides veidus vienā programmā.
12. ★ Pieraksti, ar ko šī pieeja atšķiras no vairākiem konstruktoriem C# valodā. _Norāde:
    eksāmenā var būt jautājums par konstruktoriem vispārīgi, ne tikai Python._

**Mājasdarbs:** 9. uzdevums

## 12-004 · Iekapsulēšana
`[K]` `prakse` · `teorija.py` §4

**Tēma:** Iekapsulēšana. Iekšējie atribūti un piekļuves metodes.
**SR:** Skaidro iekapsulēšanu un realizē to, izmantojot iekšējos atribūtus un `property`.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — kāpēc `k._atlikums = 1000000` nedrīkst strādāt
- 15' — demo §4: `_` vienošanās, `property`, `setter` ar validāciju
- 20' — uzdevumi

**Uzdevumi**
13. Pārraksti klasi `Konts` tā, lai atlikumu var lasīt, bet ne tieši mainīt.
14. Pievieno `property` un `setter`, kas neļauj negatīvu vērtību.
15. Pārbaudi, kas notiek, mēģinot piešķirt nederīgu vērtību.
16. ★ Uzraksti klasi, kurā viens atribūts tiek aprēķināts no citiem un tāpēc ir tikai lasāms.

**Mājasdarbs:** 14. uzdevums

## 12-005 · Sprints: klase ar validāciju
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: klase ar pilnu validāciju.
**SR:** Patstāvīgi izstrādā klasi, kas neļauj izveidot nederīgu objektu.
**Standarts:** T.A.2.4.15.

**Nedēļas sprinta uzdevums.** Rezultāts jāieliek repozitorijā līdz nākamajai klātienes stundai.

**Uzdevumi**
17. Izstrādā klasi `Lidojums` ar atribūtiem `numurs`, `galamerkis`, `vietu_skaits`,
    `rezervetas_vietas`. Visai validācijai jābūt klasē: numurs nedrīkst būt tukšs, vietu
    skaitam jābūt pozitīvam, rezervēto vietu skaits nedrīkst pārsniegt kopējo.
18. Pievieno metodes `rezervet(skaits)`, `atcelt(skaits)` un `brivas_vietas()`.
19. Uzraksti vismaz sešus pārbaudes gadījumus, tostarp trīs nederīgus, un pieraksti
    rezultātus komentārā.
20. ★ Pievieno `property`, kas atgriež aizpildījumu procentos.

**Sprints:** `lidojums.py` ar klasi un pārbaudēm

## 12-006 · Sprints: refleksija
`[A]` `teorija`

**Tēma:** Sprinta rezultātu izvērtēšana.
**SR:** Izvērtē savu risinājumu un pieraksta, kas bija grūtākais.
**Standarts:** T.A.2.4.15.

**Uzdevumi**
21. Pieraksti `piezimes.md`, kura validācija bija visgrūtākā un kāpēc.
22. Salīdzini savu risinājumu ar klasesbiedra risinājumu repozitorijā un pieraksti vienu
    lietu, ko viņš izdarīja labāk.
23. ★ Pārraksti vienu savas klases metodi tā, lai tā būtu īsāka vai skaidrāka.

**Sprints:** `piezimes.md`

## 12-007 · Mantošana
`[K]` `prakse` · `teorija.py` §5

**Tēma:** Mantošana. Virsklase un apakšklase.
**SR:** Veido klašu hierarhiju un lieto `super()`.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — kad mantošana ir pareizā atbilde un kad nav
- 15' — demo §5: `super().__init__()`, metožu pārrakstīšana
- 20' — uzdevumi

**Uzdevumi**
24. Izveido virsklasi `Transportlidzeklis` un apakšklases `Automasina` un `Velosipeds`.
25. Katrai apakšklasei pievieno savu metodi un pārrakstītu virsklases metodi.
26. Izveido objektu sarakstu ar dažādu apakšklašu objektiem un apstaigā to ar ciklu.
27. ★ Izveido trīs līmeņu hierarhiju un pieraksti, kāpēc tā parasti ir slikta ideja.

**Mājasdarbs:** 26. uzdevums

## 12-008 · Polimorfisms
`[K]` `prakse` · `teorija.py` §6

**Tēma:** Polimorfisms. Viena saskarne, dažādas realizācijas.
**SR:** Skaidro polimorfismu un izmanto to, lai apstrādātu dažādu klašu objektus vienādi.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — cikls, kas strādā ar objektiem, nezinot to tipu
- 15' — demo §6: metožu pārrakstīšana, `isinstance`, duck typing
- 20' — uzdevumi

**Uzdevumi**
28. Izveido klases `Kvadrats`, `Rinkis`, `Trijsturis`, katrai ar metodi `laukums()`.
29. Uzraksti funkciju, kas saņem figūru sarakstu un atgriež kopējo laukumu.
30. Papildini programmu ar jaunu figūru, nemainot funkciju.
31. Pieraksti, kāpēc 30. uzdevumā funkcija nebija jāmaina — tā ir polimorfisma jēga.
32. ★ Uzraksti funkciju, kas darbojas ar jebkuru objektu, kuram ir metode `apraksts()`,
    neatkarīgi no klases.

**Mājasdarbs:** 29. uzdevums

## 12-009 · Abstrakcija
`[K]` `prakse` · `teorija.py` §7

**Tēma:** Abstrakcija. Kopīgā saskarne un abstraktās metodes.
**SR:** Definē abstraktu virsklasi, kas nosaka, kas apakšklasēm obligāti jārealizē.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — ko nozīmē «figūra» pati par sevi? Laukumu aprēķināt nevar
- 15' — demo §7: `ABC`, `@abstractmethod`
- 20' — uzdevumi

**Uzdevumi**
33. Pārveido `Figura` par abstraktu klasi ar abstraktu metodi `laukums()`.
34. Pārbaudi, kas notiek, mēģinot izveidot abstraktās klases objektu.
35. Pārbaudi, kas notiek, ja apakšklase abstrakto metodi nerealizē.
36. ★ Pieraksti, ar ko abstrakcija atšķiras no iekapsulēšanas. Eksāmenā šie jēdzieni ir
    jāatšķir.

**Mājasdarbs:** 33. uzdevums

## 12-010 · Praktikums: četri principi
`[K]` `prakse` · FV1 (dators)

**Tēma:** Praktikums: abstrakcija, iekapsulēšana, mantošana, polimorfisms.
**SR:** Izmanto visus četrus OOP pamatprincipus vienā risinājumā.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — uzdevuma nolasīšana
- 20' — patstāvīgs darbs
- 15' — **FV1** pie datora

**Uzdevumi**
37. Izstrādā bibliotēkas sistēmas klases: abstrakta `Vienums` ar apakšklasēm `Gramata`,
    `Zurnals`, `DVD`. Katrai sava `apraksts()` un `izsniegsanas_termins()`.
38. Uzraksti funkciju, kas apstaigā vienumu sarakstu un izvada visu aprakstus.
39. ★ Pievieno iekapsulētu skaitītāju, cik reižu vienums izsniegts.

**Mājasdarbs:** pabeigt 37. uzdevumu

## 12-011 · Sprints: klašu hierarhija
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: klašu hierarhijas projektēšana.
**SR:** Projektē un realizē klašu hierarhiju dotam uzdevuma aprakstam.
**Standarts:** T.A.2.4.15.

**Uzdevumi**
40. Dotajam aprakstam «skolas inventāra uzskaite» izprojektē klašu hierarhiju: kas ir
    virsklase, kas apakšklases, kas abstrakts.
41. Realizē to kodā, izmantojot visus četrus OOP principus.
42. Uzraksti programmu, kas demonstrē katru principu, un komentārā norādi, kur tas ir.
43. ★ Uzzīmē klašu diagrammu un ieliec to repozitorijā.

**Sprints:** `inventars.py` un diagramma

## 12-012 · Sprints: koda pārskatīšana
`[A]` `prakse`

**Tēma:** Cita koda pārskatīšana.
**SR:** Izvērtē cita risinājumu pēc OOP principiem un sniedz konkrētu atgriezenisko saiti.
**Standarts:** T.A.2.4.15. · T.A.2.4.8.

**Uzdevumi**
44. Pārskati klasesbiedra 12-011 risinājumu un uzraksti trīs konkrētas piezīmes.
45. Atrodi vienu vietu, kur mantošana lietota tur, kur nevajadzēja, vai otrādi.
46. ★ Piedāvā konkrētu labojumu koda fragmenta veidā.

**Sprints:** piezīmes klasesbiedra repozitorijā vai `parskats.md`

## 12-013 · Standarta bibliotēka
`[K]` `prakse` · `teorija.py` §8

**Tēma:** Standarta bibliotēkas iespējas. Dokumentācijas lasīšana.
**SR:** Atrod dokumentācijā vajadzīgo standarta bibliotēkas iespēju un lieto to.
**Standarts:** T.A.2.4.10.

**Gaita**
- 5' — cik daudz jau ir Python komplektā
- 15' — demo §8: `collections`, `itertools`, `pathlib`, `datetime`
- 20' — uzdevumi, katram jāatrod risinājums dokumentācijā

**Uzdevumi**
47. Ar `collections.Counter` saskaiti burtu biežumu un salīdzini ar savu ciklu.
48. Ar `collections.defaultdict` pārraksti grupēšanas uzdevumu.
49. Ar `pathlib` uzraksti programmu, kas uzskaita visas `.py` datnes katalogā.
50. Atrodi dokumentācijā vienu `itertools` funkciju un pieraksti tās lietojuma piemēru.
51. ★ Atrodi standarta bibliotēkas moduli, ko vari izmantot savā projektā, un pamato izvēli.

**Mājasdarbs:** 49. uzdevums

## 12-014 · Ārējās bibliotēkas
`[K]` `prakse` · `teorija.py` §9

**Tēma:** Ārējo bibliotēku meklēšana, izvērtēšana un pievienošana.
**SR:** Izvēlas uzdevumam piemērotu ārējo bibliotēku un pamato izvēli.
**Standarts:** T.A.2.4.11. · T.A.2.4.10.

**Gaita**
- 10' — kā izvērtēt bibliotēku: uzturēšana, licence, lietotāju skaits, dokumentācija
- 10' — riski: liekais kods, ievainojamības, atkarību ķēde
- 20' — uzdevumi

**Uzdevumi**
52. Uzstādi bibliotēku virtuālajā vidē un izveido `requirements.txt`.
53. Izvērtē trīs bibliotēkas pēc četriem kritērijiem un aizpildi salīdzinājuma tabulu.
54. Pieraksti, kādi riski rodas, pievienojot projektam svešu bibliotēku.
55. ★ Noskaidro, cik atkarību ievelk viena tava izvēlētā bibliotēka.

**Mājasdarbs:** 53. uzdevums

## 12-015 · Grafiskā saskarne: pamati
`[K]` `prakse` · `teorija.py` §10

**Tēma:** Grafiskā lietotāja saskarne. Logs, elementi, izkārtojums.
**SR:** Izveido logu ar ievades laukiem un pogām.
**Standarts:** T.A.2.4.15. · T.A.2.4.11.

**Gaita**
- 5' — kāpēc standarts prasa grafisko saskarni; kur tā vēl noder
- 15' — demo §10: `tkinter`, logs, `Label`, `Entry`, `Button`, izkārtojums
- 20' — uzdevumi

**Uzdevumi**
56. Izveido logu ar virsrakstu, vienu ievades lauku un pogu.
57. Pievieno otru lauku un sakārto elementus režģī.
58. Pievieno teksta lauku rezultāta izvadīšanai.
59. ★ Pievieno logam izvēlni ar diviem punktiem.

**Mājasdarbs:** 57. uzdevums

## 12-016 · Grafiskā saskarne: notikumi
`[K]` `prakse` · `teorija.py` §11

**Tēma:** Notikumu apstrāde. Poga izsauc funkciju.
**SR:** Sasaista saskarnes elementus ar programmas loģiku.
**Standarts:** T.A.2.4.15.

**Gaita**
- 5' — notikums: lietotājs kaut ko dara, programma atbild
- 15' — demo §11: `command=`, vērtību nolasīšana, kļūdu apstrāde saskarnē
- 20' — uzdevumi

**Uzdevumi**
60. Panāc, lai poga nolasa ievadi un izvada rezultātu logā.
61. Pievieno validāciju: nederīgas ievades gadījumā parādi paziņojumu, nevis avarē.
62. Savieno saskarni ar savu 12-002 klasi `Rezervacija`.
63. ★ Pievieno pogu, kas notīra visus laukus.

**Mājasdarbs:** 61. uzdevums

## 12-017 · Sprints: saskarne un klase kopā
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: grafiskā saskarne virs savas klases.
**SR:** Savieno objektorientētu loģiku ar grafisko saskarni.
**Standarts:** T.A.2.4.15.

**Uzdevumi**
64. Izveido grafisku saskarni savai 12-005 klasei `Lidojums`: rezervēšana, atcelšana,
    brīvo vietu rādīšana.
65. Visai validācijai jāpaliek klasē; saskarne tikai rāda rezultātu.
66. ★ Pievieno sarakstu ar visiem lidojumiem un iespēju izvēlēties.

**Sprints:** `lidojumi_gui.py`

## 12-018 · Sprints: refleksija un uzlabojumi
`[A]` `prakse`

**Tēma:** Sava risinājuma uzlabošana.
**SR:** Atrod savā risinājumā vietas, kur loģika un saskarne ir sajauktas, un atdala tās.
**Standarts:** T.A.2.4.8.

**Uzdevumi**
67. Pārbaudi savu kodu: vai saskarnes failā ir aprēķini, kuriem tur nav vietas?
68. Pārcel tos uz klasi un pārbaudi, ka viss joprojām strādā.
69. ★ Pieraksti, kāpēc loģikas atdalīšana no saskarnes atvieglo testēšanu.

**Sprints:** uzlabots kods un `piezimes.md`

## 12-019 · Datu glabāšana
`[K]` `prakse` · `teorija.py` §12

**Tēma:** Objektu saglabāšana un ielasīšana. CSV un JSON.
**SR:** Saglabā objektus datnē un atjauno tos no tās.
**Standarts:** T.A.2.4.14. · T.A.2.4.17.

**Gaita**
- 5' — programma, kas aizmirst visu, nav produkts
- 15' — demo §12: objekts → vārdnīca → JSON un atpakaļ
- 20' — uzdevumi

**Uzdevumi**
70. Pievieno savai klasei metodi `uz_vardnicu()` un klases metodi `no_vardnicas()`.
71. Saglabā objektu sarakstu JSON datnē un ielasi to atpakaļ.
72. Pievieno programmai automātisku saglabāšanu pēc katras izmaiņas.
73. ★ Apstrādā gadījumu, kad datne ir bojāta vai tukša.

**Mājasdarbs:** 71. uzdevums

## 12-020 · Izņēmumi
`[K]` `prakse` · `teorija.py` §13

**Tēma:** Izņēmumu apstrāde un savi izņēmumu tipi.
**SR:** Apstrādā izņēmumus un definē savu izņēmuma klasi.
**Standarts:** T.A.2.4.6. · T.A.2.4.15.

**Gaita**
- 5' — kļūda nav avārija, ja to sagaidi
- 15' — demo §13: `try`/`except`/`finally`, `raise`, sava izņēmuma klase
- 20' — uzdevumi

**Uzdevumi**
74. Pievieno savai klasei izņēmumu, ko tā met nederīgas darbības gadījumā.
75. Definē savu izņēmuma klasi, kas manto `Exception`.
76. Apstrādā to programmā un parādi lietotājam saprotamu paziņojumu.
77. ★ Pieraksti, kad labāk atgriezt `False` un kad — mest izņēmumu.

**Mājasdarbs:** 75. uzdevums

## 12-021 · Jēdzieni un atkārtojums
`[K]` `jaukta` · FV2 (papīrs)

**Tēma:** OOP jēdzieni. Gatavošanās eksāmena 3. daļai.
**SR:** Skaidro un atšķir četrus OOP pamatprincipus.
**Standarts:** T.A.2.4.15.

**Gaita**
- 15' — **FV2** uz papīra, datori aizvērti
- 15' — kopīgi: kur eksāmena uzdevumos parādās katrs princips
- 10' — biežākās kļūdas jēdzienu skaidrojumos

**Uzdevumi**
78. Burtnīcā: paskaidro katru no četriem principiem vienā teikumā un dod piemēru.
79. Burtnīcā: dotajam koda fragmentam nosaki, kurš princips tajā izmantots.
80. ★ Burtnīcā: uzraksti klases definīciju ar roku pēc dota apraksta.

**Mājasdarbs:** atkārtot jēdzienus

## 12-022 · SV1 uzdevuma izsniegšana
`[K]` `teorija`

**Tēma:** Summatīvā darba specifikācija un vērtēšanas kritēriji.
**SR:** Izprot darba prasības un izplāno tā izpildi.
**Standarts:** T.A.2.4.4.

**Gaita**
- 15' — specifikācijas nolasīšana un jautājumi
- 15' — vērtēšanas kritēriju pārrunāšana
- 10' — katrs pieraksta savu plānu: ko izdarīs katrā no atlikušajām stundām

**Uzdevumi**
81. Izlasi SV1 specifikāciju un uzraksti savu izpildes plānu.
82. Pieraksti, kura prasība tev šķiet grūtākā, un kā to risināsi.
83. ★ Izplāno savu klašu hierarhiju uz papīra pirms koda rakstīšanas.

**Mājasdarbs:** plāns repozitorijā

## 12-023 · SV1 izstrāde
`[K]` `prakse`

**Tēma:** Summatīvā darba izstrāde: klašu modelis.
**SR:** Realizē risinājuma klašu daļu atbilstoši specifikācijai.
**Standarts:** T.A.2.4.15.

**Gaita**
- 35' — izstrāde, individuālas konsultācijas
- 5' — commit

**Stundas beigās:** klases ar konstruktoriem un validāciju strādā.

**Mājasdarbs:** commit ar paveikto

## 12-024 · SV1 izstrāde
`[K]` `prakse`

**Tēma:** Summatīvā darba izstrāde: saskarne un bibliotēka.
**SR:** Pievieno grafisko saskarni un ārējās bibliotēkas funkcionalitāti.
**Standarts:** T.A.2.4.15. · T.A.2.4.11.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** saskarne atver logu un sasaucas ar klasēm.

**Mājasdarbs:** commit ar paveikto

## 12-025 · Sprints: SV1 izstrāde
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs pie summatīvā darba.
**SR:** Turpina izstrādi patstāvīgi.
**Standarts:** T.A.2.4.15.

**Uzdevumi**
84. Turpini izstrādi pēc sava plāna.
85. Pieraksti, kur iestrēgi, lai nākamajā klātienes stundā to varētu atrisināt ātri.

**Sprints:** commit ar paveikto un `piezimes.md`

## 12-026 · Sprints: datu glabāšana un pašpārbaude
`[A]` `prakse`

**Tēma:** Datu saglabāšana un atbilstības pārbaude.
**SR:** Pabeidz saglabāšanas daļu un pārbauda darbu pret specifikāciju.
**Standarts:** T.A.2.4.17.

**Uzdevumi**
86. Pievieno datu saglabāšanu un atjaunošanu.
87. Aizpildi pašpārbaudes tabulu pret SV1 specifikāciju.
88. ★ Notestē savu programmu ar nederīgiem datiem un pieraksti rezultātus.

**Sprints:** `PASPARBAUDE.md` un commit

## 12-027 · SV1: pabeigšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvais darbs: programmprodukta pabeigšana.
**SR:** Pabeidz programmproduktu atbilstoši specifikācijai.
**Standarts:** T.A.2.4.15. · T.A.2.4.11.

**Gaita**
- 35' — pabeigšana pie datora, bez AI rīkiem
- 5' — pēdējais commit un iesniegšana

**Materiāli:** SV1 specifikācija (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

## 12-028 · SV1: aizstāvēšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvā darba demonstrācija un aizstāvēšana.
**SR:** Demonstrē risinājumu, pamato izvēles un veic izmaiņu uz vietas.
**Standarts:** komplekss SR

**Gaita**
- 40' — aizstāvēšanās pēc grafika: demonstrācija, jautājumi, izmaiņa uz vietas

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šī klase OOP jau ir darījusi 11. klasē.** Jaunais šeit: vairāki izveides veidi (12-003),
  `property` (12-004), abstrakcija (12-009), polimorfisms kā projektēšanas paņēmiens
  (12-008), grafiskā saskarne (12-015, 12-016) un izņēmumi (12-020). Pirmās divas stundas
  var iet ātri, ja klase to pierāda.
- **Eksāmena 3. daļa ir 31 % no punktiem** un ir tieši šis bloks. 12-021 jēdzienu stunda nav
  formalitāte — eksāmenā ir uzdevumi, kur jāatpazīst un jāskaidro principi, ne tikai jāraksta kods.
- **Grafiskā saskarne ir standarta prasība**, ne izvēle: kursa apguves prasība nr. 1 skaidri
  nosaka «aplūko grafiskās lietotāja saskarnes programmēšanas principus». Bet uzsvars paliek
  uz klasēm — saskarne ir plāns slānis virs tām, un 12-018 tas tiek tieši pārbaudīts.
- **Attālinātie sprinti ir stundas, ne mājasdarbi.** Ja rezultāta nav, nākamā klātienes
  stunda sākas ar to. Trīs izlaisti sprinti pēc kārtas nozīmē konsultāciju.
