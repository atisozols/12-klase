# 02. Datortīkls, serveris un droša datubāze — darba fails

Šeit raksti savas atbildes. Uzdevumu numuri iet cauri visam blokam.

## 12-029 · Sprints: datu modeļa atkārtojums

**1.** Atver savu 11. klases `skola.db` un uzraksti piecus vaicājumus: viens ar `JOIN`, viens ar
`GROUP BY`, viens ar `LEFT JOIN`, viens ar `HAVING`, viens ar apakšvaicājumu.


---

**2.** Pieraksti katram, ko tas atbild un cik rindas atgriež.


---

**3.** ★ Uzraksti vaicājumu, kas apvieno trīs tabulas un divus nosacījumus.


---


## 12-030 · Sprints: kur datubāze nepietiek

**4.** Dotajā tabulā katrā rindā atkārtojas skolotāja vārds un e-pasts. Pieraksti trīs problēmas,
ko tas rada.


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


## 12-032 · Normalizācija

**11.** Dotajai tabulai atrodi 1NF pārkāpumu (vairākas vērtības vienā laukā) un izlabo.


---

**12.** Dotajai tabulai atrodi 2NF un 3NF pārkāpumus un sadali to.


---

**13.** Pārbaudi savu 12-031 modeli pret trim normālformām.


---

**14.** ★ Atrodi piemēru, kur dublēšanās ir apzināta izvēle, un pamato, kāpēc.


---


## 12-033 · Datubāzes izveide

**15.** Realizē savu 12-031 modeli kā `shema.sql` ar visām atslēgām un ierobežojumiem.


---

**16.** Pievieno indeksu laukam, pēc kura meklēsi visbiežāk, un pamato izvēli.


---

**17.** Ievieto testa datus: vismaz pieci ieraksti katrā tabulā.


---

**18.** Pārbaudi, ka ierobežojumi tiešām neļauj ievadīt nederīgus datus.


---

**19.** ★ Uzraksti skriptu, kas datubāzi izdzēš un izveido no jauna vienā palaišanā.


---


## 12-034 · Vaicājumi un transakcijas

**20.** Uzraksti vaicājumu ar apakšvaicājumu: ieraksti, kuru vērtība ir virs vidējās.


---

**21.** Uzraksti darbību pāri, kas jāveic kopā, un ietver to transakcijā.


---

**22.** Izmēģini `ROLLBACK` un pārbaudi, ka izmaiņas atceltas.


---

**23.** ★ Pieraksti savā projektā vietu, kur transakcija būs vajadzīga.


---


## 12-035 · Sprints: sava datubāze

**24.** Pabeidz savu datubāzi: visas tabulas, atslēgas, ierobežojumi, indeksi.


---

**25.** Uzraksti desmit vaicājumus, kas atbild uz reāliem jautājumiem par taviem datiem.


---

**26.** ★ Uzraksti vaicājumu, kas atrod datus, kuri pārkāpj kādu loģisku noteikumu, ko datubāze
pati nepārbauda.


---


## 12-036 · Sprints: dokumentācija

**27.** Uzraksti `DATUBAZE.md`: ER modeļa attēls, tabulu apraksts, lauku nozīme.


---

**28.** Katrai tabulai pieraksti, kāpēc tā ir atsevišķa.


---

**29.** ★ Pieraksti, kas jāmaina, ja sistēmai pievienotu vēl vienu funkciju.


---


## 12-037 · Kriptogrāfija: jaucējfunkcijas

**30.** Aprēķini teksta jaucējvērtību un pārbaudi, ka vienādam tekstam tā vienmēr ir vienāda.


---

**31.** Nomaini vienu burtu un salīdzini rezultātu.


---

**32.** Pievieno savai datubāzei tabulu `lietotaji` ar jaucējvērtību, nevis paroli.


---

**33.** Uzraksti reģistrācijas un pieteikšanās funkcijas.


---

**34.** ★ Pievieno sāli un paskaidro komentārā, pret ko tā pasargā.


---


## 12-038 · Simetriskā un asimetriskā šifrēšana

**35.** Uzraksti programmu, kas šifrē un atšifrē tekstu ar simetrisku atslēgu.


---

**36.** Pieraksti, kāpēc jaucējvērtību atšifrēt nevar, bet šifrētu tekstu — var.


---

**37.** Paskaidro, kā divi cilvēki var apmainīties ar noslēpumu, nekad nesatiekoties.


---

**38.** ★ Noskaidro, kā HTTPS izmanto abus šifrēšanas veidus, un pieraksti soļus.


---


## 12-039 · Datu drošība datubāzē

**39.** Uzraksti apzināti ievainojamu vaicājumu un parādi, kā to izmantot.


---

**40.** Pārraksti to ar parametriem un pārbaudi, ka uzbrukums vairs nestrādā.


---

**41.** Pārbaudi savu projekta kodu: vai kaut kur vaicājums tiek salikts no virknēm?


---

**42.** ★ Pieraksti, kādus personas datus tava sistēma glabā un kāpēc katrs ir vajadzīgs.


---


## 12-040 · Serveris izstrādātāja vajadzībām

**43.** Izveido serveri, kas atgriež datus no tavas datubāzes.


---

**44.** Pievieno žurnalēšanu: katrs pieprasījums tiek pierakstīts ar laiku un statusa kodu.


---

**45.** Pievieno maršrutu, kas atgriež datubāzes kopsavilkumu.


---

**46.** ★ Pievieno vienkāršu pieteikšanos, kas izmanto 12-037 jaucējvērtības.


---


## 12-041 · Sprints: serveris un drošība

**47.** Pievieno visiem maršrutiem validāciju un pareizus statusa kodus.


---

**48.** Pārbaudi, ka kļūdas paziņojumos nav SQL vaicājumu vai failu ceļu.


---

**49.** Pārbaudi, ka visi vaicājumi ir parametrizēti.


---

**50.** ★ Pievieno ierobežojumu, cik pieprasījumu minūtē pieņem no viena klienta.


---


## 12-042 · Sprints: servera dokumentācija

**51.** Uzraksti `SERVERIS.md`: katram maršrutam metode, adrese, parametri, atbildes piemērs.


---

**52.** Pievieno palaišanas instrukciju no nulles.


---

**53.** ★ Pievieno kļūdu tabulu: kurā gadījumā kurš statusa kods.


---


## 12-043 · Datortīkla uzbūve

**54.** Noskaidro sava datora IP adresi, apakštīkla masku, vārteju un DNS serveri.


---

**55.** Uzzīmē skolas kabineta tīkla shēmu ar ierīcēm un adresēm.


---

**56.** Pieraksti, ar ko atšķiras statiskā un dinamiskā IP adrese un kad kuru lieto.


---

**57.** ★ Noskaidro, cik ierīču var būt tīklā ar masku 255.255.255.0, un paskaidro, kāpēc.


---


## 12-044 · Maršrutētāja konfigurācija

**58.** Konfigurē bezvadu piekļuves punktu ar paroli un pieraksti soļus ar ekrānuzņēmumiem.


---

**59.** Pieraksti, ko dara MAC adrešu filtrs un kāpēc tas nav droša aizsardzība.


---

**60.** Pieraksti, kas ir portu pāradresācija un kādos gadījumos tā vajadzīga.


---

**61.** ★ Pieraksti piecas darbības, ko izdarītu ar jaunu maršrutētāju pirms tā lietošanas.


---


## 12-045 · Servera pieejamība tīklā

**62.** Palaid savu serveri tā, lai tas ir pieejams no cita datora lokālajā tīklā.


---

**63.** Pārbaudi to no klasesbiedra datora un pieraksti adresi.


---

**64.** Pieraksti, kādi riski rodas, atverot serveri, un ko izdarītu vispirms.


---

**65.** ★ Salīdzini sava servera uzturēšanu skolā un nomātu serveri: izmaksas, drošība,
pieejamība, atbildība.


---


## 12-046 · Servera uzturēšana

**66.** Aizpildi salīdzinājuma tabulu: savs serveris pret nomātu, pēc pieciem kritērijiem.


---

**67.** Izvēlies risinājumu savam projektam un pamato.


---

**68.** Pieraksti rezerves kopiju plānu: ko, cik bieži, kur, kā pārbaudi, ka tas strādā.


---

**69.** ★ Pieraksti, kas notiktu ar tavu sistēmu, ja serveris pazustu šodien.


---


## 12-047 · Sprints: tīkla dokumentācija

**70.** Uzraksti `TIKLS.md`: tīkla shēma, adresācija, maršrutētāja iestatījumi ar ekrānuzņēmumiem.


---

**71.** Pievieno sadaļu par drošību: kas darīts un kas apzināti nav darīts.


---

**72.** ★ Pievieno soļus, kā visu atjaunot no nulles.


---


## 12-048 · Sprints: pašpārbaude

**73.** Aizpildi pašpārbaudes tabulu pret SV2 prasībām.


---

**74.** Pieraksti, kas vēl jāizdara, un saplāno atlikušās stundas.


---

**75.** ★ Iedod savu dokumentāciju klasesbiedram un palūdz izpildīt vienu soli pēc tās.


---


## 12-049 · Jēdzieni un atkārtojums

**76.** Burtnīcā: uzzīmē ER modeli dotam aprakstam un pārvērs to tabulās.


---

**77.** Burtnīcā: uzraksti `CREATE TABLE` ar roku, ieskaitot atslēgas un ierobežojumus.


---

**78.** Burtnīcā: paskaidro, kāpēc parole datubāzē netiek glabāta atklātā tekstā.


---

**79.** ★ Burtnīcā: uzraksti vaicājumu ar `JOIN` un `GROUP BY` bez datora.


---


## 12-050 · SV2 uzdevuma izsniegšana

**80.** Izlasi SV2 prasības un uzraksti savu izpildes plānu.


---

**81.** Pieraksti, kura daļa būs grūtākā un ko darīsi, ja tā neizdodas.


---

**82.** ★ Pārbaudi, kuras prasības jau ir izpildītas sprintos.


---


## 12-053 · Sprints: dokumentācijas pabeigšana

**83.** Pabeidz `DATUBAZE.md`, `SERVERIS.md` un `TIKLS.md`.


---

**84.** Pievieno visus ekrānuzņēmumus un konfigurācijas fragmentus.


---

**85.** ★ Pārbaudi, vai svešs cilvēks pēc tavas dokumentācijas var visu atkārtot.


---


## 12-054 · Sprints: pārbaude pirms iesniegšanas

**86.** Izpildi savu pašpārbaudes tabulu vēlreiz un atzīmē izmaiņas.


---

**87.** Pārbaudi, ka datubāzi var izveidot no nulles ar tavu skriptu.


---

**88.** ★ Notestē serveri ar nederīgiem datiem un pieraksti rezultātus.


---
