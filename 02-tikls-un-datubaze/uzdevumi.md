# 02. Datortīkls, serveris un droša datubāze — darba fails

Šeit raksti savas atbildes. Uzdevumu numuri iet cauri visam blokam.

Programmēšanas stundu uzdevumi ir [`uzdevumi.py`](uzdevumi.py).

## 12-029 · Sprints: datu modeļa atkārtojums

**1.** Atver savu 11. klases `skola.db` un uzraksti piecus vaicājumus: viens ar `JOIN`, viens ar
`GROUP BY`, viens ar `LEFT JOIN`, viens ar `HAVING`, viens ar apakšvaicājumu.


---

**2.** Pieraksti katram, ko tas atbild un cik rindas atgriež.


---

**3.** ★ Uzraksti vaicājumu, kas apvieno trīs tabulas un divus nosacījumus.


---


## 12-030 · Sprints: kur datubāze nepietiek

**4.** Situāciju krājuma ([`situacijas.md`](situacijas.md)) tabulā **N0** katrā rindā atkārtojas
skolotāja vārds un e-pasts. Pieraksti trīs problēmas, ko tas rada.


---

**5.** Pārprojektē šo tabulu divās un pieraksti, kas mainījās.


---

**6.** ★ Atrodi savā 11. klases projekta datubāzē vietu, kur dati atkārtojas.


---


## 12-031 · ER modelis

**7.** Uzzīmē ER modeli skolas bibliotēkai (grāmata, eksemplārs, lasītājs, izsniegums).


---

**8.** Atzīmē katras saistības kardinalitāti un pamato.


---

**9.** Pārvērs savu ER modeli tabulās un pieraksti, kur radās starptabula.


---

**10.** ★ Uzzīmē ER modeli sistēmai, kurā viena entītija saistās pati ar sevi (piemēram,
darbinieks un viņa vadītājs).


---

**11.** Uzzīmē ER modeli kinoteātra biļešu sistēmai: filmas, zāles, seansi, vietas, biļetes,
pircēji. Pārvērs to tabulās.


---

**12.** ★ Situāciju krājumā izvēlies divas situācijas no E1–E8 un uzzīmē to ER modeļus.


---


## 12-032 · Normalizācija

**13.** Situāciju krājumā **N1**, **N2**, **N3**: atrodi 1NF pārkāpumu un sadali tabulu.


---

**14.** **N4** un **N5**: nosaki primāro atslēgu, atrodi laukus, kas atkarīgi tikai no tās daļas,
un sadali tabulu.


---

**15.** **N6** un **N7**: atrodi 3NF pārkāpumu un sadali tabulu. Pie N7 pamato, vai reālā
sistēmā to sadalītu.


---

**16.** **N8**: izpildi visus sešus soļus — no Excel lapas līdz 3NF un ER modelim.


---

**17.** Pārbaudi savu kinoteātra modeli (11. uzdevums) pret trim normālformām un izlabo.


---

**18.** Izvēlies savas sistēmas tēmu: šo datubāzi tu veidosi 12-035 sprintā un nodosi SV2
darbā. Uzraksti divu teikumu aprakstu un uzzīmē ER skici: vismaz četras entītijas,
tostarp viena N:M saistība.


---

**19.** ★ **N9** un **N10**.


---


## 12-036 · Sprints: dokumentācija

**44.** Uzraksti `DATUBAZE.md` pēc veidnes [`datubaze-veidne.md`](datubaze-veidne.md): ER
modeļa attēls, tabulu apraksts, lauku nozīme.


---

**45.** Katrai tabulai pieraksti, kāpēc tā ir atsevišķa: kuru dublēšanos tā novērš.


---

**46.** Pieraksti katru `CHECK`, `UNIQUE` un indeksu un kāpēc tas vajadzīgs.


---

**47.** ★ Pieraksti, kas jāmaina, ja sistēmai pievienotu vēl vienu funkciju.


---


## 12-037 · Kriptogrāfija: jaucējfunkcijas

**48.** Aprēķini teksta jaucējvērtību un pārbaudi, ka vienādam tekstam tā vienmēr ir vienāda.


---

**49.** Nomaini vienu burtu un salīdzini rezultātu.


---

**50.** Pievieno savai datubāzei tabulu `lietotaji` ar jaucējvērtību, nevis paroli.


---

**51.** Uzraksti reģistrācijas un pieteikšanās funkcijas.


---

**52.** ★ Pievieno sāli un paskaidro komentārā, pret ko tā pasargā.


---


## 12-038 · Simetriskā un asimetriskā šifrēšana

**53.** Uzraksti programmu, kas šifrē un atšifrē tekstu ar simetrisku atslēgu.


---

**54.** Pieraksti, kāpēc jaucējvērtību atšifrēt nevar, bet šifrētu tekstu — var.


---

**55.** Paskaidro, kā divi cilvēki var apmainīties ar noslēpumu, nekad nesatiekoties.


---

**56.** ★ Noskaidro, kā HTTPS izmanto abus šifrēšanas veidus, un pieraksti soļus.


---


## 12-039 · Datu drošība datubāzē

**57.** Uzraksti apzināti ievainojamu vaicājumu un parādi, kā to izmantot.


---

**58.** Pārraksti to ar parametriem un pārbaudi, ka uzbrukums vairs nestrādā.


---

**59.** Pārbaudi savu projekta kodu: vai kaut kur vaicājums tiek salikts no virknēm?


---

**60.** ★ Pieraksti, kādus personas datus tava sistēma glabā un kāpēc katrs ir vajadzīgs.


---


## 12-040 · Serveris izstrādātāja vajadzībām

**61.** Izveido serveri, kas atgriež datus no tavas datubāzes.


---

**62.** Pievieno žurnalēšanu: katrs pieprasījums tiek pierakstīts ar laiku un statusa kodu.


---

**63.** Pievieno maršrutu, kas atgriež datubāzes kopsavilkumu.


---

**64.** ★ Pievieno vienkāršu pieteikšanos, kas izmanto 12-037 jaucējvērtības.


---


## 12-041 · Sprints: serveris un drošība

**65.** Pievieno visiem maršrutiem validāciju un pareizus statusa kodus.


---

**66.** Pārbaudi, ka kļūdas paziņojumos nav SQL vaicājumu vai failu ceļu.


---

**67.** Pārbaudi, ka visi vaicājumi ir parametrizēti.


---

**68.** ★ Pievieno ierobežojumu, cik pieprasījumu minūtē pieņem no viena klienta.


---


## 12-042 · Sprints: servera dokumentācija

**69.** Uzraksti `SERVERIS.md`: katram maršrutam metode, adrese, parametri, atbildes piemērs.


---

**70.** Pievieno palaišanas instrukciju no nulles.


---

**71.** ★ Pievieno kļūdu tabulu: kurā gadījumā kurš statusa kods.


---


## 12-043 · Datortīkla uzbūve

**72.** Noskaidro sava datora IP adresi, apakštīkla masku, vārteju un DNS serveri.


---

**73.** Uzzīmē skolas kabineta tīkla shēmu ar ierīcēm un adresēm.


---

**74.** Pieraksti, ar ko atšķiras statiskā un dinamiskā IP adrese un kad kuru lieto.


---

**75.** ★ Noskaidro, cik ierīču var būt tīklā ar masku 255.255.255.0, un paskaidro, kāpēc.


---


## 12-044 · Maršrutētāja konfigurācija

**76.** Konfigurē bezvadu piekļuves punktu ar paroli un pieraksti soļus ar ekrānuzņēmumiem.


---

**77.** Pieraksti, ko dara MAC adrešu filtrs un kāpēc tas nav droša aizsardzība.


---

**78.** Pieraksti, kas ir portu pāradresācija un kādos gadījumos tā vajadzīga.


---

**79.** ★ Pieraksti piecas darbības, ko izdarītu ar jaunu maršrutētāju pirms tā lietošanas.


---


## 12-045 · Servera pieejamība tīklā

**80.** Palaid savu serveri tā, lai tas ir pieejams no cita datora lokālajā tīklā.


---

**81.** Pārbaudi to no klasesbiedra datora un pieraksti adresi.


---

**82.** Pieraksti, kādi riski rodas, atverot serveri, un ko izdarītu vispirms.


---

**83.** ★ Salīdzini sava servera uzturēšanu skolā un nomātu serveri: izmaksas, drošība,
pieejamība, atbildība.


---


## 12-046 · Servera uzturēšana

**84.** Aizpildi salīdzinājuma tabulu: savs serveris pret nomātu, pēc pieciem kritērijiem.


---

**85.** Izvēlies risinājumu savam projektam un pamato.


---

**86.** Pieraksti rezerves kopiju plānu: ko, cik bieži, kur, kā pārbaudi, ka tas strādā.


---

**87.** ★ Pieraksti, kas notiktu ar tavu sistēmu, ja serveris pazustu šodien.


---


## 12-047 · Sprints: tīkla dokumentācija

**88.** Uzraksti `TIKLS.md`: tīkla shēma, adresācija, maršrutētāja iestatījumi ar ekrānuzņēmumiem.


---

**89.** Pievieno sadaļu par drošību: kas darīts un kas apzināti nav darīts.


---

**90.** ★ Pievieno soļus, kā visu atjaunot no nulles.


---


## 12-048 · Sprints: pašpārbaude

**91.** Aizpildi pašpārbaudes tabulu pret SV2 prasībām.


---

**92.** Pieraksti, kas vēl jāizdara, un saplāno atlikušās stundas.


---

**93.** ★ Iedod savu dokumentāciju klasesbiedram un palūdz izpildīt vienu soli pēc tās.


---


## 12-049 · Jēdzieni un atkārtojums

**94.** Burtnīcā: uzzīmē ER modeli dotam aprakstam un pārvērs to tabulās.


---

**95.** Burtnīcā: uzraksti `CREATE TABLE` ar roku, ieskaitot atslēgas un ierobežojumus.


---

**96.** Burtnīcā: paskaidro, kāpēc parole datubāzē netiek glabāta atklātā tekstā.


---

**97.** ★ Burtnīcā: uzraksti vaicājumu ar `JOIN` un `GROUP BY` bez datora.


---


## 12-050 · SV2 uzdevuma izsniegšana

**98.** Izlasi SV2 prasības un uzraksti savu izpildes plānu.


---

**99.** Pieraksti, kura daļa būs grūtākā un ko darīsi, ja tā neizdodas.


---

**100.** ★ Pārbaudi, kuras prasības jau ir izpildītas sprintos.


---


## 12-053 · Sprints: dokumentācijas pabeigšana

**101.** Pabeidz `DATUBAZE.md`, `SERVERIS.md` un `TIKLS.md`.


---

**102.** Pievieno visus ekrānuzņēmumus un konfigurācijas fragmentus.


---

**103.** ★ Pārbaudi, vai svešs cilvēks pēc tavas dokumentācijas var visu atkārtot.


---


## 12-054 · Sprints: pārbaude pirms iesniegšanas

**104.** Izpildi savu pašpārbaudes tabulu vēlreiz un atzīmē izmaiņas.


---

**105.** Pārbaudi, ka datubāzi var izveidot no nulles ar tavu skriptu.


---

**106.** ★ Notestē serveri ar nederīgiem datiem un pieraksti rezultātus.


---
