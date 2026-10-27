# 02. Datortīkls, serveris un droša datubāze

**28 stundas (12-029 – 12-056)** · Standarta 2. temats · **SV2 īpatsvars: 15 %**

**Bloka mērķis:** izveidot un konfigurēt daudzlietotāju lokālu tīklu, izveidot serveri
izstrādātāja vajadzībām, izplānot un realizēt drošu datubāzes pielietojumu.

**Teorija un piemēri:** [`teorija.md`](teorija.md) · Python un SQL — [`teorija.py`](teorija.py)
**Situāciju krājums:** [`situacijas.md`](situacijas.md) — ER modeļi un normalizācija
**Darba faili:** [`uzdevumi.md`](uzdevumi.md) · programmēšanas stundām (12-033 – 12-035)
[`uzdevumi.py`](uzdevumi.py)
**Noslēgums:** SV2 — tīkls, serveris un datubāze ar dokumentāciju (12-055, 12-056)

**Eksāmenā:** 2. daļa, 17 % no punktiem.

> Šī bloka nodevums ir **dokumentācija ar pierādījumiem** — ekrānuzņēmumi, konfigurācijas
> fragmenti, SQL skripti. Standarts to prasa tieši tā: «iesniedzot paveikto apliecinošu
> dokumentāciju». Tāpēc galvenais darba fails šeit ir `.md`; `uzdevumi.py` ir tikai stundām,
> kurās raksta programmu.

<!-- TABULA:SAKUMS · pēc izmaiņām: python3 bin/tabula.py 02-tikls-un-datubaze/README.md && python3 bin/darbafails.py 02-tikls-un-datubaze -->

| Nr. | Tēma | Sasniedzamais rezultāts | Pārbaude |
| --- | --- | --- | --- |
| 12-029 | 11. klases datubāzes prasmju atkārtojums. | Atkārto tabulu, atslēgu un vaicājumu pamatus patstāvīgi. |  |
| 12-030 | Datubāzes projektēšanas problēmas. | Atpazīst datu dublēšanos un tās sekas. |  |
| 12-031 | Entītiju un saistību modelis. Datubāzes projektēšanas valoda. | Attēlo datubāzes struktūru ER modelī ar entītijām, atribūtiem un saistībām. |  |
| 12-032 | Normalizācija. Datu dublēšanās novēršana. | Atpazīst dublēšanos un pārveido tabulu atbilstoši pirmajām trim normālformām. |  |
| 12-033 | Datubāzes izveide pēc ER modeļa. Ierobežojumi un indeksi. | Izveido datubāzi ar vairākām tabulām, atslēgām, ierobežojumiem un indeksiem. |  |
| 12-034 | Saliktie vaicājumi. Transakcijas. | Raksta saliktus vaicājumus un lieto transakciju, kur darbības jāveic kopā. |  |
| 12-035 | Patstāvīgs darbs: datubāzes pabeigšana. | Pabeidz datubāzi ar pilnu ierobežojumu komplektu un testa datiem. |  |
| 12-036 | Datubāzes dokumentēšana. | Dokumentē datubāzes struktūru tā, lai to saprot cits izstrādātājs. |  |
| 12-037 | Jaucējfunkcijas. Paroļu glabāšana. | Skaidro jaucējfunkcijas īpašības un lieto to paroļu glabāšanai. |  |
| 12-038 | Šifrēšana. Publiskā un privātā atslēga. | Atšķir jaukšanu no šifrēšanas un skaidro publiskās atslēgas principu. | **FV3** (dators) |
| 12-039 | Datubāzes drošība. SQL injekcija un piekļuves tiesības. | Atpazīst SQL injekcijas risku un novērš to ar parametrizētiem vaicājumiem. |  |
| 12-040 | Tīmekļa servera izveide. Servera loma izstrādē. | Izveido tīmekļa serveri, kas apkalpo datubāzi, un pārbauda tā darbību. |  |
| 12-041 | Patstāvīgs darbs: droša servera daļa. | Papildina serveri ar validāciju, kļūdu apstrādi un drošības pasākumiem. |  |
| 12-042 | Servera dokumentēšana. | Dokumentē servera maršrutus tā, lai citi tos var lietot. |  |
| 12-043 | Lokālais tīkls. Maršrutētājs, komutators, IP adresācija. | Apraksta lokālā tīkla uzbūvi un ierīču lomas. |  |
| 12-044 | Maršrutētāja konfigurēšana. Piekļuves kontrole. | Konfigurē bezvadu piekļuves punktu ar paroli un piekļuves ierobežojumiem. |  |
| 12-045 | Servera pieejamība lokālajā tīklā un internetā. | Padara savu serveri pieejamu citiem tīkla lietotājiem un izvērtē riskus. |  |
| 12-046 | Servera uzturēšana savās telpās un ārpakalpojumā. | Salīdzina sava un nomāta servera risinājumus un pamato izvēli. |  |
| 12-047 | Tīkla konfigurācijas dokumentēšana. | Dokumentē tīkla un servera konfigurāciju ar pierādījumiem. |  |
| 12-048 | SV2 prasību pašpārbaude. | Pārbauda savu darbu pret summatīvā darba prasībām. |  |
| 12-049 | Bloka jēdzieni. Gatavošanās eksāmena 2. daļai. | Skaidro datubāzu, tīkla un drošības jēdzienus bez rīkiem. | **FV4** (papīrs) |
| 12-050 | Summatīvā darba prasības un plānošana. | Izprot darba prasības un izplāno izpildi. |  |
| 12-051 | Summatīvā darba izstrāde: datubāze. | Pabeidz datubāzes daļu atbilstoši prasībām. |  |
| 12-052 | Summatīvā darba izstrāde: serveris un drošība. | Pabeidz servera daļu ar drošības pasākumiem. |  |
| 12-053 | Patstāvīgs darbs: dokumentācijas pabeigšana. | Pabeidz visu trīs daļu dokumentāciju ar pierādījumiem. |  |
| 12-054 | Darba pārbaude pirms iesniegšanas. | Pārbauda darba pilnīgumu pret prasībām. |  |
| 12-055 | Summatīvais darbs: tīkls, serveris un datubāze. | Iesniedz pabeigtu risinājumu ar dokumentāciju. | **SV2** |
| 12-056 | Summatīvā darba demonstrācija un aizstāvēšana. | Demonstrē risinājumu un pamato drošības un projektēšanas izvēles. | **SV2** |

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

4. Situāciju krājuma ([`situacijas.md`](situacijas.md)) tabulā **N0** katrā rindā atkārtojas
   skolotāja vārds un e-pasts. Pieraksti trīs problēmas, ko tas rada.
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
- 15' — kopīgi uz tāfeles: no apraksta uz ER modeli (paraugs — `teorija.md` §1)
- 10' — kardinalitāte: 1:1, 1:N, N:M un kā to atzīmē
- 5' — no ER modeļa uz tabulām: mehāniskie soļi

**Uzdevumi**

7. Uzzīmē ER modeli skolas bibliotēkai (grāmata, eksemplārs, lasītājs, izsniegums).
8. Atzīmē katras saistības kardinalitāti un pamato.
9. Pārvērs savu ER modeli tabulās un pieraksti, kur radās starptabula.
10. ★ Uzzīmē ER modeli sistēmai, kurā viena entītija saistās pati ar sevi (piemēram,
    darbinieks un viņa vadītājs).
11. Uzzīmē ER modeli kinoteātra biļešu sistēmai: filmas, zāles, seansi, vietas, biļetes,
    pircēji. Pārvērs to tabulās.
12. ★ Situāciju krājumā izvēlies divas situācijas no E1–E8 un uzzīmē to ER modeļus.

**Mājasdarbs:** 11. uzdevums

## 12-032 · Normalizācija
`[K]` `jaukta` · `teorija.md` §2

**Tēma:** Normalizācija. Datu dublēšanās novēršana.
**SR:** Atpazīst dublēšanos un pārveido tabulu atbilstoši pirmajām trim normālformām.
**Standarts:** T.A.2.3.2.

**Gaita**
- 5' — atkārtojums: tabula N0 un trīs anomālijas (`teorija.md` §2)
- 10' — trīs normālformas cilvēku valodā; jautājums «no kā tas ir atkarīgs?»
- 15' — pāros: N1–N7, katrs pāris pa vienai tabulai no katras normālformas; pārrunājam
- 10' — kopīgi uz tāfeles: N8 soli pa solim; kad normalizāciju apzināti pārkāpj

**Uzdevumi**

13. Situāciju krājumā **N1**, **N2**, **N3**: atrodi 1NF pārkāpumu un sadali tabulu.
14. **N4** un **N5**: nosaki primāro atslēgu, atrodi laukus, kas atkarīgi tikai no tās daļas,
    un sadali tabulu.
15. **N6** un **N7**: atrodi 3NF pārkāpumu un sadali tabulu. Pie N7 pamato, vai reālā
    sistēmā to sadalītu.
16. **N8**: izpildi visus sešus soļus — no Excel lapas līdz 3NF un ER modelim.
17. Pārbaudi savu kinoteātra modeli (11. uzdevums) pret trim normālformām un izlabo.
18. Izvēlies savas sistēmas tēmu: šo datubāzi tu veidosi 12-035 sprintā un nodosi SV2
    darbā. Uzraksti divu teikumu aprakstu un uzzīmē ER skici: vismaz četras entītijas,
    tostarp viena N:M saistība.
19. ★ **N9** un **N10**.

**Mājasdarbs:** 17. un 18. uzdevums

## 12-033 · Datubāze no Python
`[K]` `prakse` · `teorija.py` §1–§7

**Tēma:** Datubāzes izveide pēc ER modeļa. Ierobežojumi un indeksi.
**SR:** Izveido datubāzi ar vairākām tabulām, atslēgām, ierobežojumiem un indeksiem.
**Standarts:** T.A.2.3.2. · T.A.2.4.17.

**Gaita**
- 5' — `skola.db` izveide; demo §1: savienojums un pirmais vaicājums no Python
- 15' — SQL atkārtojums uz `skola.db` ar §2 atgādni (20.–24. uzdevums)
- 10' — demo §3–§6: `CREATE TABLE` ar ierobežojumiem, `PRAGMA foreign_keys`, `IntegrityError`,
  indekss
- 10' — bibliotēkas shēma no 12-031 modeļa; ko nepaspēj, pabeidz mājās

**Uzdevumi**

20. Izveido mācību datubāzi: no repozitorija saknes palaid
    `python3 bin/izveido_db.py 02-tikls-un-datubaze/skola.db`. Savienojies ar to no Python
    un izdrukā visu tabulu nosaukumus (`teorija.py` §1 un §3). Ja redzi `no such table`,
    datubāze nav tajā mapē, kur to meklē.
    ```python
    import sqlite3
    from pathlib import Path

    MAPE = Path(__file__).parent
    con = sqlite3.connect(MAPE / "skola.db", isolation_level=None)
    con.execute("PRAGMA foreign_keys = ON")
    ```
21. Uzraksti funkciju `radit(sql, parametri=())`, kas izpilda vaicājumu un izdrukā kolonnu
    nosaukumus, rindas un rindu skaitu.
22. SQL atkārtojums — viena tabula. Uzraksti vaicājumus:
    - a) skolēni, kas dzimuši 2008. gadā, sakārtoti pēc uzvārda;
    - b) skolēni, kuriem nav e-pasta;
    - c) cik reižu ir likta katra atzīme no 1 līdz 10;
    - d) cik skolēnu ir katrā klasē (pēc `klase_id`);
    - e) desmit augstākās decembrī saņemtās atzīmes ar datumu.
23. SQL atkārtojums — vairākas tabulas. Uzraksti vaicājumus:
    - a) katras klases nosaukums un audzinātāja vārds un uzvārds;
    - b) katra priekšmeta vidējā atzīme, noapaļota līdz divām zīmēm, augstākā vispirms;
    - c) klases, kuru vidējā atzīme ir augstāka par 6,7;
    - d) skolēni, kuriem nav nevienas atzīmes;
    - e) visi pulciņi ar dalībnieku skaitu, ieskaitot pulciņus bez dalībniekiem;
    - f) ★ pieci skolēni ar augstāko vidējo atzīmi starp tiem, kam ir vismaz 10 atzīmes.
24. Uzraksti funkciju `klases_skoleni(klase)`, kas atgriež dotās klases (piemēram, `"12.a"`)
    skolēnu vārdus un uzvārdus. Klases nosaukumu padod ar `?`, nevis ar f-string.
25. Realizē savu 12-031 bibliotēkas ER modeli kā failu `biblioteka.sql` ar tabulām
    `gramatas`, `eksemplari`, `lasitaji`, `izsniegumi`. Prasības:
    - primārās un ārējās atslēgas;
    - `NOT NULL` visur, kur tukša vērtība nav jēgpilna;
    - `UNIQUE` svītrkodam un e-pastam;
    - `CHECK` izdošanas gadam un tam, ka atgriešanas datums nav agrāks par izsniegšanas;
    - `DEFAULT` izsniegšanas datumam.
26. Uzraksti funkciju `izveidot_biblioteku()`, kas izdzēš veco `biblioteka.db`, ieslēdz
    ārējo atslēgu pārbaudi un izpilda `biblioteka.sql` (`teorija.py` §7). Ievieto testa
    datus ar `executemany`: vismaz pieci ieraksti katrā tabulā.
27. Pārbaudi ierobežojumus. Katrai darbībai jābeidzas ar `sqlite3.IntegrityError`. Izdrukā
    kļūdas tekstu un komentārā pieraksti, kurš ierobežojums to apturēja:
    - a) lasītājs ar jau esošu e-pastu;
    - b) eksemplārs grāmatai, kuras nav (`gramata_id = 999`);
    - c) grāmata bez autora;
    - d) grāmata ar izdošanas gadu 3025;
    - e) izsniegums, kas atgriezts agrāk, nekā izsniegts;
    - f) lasītāja dzēšana, ja viņam ir izsniegumi.
28. Pievieno indeksu laukam, pēc kura meklēsi visbiežāk. Ar `EXPLAIN QUERY PLAN` parādi
    vaicājuma plānu pirms un pēc indeksa izveides un komentārā pamato izvēli.
29. ★ Uzraksti vaicājumu: kuri eksemplāri pašlaik ir izsniegti, kam un cik dienas.

**Mājasdarbs:** 26. un 27. uzdevums

## 12-034 · Vaicājumi un transakcijas
`[K]` `prakse` · `teorija.py` §8–§9

**Tēma:** Saliktie vaicājumi. Transakcijas.
**SR:** Raksta saliktus vaicājumus un lieto transakciju, kur darbības jāveic kopā.
**Standarts:** T.A.2.4.17.

**Gaita**
- 5' — kas notiek, ja naudas pārskaitījuma vidū pazūd strāva?
- 10' — demo §8: apakšvaicājums kā vērtība, saraksts un tabula
- 10' — demo §9: pasūtījums ar `BEGIN` / `COMMIT` / `ROLLBACK`, kad pietrūkst preces
- 15' — uzdevumi; kad transakcija tiešām vajadzīga

**Uzdevumi**

30. Apakšvaicājumi uz `skola.db`:
    - a) skolēni, kuru vidējā atzīme ir augstāka par visas skolas vidējo;
    - b) skolēni, kuri nav nevienā pulciņā;
    - c) priekšmets, kurā ir likts visvairāk atzīmju;
    - d) vidējais dalībnieku skaits pulciņos, kuros ir vismaz viens dalībnieks;
    - e) ★ katram skolēnam viņa pēdējās atzīmes datums un pati atzīme.
31. Bankas konti. Atmiņā (`":memory:"`) izveido tabulu
    `konti(id, ipasnieks, atlikums)` ar `CHECK (atlikums >= 0)` un divus kontus ar 100 €
    katrā. Uzraksti funkciju `kopsumma()`, kas atgriež visu kontu atlikumu summu.
32. Uzraksti funkciju `parskaitit_bez_transakcijas(no_id, uz_id, summa)`: divi `UPDATE`
    pēc kārtas, bet starp tiem `if summa > 50: raise RuntimeError("Strāva pazuda!")`.
    Izsauc to ar 80 €, noķer kļūdu un izdrukā kopsummu. Kur palika nauda?
33. Uzraksti funkciju `parskaitit(no_id, uz_id, summa)` ar `BEGIN` / `COMMIT` / `ROLLBACK`
    un tādu pašu «strāvas zudumu». Pārbaudi: kopsummai jāpaliek 200 €.
34. Mēģini pārskaitīt vairāk, nekā ir kontā. Kurš ierobežojums to aptur? Samaini abus
    `UPDATE` vietām (vispirms pieskaita, tad atņem) un pārbaudi vēlreiz: kas bez `ROLLBACK`
    notiktu ar otra konta atlikumu?
35. Kinoteātris. Atmiņā izveido tabulu `biletes` un uzraksti funkciju
    `nopirkt(seanss_id, vietas, epasts)`, kur `vietas` ir saraksts ar `(rinda, vieta)`.
    Vai nu tiek nopirktas visas biļetes, vai neviena. Funkcija atgriež `True` vai `False`.
    ```sql
    CREATE TABLE biletes (
        id        INTEGER PRIMARY KEY,
        seanss_id INTEGER NOT NULL,
        rinda     INTEGER NOT NULL CHECK (rinda BETWEEN 1 AND 10),
        vieta     INTEGER NOT NULL CHECK (vieta BETWEEN 1 AND 12),
        epasts    TEXT NOT NULL,
        UNIQUE (seanss_id, rinda, vieta)
    );
    ```
36. Pārbaudi: Anna pērk seansam 1 vietas (5, 7) un (5, 8). Pēc tam Kārlis pērk (5, 8) un
    (5, 9). Cik biļešu ir Kārlim? Vai vieta (5, 9) palika brīva? Pēc tam pamēģini nopirkt
    vietu (11, 1).
37. ★ Pieraksti savā sistēmā (18. uzdevums) vienu vietu, kur būs vajadzīga transakcija, un
    kāpēc.

**Mājasdarbs:** 35. un 36. uzdevums

## 12-035 · Sprints: sava datubāze
`[A]` `prakse` · `uzdevumi.py`

**Tēma:** Patstāvīgs darbs: datubāzes pabeigšana.
**SR:** Pabeidz datubāzi ar pilnu ierobežojumu komplektu un testa datiem.
**Standarts:** T.A.2.3.2.

**Uzdevumi**

38. Pārvērs savas sistēmas ER modeli (18. uzdevums, izlabots pēc 12-032) failā `shema.sql`:
    visas tabulas, primārās un ārējās atslēgas, `NOT NULL`, `UNIQUE`, vismaz viens `CHECK`
    un vismaz viens indekss ar komentāru, kāpēc tieši tur.
39. Uzraksti `dati.sql` ar testa datiem (vismaz pieci ieraksti katrā tabulā) un Python
    funkciju, kas datubāzi izveido no nulles no abiem failiem.
40. Uzraksti `vaicajumi.sql` ar desmit vaicājumiem, kas atbild uz reāliem jautājumiem par
    taviem datiem. Pirms katra vaicājuma komentārā uzraksti jautājumu. Starp tiem jābūt
    `JOIN`, `LEFT JOIN`, `GROUP BY` ar `HAVING` un apakšvaicājumam.
41. Uzraksti vienu Python funkciju ar transakciju — darbību, kurā divas vai vairākas
    izmaiņas jāveic kopā. Notestē gan veiksmīgu, gan neveiksmīgu gadījumu.
42. Katram ierobežojumam uzraksti vienu mēģinājumu ievadīt nederīgus datus, kas beidzas ar
    `IntegrityError`.
43. ★ Uzraksti vaicājumu, kas atrod datus, kuri pārkāpj kādu loģisku noteikumu, ko datubāze
    pati nepārbauda.

**Sprints:** `shema.sql`, `dati.sql`, `vaicajumi.sql` un izveides skripts repozitorijā

## 12-036 · Sprints: dokumentācija
`[A]` `prakse`

**Tēma:** Datubāzes dokumentēšana.
**SR:** Dokumentē datubāzes struktūru tā, lai to saprot cits izstrādātājs.
**Standarts:** T.A.2.4.7.

**Uzdevumi**

44. Uzraksti `DATUBAZE.md` pēc veidnes [`datubaze-veidne.md`](datubaze-veidne.md): ER
    modeļa attēls, tabulu apraksts, lauku nozīme.
45. Katrai tabulai pieraksti, kāpēc tā ir atsevišķa: kuru dublēšanos tā novērš.
46. Pieraksti katru `CHECK`, `UNIQUE` un indeksu un kāpēc tas vajadzīgs.
47. ★ Pieraksti, kas jāmaina, ja sistēmai pievienotu vēl vienu funkciju.

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

48. Aprēķini teksta jaucējvērtību un pārbaudi, ka vienādam tekstam tā vienmēr ir vienāda.
49. Nomaini vienu burtu un salīdzini rezultātu.
50. Pievieno savai datubāzei tabulu `lietotaji` ar jaucējvērtību, nevis paroli.
51. Uzraksti reģistrācijas un pieteikšanās funkcijas.
52. ★ Pievieno sāli un paskaidro komentārā, pret ko tā pasargā.

**Mājasdarbs:** 51. uzdevums

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

53. Uzraksti programmu, kas šifrē un atšifrē tekstu ar simetrisku atslēgu.
54. Pieraksti, kāpēc jaucējvērtību atšifrēt nevar, bet šifrētu tekstu — var.
55. Paskaidro, kā divi cilvēki var apmainīties ar noslēpumu, nekad nesatiekoties.
56. ★ Noskaidro, kā HTTPS izmanto abus šifrēšanas veidus, un pieraksti soļus.

**Mājasdarbs:** 55. uzdevums

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

57. Uzraksti apzināti ievainojamu vaicājumu un parādi, kā to izmantot.
58. Pārraksti to ar parametriem un pārbaudi, ka uzbrukums vairs nestrādā.
59. Pārbaudi savu projekta kodu: vai kaut kur vaicājums tiek salikts no virknēm?
60. ★ Pieraksti, kādus personas datus tava sistēma glabā un kāpēc katrs ir vajadzīgs.

**Mājasdarbs:** 58. uzdevums

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

61. Izveido serveri, kas atgriež datus no tavas datubāzes.
62. Pievieno žurnalēšanu: katrs pieprasījums tiek pierakstīts ar laiku un statusa kodu.
63. Pievieno maršrutu, kas atgriež datubāzes kopsavilkumu.
64. ★ Pievieno vienkāršu pieteikšanos, kas izmanto 12-037 jaucējvērtības.

**Mājasdarbs:** 62. uzdevums

## 12-041 · Sprints: serveris un drošība
`[A]` `prakse`

**Tēma:** Patstāvīgs darbs: droša servera daļa.
**SR:** Papildina serveri ar validāciju, kļūdu apstrādi un drošības pasākumiem.
**Standarts:** T.A.2.3.1. · T.A.3.1.2.

**Uzdevumi**

65. Pievieno visiem maršrutiem validāciju un pareizus statusa kodus.
66. Pārbaudi, ka kļūdas paziņojumos nav SQL vaicājumu vai failu ceļu.
67. Pārbaudi, ka visi vaicājumi ir parametrizēti.
68. ★ Pievieno ierobežojumu, cik pieprasījumu minūtē pieņem no viena klienta.

**Sprints:** serveris repozitorijā ar drošības pārbaudēm

## 12-042 · Sprints: servera dokumentācija
`[A]` `prakse`

**Tēma:** Servera dokumentēšana.
**SR:** Dokumentē servera maršrutus tā, lai citi tos var lietot.
**Standarts:** T.A.2.4.7.

**Uzdevumi**

69. Uzraksti `SERVERIS.md`: katram maršrutam metode, adrese, parametri, atbildes piemērs.
70. Pievieno palaišanas instrukciju no nulles.
71. ★ Pievieno kļūdu tabulu: kurā gadījumā kurš statusa kods.

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

72. Noskaidro sava datora IP adresi, apakštīkla masku, vārteju un DNS serveri.
73. Uzzīmē skolas kabineta tīkla shēmu ar ierīcēm un adresēm.
74. Pieraksti, ar ko atšķiras statiskā un dinamiskā IP adrese un kad kuru lieto.
75. ★ Noskaidro, cik ierīču var būt tīklā ar masku 255.255.255.0, un paskaidro, kāpēc.

**Mājasdarbs:** 74. uzdevums

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

76. Konfigurē bezvadu piekļuves punktu ar paroli un pieraksti soļus ar ekrānuzņēmumiem.
77. Pieraksti, ko dara MAC adrešu filtrs un kāpēc tas nav droša aizsardzība.
78. Pieraksti, kas ir portu pāradresācija un kādos gadījumos tā vajadzīga.
79. ★ Pieraksti piecas darbības, ko izdarītu ar jaunu maršrutētāju pirms tā lietošanas.

**Mājasdarbs:** 76. uzdevums

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

80. Palaid savu serveri tā, lai tas ir pieejams no cita datora lokālajā tīklā.
81. Pārbaudi to no klasesbiedra datora un pieraksti adresi.
82. Pieraksti, kādi riski rodas, atverot serveri, un ko izdarītu vispirms.
83. ★ Salīdzini sava servera uzturēšanu skolā un nomātu serveri: izmaksas, drošība,
    pieejamība, atbildība.

**Mājasdarbs:** 82. uzdevums

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

84. Aizpildi salīdzinājuma tabulu: savs serveris pret nomātu, pēc pieciem kritērijiem.
85. Izvēlies risinājumu savam projektam un pamato.
86. Pieraksti rezerves kopiju plānu: ko, cik bieži, kur, kā pārbaudi, ka tas strādā.
87. ★ Pieraksti, kas notiktu ar tavu sistēmu, ja serveris pazustu šodien.

**Mājasdarbs:** 86. uzdevums

## 12-047 · Sprints: tīkla dokumentācija
`[A]` `prakse`

**Tēma:** Tīkla konfigurācijas dokumentēšana.
**SR:** Dokumentē tīkla un servera konfigurāciju ar pierādījumiem.
**Standarts:** T.A.2.3.1. · T.A.2.4.7.

**Uzdevumi**

88. Uzraksti `TIKLS.md`: tīkla shēma, adresācija, maršrutētāja iestatījumi ar ekrānuzņēmumiem.
89. Pievieno sadaļu par drošību: kas darīts un kas apzināti nav darīts.
90. ★ Pievieno soļus, kā visu atjaunot no nulles.

**Sprints:** `TIKLS.md`

## 12-048 · Sprints: pašpārbaude
`[A]` `prakse`

**Tēma:** SV2 prasību pašpārbaude.
**SR:** Pārbauda savu darbu pret summatīvā darba prasībām.
**Standarts:** T.A.2.4.6.

**Uzdevumi**

91. Aizpildi pašpārbaudes tabulu pret SV2 prasībām.
92. Pieraksti, kas vēl jāizdara, un saplāno atlikušās stundas.
93. ★ Iedod savu dokumentāciju klasesbiedram un palūdz izpildīt vienu soli pēc tās.

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

94. Burtnīcā: uzzīmē ER modeli dotam aprakstam un pārvērs to tabulās.
95. Burtnīcā: uzraksti `CREATE TABLE` ar roku, ieskaitot atslēgas un ierobežojumus.
96. Burtnīcā: paskaidro, kāpēc parole datubāzē netiek glabāta atklātā tekstā.
97. ★ Burtnīcā: uzraksti vaicājumu ar `JOIN` un `GROUP BY` bez datora.

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

98. Izlasi SV2 prasības un uzraksti savu izpildes plānu.
99. Pieraksti, kura daļa būs grūtākā un ko darīsi, ja tā neizdodas.
100. ★ Pārbaudi, kuras prasības jau ir izpildītas sprintos.

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

101. Pabeidz `DATUBAZE.md`, `SERVERIS.md` un `TIKLS.md`.
102. Pievieno visus ekrānuzņēmumus un konfigurācijas fragmentus.
103. ★ Pārbaudi, vai svešs cilvēks pēc tavas dokumentācijas var visu atkārtot.

**Sprints:** pilna dokumentācija repozitorijā

## 12-054 · Sprints: pārbaude pirms iesniegšanas
`[A]` `prakse`

**Tēma:** Darba pārbaude pirms iesniegšanas.
**SR:** Pārbauda darba pilnīgumu pret prasībām.
**Standarts:** T.A.2.4.6.

**Uzdevumi**

104. Izpildi savu pašpārbaudes tabulu vēlreiz un atzīmē izmaiņas.
105. Pārbaudi, ka datubāzi var izveidot no nulles ar tavu skriptu.
106. ★ Notestē serveri ar nederīgiem datiem un pieraksti rezultātus.

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
  12-047) ir veltīti tieši dokumentēšanai, un galvenais darba fails ir markdown.
- **Situāciju krājumā ir vairāk, nekā var paspēt.** 12-031 un 12-032 klātienē pietiek ar
  vienu situāciju no katra veida (E, N1–N3, N4–N5, N6–N7) un kopīgi N8. Pārējās ir mājām,
  attālinātajām stundām un gatavojoties FV4 (12-049).
- **No ER modeļa uz kodu ved viens pavediens.** 12-031 bibliotēka uz papīra → 12-033 tā pati
  bibliotēka kā `biblioteka.sql` no Python. 12-031 kinoteātris → 12-032 normalizācija →
  12-034 biļešu pirkšana ar transakciju. 12-032 izvēlētā sava tēma → 12-035 sava datubāze →
  12-036 `DATUBAZE.md` → SV2.
- **SQL atkārtojums 12-033.** Pēc gada ar knex skolēni SQL sintaksi ir aizmirsuši. 20.–24.
  uzdevums ir uz jau zināmās `skola.db`, lai jāatceras tikai SQL, ne dati.
- **Divas SQLite īpatnības**, kas citādi aizņem pusi stundas: ārējās atslēgas pārbauda tikai
  pēc `PRAGMA foreign_keys = ON` (katram savienojumam), un bez `isolation_level=None`
  izmaiņas nesaglabājas, ja aizmirst `con.commit()`. `teorija.py` lieto `isolation_level=None`,
  lai transakcijas 12-034 būtu redzamas tieši kā SQL: `BEGIN` / `COMMIT` / `ROLLBACK`.
- **Maršrutētājs.** Ja kabinetā ir viens maršrutētājs, dari to kā demonstrāciju un ļauj
  skolēniem konfigurēt telefona karstvietu — standarts to tieši pieļauj. Svarīgākais, ko
  skolēnam saprast, ir noklusētās konfigurācijas maiņa un tas, ka atvērts ports ir risks.
- **SQL injekcija 12-039 ir jāparāda darbībā.** Uz savas testa datubāzes, ne uz kāda cita.
  Kad skolēns pats ieraksta `' OR '1'='1` un redz, ka pieteikšanās izdodas, parametrizēti
  vaicājumi vairs nav noteikums no grāmatas.
- **Normalizācija ir eksāmena 2. daļas serde.** ER modelis ar roku uz papīra (12-049) ir
  tieši tas formāts, kādā tas parādās eksāmenā.
