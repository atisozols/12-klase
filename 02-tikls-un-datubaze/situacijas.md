# 02. bloks — situāciju krājums

ER modeļi un normalizācija dažādās situācijās. Uzdevumos atsaucamies uz tām pēc koda,
piemēram **E3** vai **N5**. Atbildes raksti [`uzdevumi.md`](uzdevumi.md) vai burtnīcā.

Atgādne: [`teorija.md`](teorija.md) §1 (ER modelis) un §2 (normalizācija).

| Daļa | Kas jādara | Situācijas |
| --- | --- | --- |
| A | No apraksta uz ER modeli | E1–E8 |
| B | No tabulām uz ER modeli | R1 |
| C | Atrodi projektēšanas kļūdu | K1–K4 |
| D | Normalizācija | N0–N10 |

★ — grūtāka situācija.

---

## A. No apraksta uz ER modeli

Katrai situācijai: **(1)** atrodi entītijas (lietvārdi, par kuriem jāglabā dati),
**(2)** katrai entītijai pieraksti atribūtus, **(3)** novelc saistības un atzīmē
kardinalitāti, **(4)** pārvērs modeli tabulās ar primārajām un ārējām atslēgām.
Pēc tam atbildi uz jautājumiem.

### E1 · Veterinārā klīnika

> Klīnikā strādā vairāki ārsti. Katram dzīvnieka saimniekam ir vārds, tālrunis un e-pasts.
> Saimniekam var būt vairāki dzīvnieki; katram dzīvniekam ir vārds, suga un dzimšanas gads.
> Kad dzīvnieks atnāk uz vizīti, pieraksta datumu, ārstu, kas to pieņēma, diagnozi un
> samaksāto summu.

- Kāda ir saistība starp ārstu un dzīvnieku? Kura entītija tos savieno?
- Vai šai saistībai vajadzīga vēl viena, atsevišķa starptabula? Kāpēc?

### E2 · Ēdienu piegāde

> Platformā ir restorāni ar nosaukumu un adresi. Katram restorānam ir sava ēdienkarte —
> ēdieni ar nosaukumu un cenu. Klients pasūta no viena restorāna vairākus ēdienus, katru
> noteiktā daudzumā. Pasūtījumu piegādā kurjers; kurjers dienā piegādā daudzus pasūtījumus.
> Pasūtījumam pieraksta laiku un piegādes adresi.

- Kurā tabulā glabājas ēdiena daudzums? Kāpēc ne tabulā `edieni` un ne tabulā `pasutijumi`?
- Vai tavs modelis ļauj vienā pasūtījumā ielikt ēdienus no diviem restorāniem? Kā to
  varētu aizliegt?

### E3 · Skolas stundu saraksts

> Skolā ir klases, skolotāji, priekšmeti un kabineti. Stundu sarakstā katrai stundai ir
> nedēļas diena un stundas numurs (1.–8.). Katrā stundā viena klase mācās vienu priekšmetu
> pie viena skolotāja vienā kabinetā. Viens skolotājs var mācīt vairākus priekšmetus.

- Ar cik citām entītijām saistās «stunda»?
- Kādi `UNIQUE` ierobežojumi neļautu (a) divām klasēm vienlaikus būt vienā kabinetā,
  (b) skolotājam vienlaikus būt divās stundās?

### E4 · Mūzikas straumēšana

> Lietotāji klausās dziesmas. Dziesmai ir nosaukums un garums sekundēs, un tā pieder vienam
> albumam. Albumam ir nosaukums un izdošanas gads. Dziesmu var izpildīt vairāki izpildītāji
> kopā. Lietotājs veido atskaņošanas sarakstus; sarakstā dziesmas ir noteiktā secībā, un
> viena dziesma var būt daudzos sarakstos. Sistēma pieraksta katru noklausīšanos ar laiku.

- Cik starptabulu ir tavā modelī? Nosauc katru.
- Kur glabājas informācija par to, kurā vietā sarakstā ir dziesma?

### E5 · Pilsētas velosipēdu noma

> Pilsētā ir nomas stacijas ar nosaukumu, adresi un vietu skaitu. Katram velosipēdam ir
> numurs un tips (parastais vai elektriskais). Lietotājs paņem velosipēdu vienā stacijā un
> atstāj to citā. Braucienam pieraksta sākuma un beigu laiku, sākuma un beigu staciju un
> samaksu.

- Starp braucienu un staciju ir **divas** saistības. Kā tās izskatās tabulā?
- Kā uzzināt, kurā stacijā velosipēds atrodas tagad? Vai to vajag glabāt atsevišķā laukā?

### E6 · Viesnīca

> Viesnīcā ir istabas ar numuru, stāvu un tipu (vienvietīga, divvietīga, lukss). Cena par
> nakti ir atkarīga no tipa, nevis no konkrētās istabas. Viesis rezervē istabu uz noteiktiem
> datumiem (no–līdz). Rezervācijai var pievienot papildpakalpojumus (brokastis, autostāvvieta,
> SPA), katru vienu vai vairākas reizes.

- Kāpēc istabas tips ir atsevišķa entītija, nevis teksta lauks istabai?
- Vai ar `CHECK` vai `UNIQUE` var aizliegt divas pārklājošās rezervācijas vienai istabai?
  Ja nevar, kur šo pārbaudi jāliek?

### E7 · ★ Futbola līga

> Līgā spēlē komandas. Spēlētājs pašlaik spēlē vienā komandā, bet līga grib zināt arī, kurās
> komandās viņš spēlējis agrāk un kurā laika posmā. Katrā spēlē piedalās divas komandas —
> mājinieki un viesi. Spēlē pieraksta vārtus: kurš spēlētājs, kurā minūtē.

- Kā attēlot spēlētāja komandu vēsturi? Vai `komanda_id` tabulā `speletaji` pietiek?
- Kā spēle saistās ar komandām? Kāds `CHECK` neļautu komandai spēlēt pašai pret sevi?

### E8 · ★ Sociālais tīkls

> Lietotāji publicē ierakstus. Citi lietotāji var komentēt ierakstus un atzīmēt «patīk»
> ierakstiem. Lietotājs var sekot citiem lietotājiem; sekošana nav abpusēja. Uz komentāru
> var atbildēt ar citu komentāru.

- Modelī ir divas saistības, kurās entītija saistās pati ar sevi. Kuras?
- Kāds `UNIQUE` neļautu vienam lietotājam atzīmēt «patīk» vienam ierakstam divreiz?

---

## B. No tabulām uz ER modeli

### R1 · Picērija

```
picerijas(id, nosaukums, adrese)
kurjeri(id, vards, picerija_id → picerijas)
picas(id, nosaukums, cena)
klienti(id, vards, talrunis)
pasutijumi(id, klients_id → klienti, kurjers_id → kurjeri, laiks)
pasutijuma_picas(pasutijums_id → pasutijumi, pica_id → picas, skaits)
```

- Uzzīmē ER modeli un atzīmē visas kardinalitātes.
- Kura tabula ir starptabula? Kuru N:M saistību tā attēlo?
- Ko šis modelis **nevar** attēlot? (Padomā: vai visās picērijās ir visas picas par vienu
  cenu?)

---

## C. Kas te nav kārtībā?

Katrai tabulai: ko šī shēma **nevar** attēlot vai kas tajā var noiet greizi? Kā to
izlabotu?

**K1.** `skoleni(id, vards, uzvards, pulcins_id → pulcini)`

**K2.** `gramatas(id, nosaukums, autors, lasitajs_id → lasitaji, izsniegts)`
— grāmatas tabulā glabājas, kam tā pašlaik izsniegta.

**K3.** `pasutijumi(id, klients, prece1, daudzums1, prece2, daudzums2, prece3, daudzums3)`

**K4.** ★ `draudzibas(lietotajs1_id, lietotajs2_id)` — draudzība ir abpusēja. Tabulā ir
rindas `(1, 2)` un `(2, 1)`. Kāda problēma? Kāds `CHECK` to novērstu?

---

## D. Normalizācija

Katrai tabulai: **(1)** kas ir primārā atslēga? **(2)** kura normālforma pārkāpta un kur?
**(3)** sadali tabulu tā, lai pārkāpuma vairs nav, un pieraksti jaunās tabulas ar atslēgām.

Soli pa solim metode ir [`teorija.md`](teorija.md) §2.

### N0 · Stundu žurnāls *(12-030)*

| datums | klase | prieksmets | skolotajs | skolotaja_epasts |
| --- | --- | --- | --- | --- |
| 2026-10-05 | 12.a | Programmēšana | A. Kalniņa | a.kalnina@skola.lv |
| 2026-10-05 | 12.b | Programmēšana | A. Kalniņa | a.kalnina@skola.lv |
| 2026-10-06 | 12.a | Fizika | J. Ozols | j.ozols@skola.lv |
| 2026-10-07 | 11.a | Programmēšana | A. Kalniņa | a.kalnina@skola.ly |
| 2026-10-07 | 12.a | Matemātika | L. Bērziņa | l.berzina@skola.lv |

### 1NF — vienā laukā viena vērtība

#### N1 · Pulciņi

| id | nosaukums | skolotajs | dalibnieki |
| --- | --- | --- | --- |
| 1 | Robotika | A. Kalniņa | Jānis Ozols, Līga Bērziņa, Marta Liepa |
| 2 | Teātris | R. Zariņš | Līga Bērziņa |
| 3 | Šahs | A. Kalniņa | Pēteris Krūmiņš, Jānis Ozols |

Kā ar šo tabulu uzzinātu, kuros pulciņos ir Līga? Cik pulciņos ir Jānis?

#### N2 · Kontakti

| id | vards | telefons1 | telefons2 | telefons3 |
| --- | --- | --- | --- | --- |
| 1 | Anna | 26123456 | 29876543 | |
| 2 | Kārlis | 20011223 | | |
| 3 | Līga | 26555111 | 67123456 | 29000111 |

Katrā laukā ir viena vērtība — formāli viss kārtībā. Kāpēc tā tomēr ir 1NF problēma? Kas
notiek, ja kādam ir četri tālruņi? Kā atrast, kam pieder numurs 29876543?

#### N3 · Pasūtījumi

| pasutijums | klients | datums | preces |
| --- | --- | --- | --- |
| 101 | Anna | 2026-10-20 | Maize x2, Piens x1 |
| 102 | Kārlis | 2026-10-21 | Kafija x1 |
| 103 | Anna | 2026-10-22 | Piens x3, Siers x1, Maize x1 |

Cik piena kopā pārdots? Kāpēc to ir grūti uzzināt ar SQL?

### 2NF — viss atkarīgs no visas atslēgas

2NF problēma var rasties tikai tad, ja primārā atslēga sastāv no **vairākiem** laukiem.

#### N4 · Atzīmes

Primārā atslēga: `(skolens_id, prieksmets_id, datums)`.

| skolens_id | prieksmets_id | datums | atzime | skolena_vards | skolena_klase | prieksmeta_nosaukums |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 1 | 2026-10-01 | 8 | Jānis Ozols | 12.a | Programmēšana |
| 5 | 2 | 2026-10-02 | 6 | Jānis Ozols | 12.a | Matemātika |
| 7 | 1 | 2026-10-01 | 9 | Līga Bērziņa | 12.b | Programmēšana |
| 5 | 1 | 2026-10-08 | 7 | Jānis Ozols | 12.a | Programmēšana |

Kuri lauki ir atkarīgi tikai no atslēgas **daļas**? No kuras daļas?

#### N5 · Kino biļetes

Primārā atslēga: `(seanss_id, rinda, vieta)`.

| seanss_id | rinda | vieta | filma | zale | sakums | cena | pirceja_epasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 5 | 7 | Straume | 2 | 2026-11-06 19:00 | 7.50 | anna@epasts.lv |
| 12 | 5 | 8 | Straume | 2 | 2026-11-06 19:00 | 7.50 | anna@epasts.lv |
| 12 | 6 | 1 | Straume | 2 | 2026-11-06 19:00 | 7.50 | karlis@epasts.lv |
| 13 | 1 | 1 | Dvēseļu putenis | 1 | 2026-11-06 17:00 | 6.00 | liga@epasts.lv |

- Kuri lauki atkarīgi tikai no `seanss_id`?
- Lauks `cena`: atkarīgs no seansa vai no vietas? Atbilde ir atkarīga no biznesa
  noteikuma. Uzraksti abus variantus un sadali tabulu katram.

### 3NF — nekas nav atkarīgs no ne-atslēgas lauka

#### N6 · Darbinieki

| id | vards | nodala | nodalas_vaditajs | nodalas_stavs |
| --- | --- | --- | --- | --- |
| 1 | Anna | IT | M. Liepa | 3 |
| 2 | Kārlis | IT | M. Liepa | 3 |
| 3 | Līga | Grāmatvedība | R. Zariņš | 2 |
| 4 | Pēteris | IT | M. Liepa | 3 |

Uzņēmumā izveido jaunu nodaļu «Mārketings» ar vadītāju, bet darbinieku tajā vēl nav. Kur to
ierakstīt?

#### N7 · Klientu adreses

| id | vards | iela | pasta_indekss | pilseta |
| --- | --- | --- | --- | --- |
| 1 | Anna | Raiņa iela 7 | LV-3101 | Tukums |
| 2 | Kārlis | Pils iela 3 | LV-3101 | Tukums |
| 3 | Līga | Brīvības iela 12 | LV-1010 | Rīga |
| 4 | Pēteris | Talsu iela 1 | LV-3101 | Tukum |

- Kurš lauks ir atkarīgs no cita ne-atslēgas lauka?
- Vai **tu** šo tabulu sadalītu? Lielākā daļa reālu sistēmu to nedara. Kāpēc?

### Visas trīs kopā

#### N8 · Autoskolas braukšanas nodarbības

Autoskola nodarbības līdz šim uzskaitīja Excel lapā:

| datums | audzeknis | audz_talrunis | instruktors | instr_talrunis | auto | auto_modelis | veids | cena |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-01 | Roberts Kalniņš | 26100001 | J. Vanags | 29200002 | KA-1234 | Toyota Yaris | pilsēta | 25 |
| 2026-10-01 | Marta Liepa | 26100003 | J. Vanags | 29200002 | KA-1234 | Toyota Yaris | laukums | 20 |
| 2026-10-02 | Roberts Kalniņš | 26100001 | I. Celma | 29200004 | LB-777 | VW Polo | šoseja | 30 |
| 2026-10-03 | Roberts Kalniņš | 26100001 | J. Vanags | 29200009 | KA-1234 | Toyota Yaris | pilsēta | 25 |
| 2026-10-03 | Emīls Ozols | 26100005, 26100006 | I. Celma | 29200004 | LB-777 | VW Polo | pilsēta | 25 |

1. Atrodi 1NF pārkāpumu.
2. Pieraksti katru atkarību formā `A → B` («ja zinu A, zinu arī B»).
3. Sadali līdz 3NF un uzzīmē ER modeli jaunajām tabulām.
4. Atrodi tabulā vienu **atjaunināšanas** anomāliju, kas jau ir notikusi.
5. Kur ierakstīt jaunu auto, ar kuru vēl nav bijis nodarbību? (**ievietošanas** anomālija)
6. Dzēš Martas vienīgo nodarbību. Kāda informācija pazūd līdz ar to? (**dzēšanas**
   anomālija)

#### N9 · ★ Olimpiāžu rezultāti

| skolens | klase | audzinatajs | prieksmets | posms | datums | punkti | vieta | sagatavoja |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Līva Ozola | 11.a | D. Liepiņš | Informātika | novada | 2026-01-15 | 78 | 1 | A. Kalniņa |
| Līva Ozola | 11.a | D. Liepiņš | Matemātika | novada | 2026-01-22 | 54 | 3 | M. Riekstiņš |
| Toms Lācis | 12.b | R. Grīnbergs | Informātika | novada | 2026-01-15 | 81 | 1 | A. Kalniņa |
| Līva Ozola | 11.a | D. Liepiņš | Informātika | valsts | 2026-03-10 | 65 | 2 | A. Kalniņa |

Sadali līdz 3NF. Rūpīgi padomā par lauku `sagatavoja`: no kā tas ir atkarīgs — no
skolēna, no olimpiādes vai no kaut kā cita?

### Apzināta dublēšana

#### N10 · Kad dublēšana ir pareiza izvēle

**a)** Veikalā ir tabulas `preces(id, nosaukums, cena)` un
`pasutijuma_rindas(pasutijums_id, prece_id, daudzums, cena)`. Cena glabājas divās vietās.
Kas notiktu ar vecajiem pasūtījumiem, ja cena būtu tikai tabulā `preces` un prece kļūtu
dārgāka? Vai šī vispār ir dublēšana?

**b)** Tabulā `ieraksti(id, teksts, autors_id, komentaru_skaits)` komentāru skaitu var
saskaitīt no tabulas `komentari`. Kāpēc kāds to tomēr glabā atsevišķi? Kāds ir risks, un kas
jādara katru reizi, kad pievieno komentāru?
