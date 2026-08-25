# 02. Datortīkls, serveris un droša datubāze

**28 stundas (12-029 – 12-056)** · Standarta 2. temats · **SV2 īpatsvars: 15 %**

**Bloka mērķis:** izveidot un konfigurēt daudzlietotāju lokālu tīklu, izveidot serveri
izstrādātāja vajadzībām, izplānot un realizēt drošu datubāzes pielietojumu.

**Teorija un piemēri:** [`teorija.md`](teorija.md) · **Darba fails:** [`uzdevumi.md`](uzdevumi.md)
**Noslēgums:** SV2 — tīkls, serveris un datubāze ar dokumentāciju (12-055, 12-056)

**Eksāmenā:** 2. daļa, 17 % no punktiem.

> Šī bloka nodevums ir **dokumentācija ar pierādījumiem** — ekrānuzņēmumi, konfigurācijas
> fragmenti, SQL skripti. Standarts to prasa tieši tā: «iesniedzot paveikto apliecinošu
> dokumentāciju». Tāpēc darba fails šeit ir `.md`, ne kods.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 02-tikls-un-datubaze/README.md && python3 bin/darbafails.py 02-tikls-un-datubaze -->

| Nr. | Tēma | Sasniedzamais rezultāts |
| --- | --- | --- |
| 12-029 | 11. klases datubāzes prasmju atkārtojums. | Atkārto tabulu, atslēgu un vaicājumu pamatus patstāvīgi. |
| 12-030 | Datubāzes projektēšanas problēmas. | Atpazīst datu dublēšanos un tās sekas. |
| 12-031 | Entītiju un saistību modelis. Datubāzes projektēšanas valoda. | Attēlo datubāzes struktūru ER modelī ar entītijām, atribūtiem un saistībām. |
| 12-032 | Normalizācija. Datu dublēšanās novēršana. | Atpazīst dublēšanos un pārveido tabulu atbilstoši pirmajām trim normālformām. |
| 12-033 | Datubāzes izveide pēc ER modeļa. Ierobežojumi un indeksi. | Izveido datubāzi ar vairākām tabulām, atslēgām, ierobežojumiem un indeksiem. |
| 12-034 | Saliktie vaicājumi. Transakcijas. | Raksta saliktus vaicājumus un lieto transakciju, kur darbības jāveic kopā. |
| 12-035 | Patstāvīgs darbs: datubāzes pabeigšana. | Pabeidz datubāzi ar pilnu ierobežojumu komplektu un testa datiem. |
| 12-036 | Datubāzes dokumentēšana. | Dokumentē datubāzes struktūru tā, lai to saprot cits izstrādātājs. |
| 12-037 | Jaucējfunkcijas. Paroļu glabāšana. | Skaidro jaucējfunkcijas īpašības un lieto to paroļu glabāšanai. |
| 12-038 | Šifrēšana. Publiskā un privātā atslēga. | Atšķir jaukšanu no šifrēšanas un skaidro publiskās atslēgas principu. |
| 12-039 | Datubāzes drošība. SQL injekcija un piekļuves tiesības. | Atpazīst SQL injekcijas risku un novērš to ar parametrizētiem vaicājumiem. |
| 12-040 | Tīmekļa servera izveide. Servera loma izstrādē. | Izveido tīmekļa serveri, kas apkalpo datubāzi, un pārbauda tā darbību. |
| 12-041 | Patstāvīgs darbs: droša servera daļa. | Papildina serveri ar validāciju, kļūdu apstrādi un drošības pasākumiem. |
| 12-042 | Servera dokumentēšana. | Dokumentē servera maršrutus tā, lai citi tos var lietot. |
| 12-043 | Lokālais tīkls. Maršrutētājs, komutators, IP adresācija. | Apraksta lokālā tīkla uzbūvi un ierīču lomas. |
| 12-044 | Maršrutētāja konfigurēšana. Piekļuves kontrole. | Konfigurē bezvadu piekļuves punktu ar paroli un piekļuves ierobežojumiem. |
| 12-045 | Servera pieejamība lokālajā tīklā un internetā. | Padara savu serveri pieejamu citiem tīkla lietotājiem un izvērtē riskus. |
| 12-046 | Servera uzturēšana savās telpās un ārpakalpojumā. | Salīdzina sava un nomāta servera risinājumus un pamato izvēli. |
| 12-047 | Tīkla konfigurācijas dokumentēšana. | Dokumentē tīkla un servera konfigurāciju ar pierādījumiem. |
| 12-048 | SV2 prasību pašpārbaude. | Pārbauda savu darbu pret summatīvā darba prasībām. |
| 12-049 | Bloka jēdzieni. Gatavošanās eksāmena 2. daļai. | Skaidro datubāzu, tīkla un drošības jēdzienus bez rīkiem. |
| 12-050 | Summatīvā darba prasības un plānošana. | Izprot darba prasības un izplāno izpildi. |
| 12-051 | Summatīvā darba izstrāde: datubāze. | Pabeidz datubāzes daļu atbilstoši prasībām. |
| 12-052 | Summatīvā darba izstrāde: serveris un drošība. | Pabeidz servera daļu ar drošības pasākumiem. |
| 12-053 | Patstāvīgs darbs: dokumentācijas pabeigšana. | Pabeidz visu trīs daļu dokumentāciju ar pierādījumiem. |
| 12-054 | Darba pārbaude pirms iesniegšanas. | Pārbauda darba pilnīgumu pret prasībām. |
| 12-055 | Summatīvais darbs: tīkls, serveris un datubāze. | Iesniedz pabeigtu risinājumu ar dokumentāciju. |
| 12-056 | Summatīvā darba demonstrācija un aizstāvēšana. | Demonstrē risinājumu un pamato drošības un projektēšanas izvēles. |

<!-- TABULA:BEIGAS -->

---

## 12-029 · Sprints: datu modeļa atkārtojums
`[A]` `prakse`

**Tēma:** 11. klases datubāzes prasmju atkārtojums.
**SR:** Atkārto tabulu, atslēgu un vaicājumu pamatus patstāvīgi.
**Standarts:** T.A.2.3.2.

**Uzdevumi**
1. Atver savu 11. klases `skola.db` un uzraksti piecus vaicājumus: viens ar `JOIN`, viens ar
   `GROUP BY`, viens ar `LEFT JOIN`, viens ar `HAVING`, viens ar apakšvaicājumu.
2. Pieraksti katram, ko tas atbild un cik rindas atgriež.
3. ★ Uzraksti vaicājumu, kas apvieno trīs tabulas un divus nosacījumus.

**Sprints:** `atkartojums.sql` ar vaicājumiem un komentāriem

## 12-030 · Sprints: kur datubāze nepietiek
`[A]` `teorija`

**Tēma:** Datubāzes projektēšanas problēmas.
**SR:** Atpazīst datu dublēšanos un tās sekas.
**Standarts:** T.A.2.3.2.

**Uzdevumi**
4. Dotajā tabulā katrā rindā atkārtojas skolotāja vārds un e-pasts. Pieraksti trīs problēmas,
   ko tas rada.
5. Pārprojektē šo tabulu divās un pieraksti, kas mainījās.
6. ★ Atrodi savā 11. klases projekta datubāzē vietu, kur dati atkārtojas.

**Sprints:** `analize.md`

## 12-031 · ER modelis
`[K]` `teorija` · `teorija.md` §1

**Tēma:** Entītiju un saistību modelis. Datubāzes projektēšanas valoda.
**SR:** Attēlo datubāzes struktūru ER modelī ar entītijām, atribūtiem un saistībām.
**Standarts:** T.A.2.3.2.

**Gaita**
- 10' — kāpēc pirms `CREATE TABLE` zīmē; ER modeļa elementi
- 15' — kopīgi uz tāfeles: no apraksta uz ER modeli
- 10' — kardinalitāte: 1:1, 1:N, N:M un kā to atzīmē
- 5' — no ER modeļa uz tabulām: mehāniskie soļi

**Uzdevumi**
7. Uzzīmē ER modeli skolas bibliotēkai (grāmata, eksemplārs, lasītājs, izsniegums).
8. Atzīmē katras saistības kardinalitāti un pamato.
9. Pārvērs savu ER modeli tabulās un pieraksti, kur radās starptabula.
10. ★ Uzzīmē ER modeli sistēmai, kurā viena entītija saistās pati ar sevi (piemēram,
    darbinieks un viņa vadītājs).

**Mājasdarbs:** 9. uzdevums

## 12-032 · Normalizācija
`[K]` `jaukta` · `teorija.md` §2

**Tēma:** Normalizācija. Datu dublēšanās novēršana.
**SR:** Atpazīst dublēšanos un pārveido tabulu atbilstoši pirmajām trim normālformām.
**Standarts:** T.A.2.3.2.

**Gaita**
- 10' — trīs normālformas cilvēku valodā
- 15' — kopīgi: slikti projektēta tabula un tās sadalīšana
- 10' — kad normalizāciju apzināti pārkāpj (ātrdarbība)
- 5' — kā to pamanīt savā projektā

**Uzdevumi**
11. Dotajai tabulai atrodi 1NF pārkāpumu (vairākas vērtības vienā laukā) un izlabo.
12. Dotajai tabulai atrodi 2NF un 3NF pārkāpumus un sadali to.
13. Pārbaudi savu 12-031 modeli pret trim normālformām.
14. ★ Atrodi piemēru, kur dublēšanās ir apzināta izvēle, un pamato, kāpēc.

**Mājasdarbs:** 13. uzdevums

## 12-033 · Datubāzes izveide
`[K]` `prakse` · `teorija.md` §3

**Tēma:** Datubāzes izveide pēc ER modeļa. Ierobežojumi un indeksi.
**SR:** Izveido datubāzi ar vairākām tabulām, atslēgām, ierobežojumiem un indeksiem.
**Standarts:** T.A.2.3.2. · T.A.2.4.17.

**Gaita**
- 5' — no modeļa uz skriptu
- 10' — demo §3: `CREATE TABLE`, `FOREIGN KEY`, `CHECK`, `CREATE INDEX`
- 20' — uzdevumi
- 5' — kāpēc skripts, ne klikšķināšana: to var atkārtot un ielikt repozitorijā

**Uzdevumi**
15. Realizē savu 12-031 modeli kā `shema.sql` ar visām atslēgām un ierobežojumiem.
16. Pievieno indeksu laukam, pēc kura meklēsi visbiežāk, un pamato izvēli.
17. Ievieto testa datus: vismaz pieci ieraksti katrā tabulā.
18. Pārbaudi, ka ierobežojumi tiešām neļauj ievadīt nederīgus datus.
19. ★ Uzraksti skriptu, kas datubāzi izdzēš un izveido no jauna vienā palaišanā.

**Mājasdarbs:** 17. uzdevums

## 12-034 · Vaicājumi un transakcijas
`[K]` `prakse` · `teorija.md` §4

**Tēma:** Saliktie vaicājumi. Transakcijas.
**SR:** Raksta saliktus vaicājumus un lieto transakciju, kur darbības jāveic kopā.
**Standarts:** T.A.2.4.17.

**Gaita**
- 5' — kas notiek, ja naudas pārskaitījuma vidū pazūd strāva?
- 15' — demo §4: apakšvaicājumi, `BEGIN` / `COMMIT` / `ROLLBACK`
- 15' — uzdevumi
- 5' — kad transakcija tiešām vajadzīga

**Uzdevumi**
20. Uzraksti vaicājumu ar apakšvaicājumu: ieraksti, kuru vērtība ir virs vidējās.
21. Uzraksti darbību pāri, kas jāveic kopā, un ietver to transakcijā.
22. Izmēģini `ROLLBACK` un pārbaudi, ka izmaiņas atceltas.
23. ★ Pieraksti savā projektā vietu, kur transakcija būs vajadzīga.

**Mājasdarbs:** 21. uzdevums

## 12-035 · Sprints: sava datubāze
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: datubāzes pabeigšana.
**SR:** Pabeidz datubāzi ar pilnu ierobežojumu komplektu un testa datiem.
**Standarts:** T.A.2.3.2.

**Uzdevumi**
24. Pabeidz savu datubāzi: visas tabulas, atslēgas, ierobežojumi, indeksi.
25. Uzraksti desmit vaicājumus, kas atbild uz reāliem jautājumiem par taviem datiem.
26. ★ Uzraksti vaicājumu, kas atrod datus, kuri pārkāpj kādu loģisku noteikumu, ko datubāze
    pati nepārbauda.

**Sprints:** `shema.sql`, `dati.sql`, `vaicajumi.sql`

## 12-036 · Sprints: dokumentācija
`[A]` `prakse`

**Tēma:** Datubāzes dokumentēšana.
**SR:** Dokumentē datubāzes struktūru tā, lai to saprot cits izstrādātājs.
**Standarts:** T.A.2.4.7.

**Uzdevumi**
27. Uzraksti `DATUBAZE.md`: ER modeļa attēls, tabulu apraksts, lauku nozīme.
28. Katrai tabulai pieraksti, kāpēc tā ir atsevišķa.
29. ★ Pieraksti, kas jāmaina, ja sistēmai pievienotu vēl vienu funkciju.

**Sprints:** `DATUBAZE.md`

## 12-037 · Kriptogrāfija: jaucējfunkcijas
`[K]` `prakse` · `teorija.md` §5

**Tēma:** Jaucējfunkcijas. Paroļu glabāšana.
**SR:** Skaidro jaucējfunkcijas īpašības un lieto to paroļu glabāšanai.
**Standarts:** T.A.3.1.2.

**Gaita**
- 10' — kas notiek, kad noplūst datubāze ar paroles atklātā tekstā
- 15' — demo §5: `hashlib`, sāls, kāpēc SHA-256 vien nepietiek
- 10' — uzdevumi
- 5' — kur šo redzam ikdienā: «paroli atjaunot nevar, tikai nomainīt»

**Uzdevumi**
30. Aprēķini teksta jaucējvērtību un pārbaudi, ka vienādam tekstam tā vienmēr ir vienāda.
31. Nomaini vienu burtu un salīdzini rezultātu.
32. Pievieno savai datubāzei tabulu `lietotaji` ar jaucējvērtību, nevis paroli.
33. Uzraksti reģistrācijas un pieteikšanās funkcijas.
34. ★ Pievieno sāli un paskaidro komentārā, pret ko tā pasargā.

**Mājasdarbs:** 33. uzdevums

## 12-038 · Simetriskā un asimetriskā šifrēšana
`[K]` `jaukta` · FV3 (dators) · `teorija.md` §6

**Tēma:** Šifrēšana. Publiskā un privātā atslēga.
**SR:** Atšķir jaukšanu no šifrēšanas un skaidro publiskās atslēgas principu.
**Standarts:** T.A.3.1.2.

**Gaita**
- 10' — trīs dažādas lietas: jaukšana, simetriskā, asimetriskā šifrēšana
- 10' — demo §6: kā darbojas publiskā un privātā atslēga
- 15' — **FV3** pie datora
- 5' — kur to lieto: HTTPS, paraksti, SSH

**Uzdevumi**
35. Uzraksti programmu, kas šifrē un atšifrē tekstu ar simetrisku atslēgu.
36. Pieraksti, kāpēc jaucējvērtību atšifrēt nevar, bet šifrētu tekstu — var.
37. Paskaidro, kā divi cilvēki var apmainīties ar noslēpumu, nekad nesatiekoties.
38. ★ Noskaidro, kā HTTPS izmanto abus šifrēšanas veidus, un pieraksti soļus.

**Mājasdarbs:** 37. uzdevums

## 12-039 · Datu drošība datubāzē
`[K]` `prakse` · `teorija.md` §7

**Tēma:** Datubāzes drošība. SQL injekcija un piekļuves tiesības.
**SR:** Atpazīst SQL injekcijas risku un novērš to ar parametrizētiem vaicājumiem.
**Standarts:** T.A.3.1.2. · T.A.2.4.17.

**Gaita**
- 10' — klasiskais piemērs: `' OR '1'='1`
- 15' — demo §7: kāpēc virkņu salikšana ir bīstama; parametrizēti vaicājumi
- 10' — uzdevumi
- 5' — personas datu glabāšanas principi

**Uzdevumi**
39. Uzraksti apzināti ievainojamu vaicājumu un parādi, kā to izmantot.
40. Pārraksti to ar parametriem un pārbaudi, ka uzbrukums vairs nestrādā.
41. Pārbaudi savu projekta kodu: vai kaut kur vaicājums tiek salikts no virknēm?
42. ★ Pieraksti, kādus personas datus tava sistēma glabā un kāpēc katrs ir vajadzīgs.

**Mājasdarbs:** 40. uzdevums

## 12-040 · Serveris izstrādātāja vajadzībām
`[K]` `prakse` · `teorija.md` §8

**Tēma:** Tīmekļa servera izveide. Servera loma izstrādē.
**SR:** Izveido tīmekļa serveri, kas apkalpo datubāzi, un pārbauda tā darbību.
**Standarts:** T.A.2.3.1.

**Gaita**
- 5' — atkārtojums no 11. klases: klients, serveris, maršruts
- 15' — demo §8: serveris ar datubāzi; žurnalēšana
- 15' — uzdevumi
- 5' — kas atšķiras starp izstrādes un ražošanas serveri

**Uzdevumi**
43. Izveido serveri, kas atgriež datus no tavas datubāzes.
44. Pievieno žurnalēšanu: katrs pieprasījums tiek pierakstīts ar laiku un statusa kodu.
45. Pievieno maršrutu, kas atgriež datubāzes kopsavilkumu.
46. ★ Pievieno vienkāršu pieteikšanos, kas izmanto 12-037 jaucējvērtības.

**Mājasdarbs:** 44. uzdevums

## 12-041 · Sprints: serveris un drošība
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: droša servera daļa.
**SR:** Papildina serveri ar validāciju, kļūdu apstrādi un drošības pasākumiem.
**Standarts:** T.A.2.3.1. · T.A.3.1.2.

**Uzdevumi**
47. Pievieno visiem maršrutiem validāciju un pareizus statusa kodus.
48. Pārbaudi, ka kļūdas paziņojumos nav SQL vaicājumu vai failu ceļu.
49. Pārbaudi, ka visi vaicājumi ir parametrizēti.
50. ★ Pievieno ierobežojumu, cik pieprasījumu minūtē pieņem no viena klienta.

**Sprints:** serveris repozitorijā ar drošības pārbaudēm

## 12-042 · Sprints: servera dokumentācija
`[A]` `prakse`

**Tēma:** Servera dokumentēšana.
**SR:** Dokumentē servera maršrutus tā, lai citi tos var lietot.
**Standarts:** T.A.2.4.7.

**Uzdevumi**
51. Uzraksti `SERVERIS.md`: katram maršrutam metode, adrese, parametri, atbildes piemērs.
52. Pievieno palaišanas instrukciju no nulles.
53. ★ Pievieno kļūdu tabulu: kurā gadījumā kurš statusa kods.

**Sprints:** `SERVERIS.md`

## 12-043 · Datortīkla uzbūve
`[K]` `teorija` · `teorija.md` §9

**Tēma:** Lokālais tīkls. Maršrutētājs, komutators, IP adresācija.
**SR:** Apraksta lokālā tīkla uzbūvi un ierīču lomas.
**Standarts:** T.A.2.3.1.

**Gaita**
- 10' — tīkla ierīces un to lomas
- 10' — IP adrese, apakštīkla maska, vārteja, DNS
- 15' — statiskā un dinamiskā adrese; DHCP
- 5' — kā to visu redzēt savā datorā

**Uzdevumi**
54. Noskaidro sava datora IP adresi, apakštīkla masku, vārteju un DNS serveri.
55. Uzzīmē skolas kabineta tīkla shēmu ar ierīcēm un adresēm.
56. Pieraksti, ar ko atšķiras statiskā un dinamiskā IP adrese un kad kuru lieto.
57. ★ Noskaidro, cik ierīču var būt tīklā ar masku 255.255.255.0, un paskaidro, kāpēc.

**Mājasdarbs:** 56. uzdevums

## 12-044 · Maršrutētāja konfigurācija
`[K]` `prakse` · `teorija.md` §10

**Tēma:** Maršrutētāja konfigurēšana. Piekļuves kontrole.
**SR:** Konfigurē bezvadu piekļuves punktu ar paroli un piekļuves ierobežojumiem.
**Standarts:** T.A.2.3.1. · T.A.3.1.2.

**Gaita**
- 10' — demonstrācija ar īstu maršrutētāju: noklusētā konfigurācija un kāpēc to maina
- 10' — Wi-Fi parole, MAC filtrs, portu pāradresācija
- 15' — uzdevumi pāros ar telefona karstvietu, ja maršrutētāju nepietiek
- 5' — kāpēc portu atvēršana ir risks

**Uzdevumi**
58. Konfigurē bezvadu piekļuves punktu ar paroli un pieraksti soļus ar ekrānuzņēmumiem.
59. Pieraksti, ko dara MAC adrešu filtrs un kāpēc tas nav droša aizsardzība.
60. Pieraksti, kas ir portu pāradresācija un kādos gadījumos tā vajadzīga.
61. ★ Pieraksti piecas darbības, ko izdarītu ar jaunu maršrutētāju pirms tā lietošanas.

**Mājasdarbs:** 58. uzdevums

## 12-045 · Servera pieejamība tīklā
`[K]` `prakse` · `teorija.md` §11

**Tēma:** Servera pieejamība lokālajā tīklā un internetā.
**SR:** Padara savu serveri pieejamu citiem tīkla lietotājiem un izvērtē riskus.
**Standarts:** T.A.2.3.1.

**Gaita**
- 5' — `localhost` pret `0.0.0.0`
- 10' — serveris tīklā: kā to atrod citi
- 20' — uzdevumi pāros
- 5' — kas mainās, ja to atver internetam

**Uzdevumi**
62. Palaid savu serveri tā, lai tas ir pieejams no cita datora lokālajā tīklā.
63. Pārbaudi to no klasesbiedra datora un pieraksti adresi.
64. Pieraksti, kādi riski rodas, atverot serveri, un ko izdarītu vispirms.
65. ★ Salīdzini sava servera uzturēšanu skolā un nomātu serveri: izmaksas, drošība,
    pieejamība, atbildība.

**Mājasdarbs:** 64. uzdevums

## 12-046 · Servera uzturēšana
`[K]` `teorija` · `teorija.md` §12

**Tēma:** Servera uzturēšana savās telpās un ārpakalpojumā.
**SR:** Salīdzina sava un nomāta servera risinājumus un pamato izvēli.
**Standarts:** T.A.2.3.1.

**Gaita**
- 10' — kas jāapsver, turot serveri savās telpās: strāva, mikroklimats, fiziskā drošība
- 10' — ārpakalpojums: nomas modeļi, piekļuves tiesības, atbildības sadalījums
- 15' — uzdevumi
- 5' — rezerves kopijas: cik bieži un kur

**Uzdevumi**
66. Aizpildi salīdzinājuma tabulu: savs serveris pret nomātu, pēc pieciem kritērijiem.
67. Izvēlies risinājumu savam projektam un pamato.
68. Pieraksti rezerves kopiju plānu: ko, cik bieži, kur, kā pārbaudi, ka tas strādā.
69. ★ Pieraksti, kas notiktu ar tavu sistēmu, ja serveris pazustu šodien.

**Mājasdarbs:** 68. uzdevums

## 12-047 · Sprints: tīkla dokumentācija
`[A]` `prakse`

**Tēma:** Tīkla konfigurācijas dokumentēšana.
**SR:** Dokumentē tīkla un servera konfigurāciju ar pierādījumiem.
**Standarts:** T.A.2.3.1. · T.A.2.4.7.

**Uzdevumi**
70. Uzraksti `TIKLS.md`: tīkla shēma, adresācija, maršrutētāja iestatījumi ar ekrānuzņēmumiem.
71. Pievieno sadaļu par drošību: kas darīts un kas apzināti nav darīts.
72. ★ Pievieno soļus, kā visu atjaunot no nulles.

**Sprints:** `TIKLS.md`

## 12-048 · Sprints: pašpārbaude
`[A]` `prakse`

**Tēma:** SV2 prasību pašpārbaude.
**SR:** Pārbauda savu darbu pret summatīvā darba prasībām.
**Standarts:** T.A.2.4.6.

**Uzdevumi**
73. Aizpildi pašpārbaudes tabulu pret SV2 prasībām.
74. Pieraksti, kas vēl jāizdara, un saplāno atlikušās stundas.
75. ★ Iedod savu dokumentāciju klasesbiedram un palūdz izpildīt vienu soli pēc tās.

**Sprints:** `PASPARBAUDE.md`

## 12-049 · Jēdzieni un atkārtojums
`[K]` `jaukta` · FV4 (papīrs)

**Tēma:** Bloka jēdzieni. Gatavošanās eksāmena 2. daļai.
**SR:** Skaidro datubāzu, tīkla un drošības jēdzienus bez rīkiem.
**Standarts:** T.A.2.3.2. · T.A.3.1.2.

**Gaita**
- 15' — **FV4** uz papīra, datori aizvērti
- 15' — kopīgi: kā izskatās eksāmena 2. daļas uzdevumi
- 10' — biežākās kļūdas ER modeļos

**Uzdevumi**
76. Burtnīcā: uzzīmē ER modeli dotam aprakstam un pārvērs to tabulās.
77. Burtnīcā: uzraksti `CREATE TABLE` ar roku, ieskaitot atslēgas un ierobežojumus.
78. Burtnīcā: paskaidro, kāpēc parole datubāzē netiek glabāta atklātā tekstā.
79. ★ Burtnīcā: uzraksti vaicājumu ar `JOIN` un `GROUP BY` bez datora.

**Mājasdarbs:** atkārtot jēdzienus

## 12-050 · SV2 uzdevuma izsniegšana
`[K]` `teorija`

**Tēma:** Summatīvā darba prasības un plānošana.
**SR:** Izprot darba prasības un izplāno izpildi.
**Standarts:** T.A.2.4.4.

**Gaita**
- 15' — prasību nolasīšana, jautājumi
- 15' — vērtēšanas kritēriji un dokumentācijas prasības
- 10' — katrs pieraksta plānu atlikušajām stundām

**Uzdevumi**
80. Izlasi SV2 prasības un uzraksti savu izpildes plānu.
81. Pieraksti, kura daļa būs grūtākā un ko darīsi, ja tā neizdodas.
82. ★ Pārbaudi, kuras prasības jau ir izpildītas sprintos.

**Mājasdarbs:** plāns repozitorijā

## 12-051 · SV2 izstrāde
`[K]` `prakse`

**Tēma:** Summatīvā darba izstrāde: datubāze.
**SR:** Pabeidz datubāzes daļu atbilstoši prasībām.
**Standarts:** T.A.2.3.2. · T.A.2.4.17.

**Gaita**
- 35' — izstrāde, individuālas konsultācijas
- 5' — commit

**Stundas beigās:** datubāze ar visām tabulām, ierobežojumiem un testa datiem strādā.

**Mājasdarbs:** commit ar paveikto

## 12-052 · SV2 izstrāde
`[K]` `prakse`

**Tēma:** Summatīvā darba izstrāde: serveris un drošība.
**SR:** Pabeidz servera daļu ar drošības pasākumiem.
**Standarts:** T.A.2.3.1. · T.A.3.1.2.

**Gaita**
- 35' — izstrāde
- 5' — commit

**Stundas beigās:** serveris strādā ar datubāzi, vaicājumi parametrizēti, paroles jauktas.

**Mājasdarbs:** commit ar paveikto

## 12-053 · Sprints: dokumentācijas pabeigšana
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: dokumentācijas pabeigšana.
**SR:** Pabeidz visu trīs daļu dokumentāciju ar pierādījumiem.
**Standarts:** T.A.2.4.7.

**Uzdevumi**
83. Pabeidz `DATUBAZE.md`, `SERVERIS.md` un `TIKLS.md`.
84. Pievieno visus ekrānuzņēmumus un konfigurācijas fragmentus.
85. ★ Pārbaudi, vai svešs cilvēks pēc tavas dokumentācijas var visu atkārtot.

**Sprints:** pilna dokumentācija repozitorijā

## 12-054 · Sprints: pārbaude pirms iesniegšanas
`[A]` `prakse`

**Tēma:** Darba pārbaude pirms iesniegšanas.
**SR:** Pārbauda darba pilnīgumu pret prasībām.
**Standarts:** T.A.2.4.6.

**Uzdevumi**
86. Izpildi savu pašpārbaudes tabulu vēlreiz un atzīmē izmaiņas.
87. Pārbaudi, ka datubāzi var izveidot no nulles ar tavu skriptu.
88. ★ Notestē serveri ar nederīgiem datiem un pieraksti rezultātus.

**Sprints:** gatavs darbs repozitorijā

## 12-055 · SV2: iesniegšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvais darbs: tīkls, serveris un datubāze.
**SR:** Iesniedz pabeigtu risinājumu ar dokumentāciju.
**Standarts:** T.A.2.3.1. · T.A.2.3.2. · T.A.3.1.2.

**Gaita**
- 35' — pēdējie labojumi pie datora, bez AI rīkiem
- 5' — iesniegšana

**Materiāli:** SV2 prasības (skat. `kurss/vertesana.md`)

**Mājasdarbs:** —

## 12-056 · SV2: aizstāvēšana
`[K]` `pārbaudes darbs`

**Tēma:** Summatīvā darba demonstrācija un aizstāvēšana.
**SR:** Demonstrē risinājumu un pamato drošības un projektēšanas izvēles.
**Standarts:** komplekss SR

**Gaita**
- 40' — aizstāvēšanās: demonstrācija, jautājumi par ER modeli un drošību, izmaiņa uz vietas

**Mājasdarbs:** —

---

## Metodiskās piezīmes

- **Šī bloka nodevums ir dokumentācija.** Standarta prasība nr. 2 to nosaka tieši:
  «iesniedzot paveiktā apliecinošu dokumentāciju». Tāpēc trīs sprinti (12-036, 12-042,
  12-047) ir veltīti tieši dokumentēšanai, un darba fails ir markdown, ne kods.
- **Maršrutētājs.** Ja kabinetā ir viens maršrutētājs, dari to kā demonstrāciju un ļauj
  skolēniem konfigurēt telefona karstvietu — standarts to tieši pieļauj. Svarīgākais, ko
  skolēnam saprast, ir noklusētās konfigurācijas maiņa un tas, ka atvērts ports ir risks.
- **SQL injekcija 12-039 ir jāparāda darbībā.** Uz savas testa datubāzes, ne uz kāda cita.
  Kad skolēns pats ieraksta `' OR '1'='1` un redz, ka pieteikšanās izdodas, parametrizēti
  vaicājumi vairs nav noteikums no grāmatas.
- **Normalizācija ir eksāmena 2. daļas serde.** ER modelis ar roku uz papīra (12-049) ir
  tieši tas formāts, kādā tas parādās eksāmenā.
