# 02. bloks — teorija un paraugi

Šis ir bloka atgādne. Uzdevumus pildi [`uzdevumi.md`](uzdevumi.md) failā.

## §1 ER modelis

ER modelis (entītiju un saistību modelis) ir veids, kā datubāzi uzzīmēt, pirms to izveido.

| Elements | Ko nozīmē                   | Kā zīmē                       |
| -------- | --------------------------- | ----------------------------- |
| Entītija | lieta, par kuru glabā datus | taisnstūris                   |
| Atribūts | entītijas īpašība           | ovāls vai saraksts taisnstūrī |
| Saistība | kā entītijas saistās        | līnija ar apzīmējumu          |

**Kardinalitāte** pasaka, cik daudz ar cik:

- **1:1** — vienai pasei atbilst viens cilvēks (reti sastopams; parasti to var apvienot vienā tabulā);
- **1:N** — vienā klasē daudz skolēnu, bet skolēns ir vienā klasē;
- **N:M** — skolēns var būt daudzos pulciņos, pulciņā daudz skolēnu.

**No modeļa uz tabulām** — mehāniski soļi:

1. katra entītija kļūst par tabulu;
2. katrs atribūts kļūst par lauku;
3. 1:N saistība kļūst par ārējo atslēgu **daudzu pusē**;
4. N:M saistība **vienmēr** kļūst par atsevišķu starptabulu ar divām ārējām atslēgām.

Ja entītija saistās pati ar sevi (darbinieks un viņa vadītājs), ārējā atslēga norāda uz
to pašu tabulu: `vaditajs_id INTEGER REFERENCES darbinieki(id)`.

### Paraugs: skolas bibliotēka

> Bibliotēkā ir grāmatas. No vienas grāmatas var būt vairāki eksemplāri, katram savs
> svītrkods. Lasītājs var aizņemties eksemplāru; izsniegumam pieraksta datumu, kad izsniegts
> un kad atgriezts.

**1. Entītijas** ir lietvārdi, par kuriem jāglabā vairāki fakti: grāmata, eksemplārs,
lasītājs, izsniegums. «Svītrkods» un «datums» ir tikai fakti, tāpēc tie ir atribūti.

**2. Saistības** — par katru pāri jautā abos virzienos:

- vienai grāmatai daudz eksemplāru; eksemplārs ir vienas grāmatas → **1:N**;
- lasītājs var aizņemties daudz eksemplāru, eksemplāru laika gaitā aizņemas daudzi
  lasītāji → **N:M**. Starptabula ir *izsniegums*, un tai ir savi atribūti (datumi).

```
┌──────────┐ 1     N ┌────────────┐ 1     N ┌─────────────┐ N     1 ┌──────────┐
│ GRĀMATA  │─────────│ EKSEMPLĀRS │─────────│ IZSNIEGUMS  │─────────│ LASĪTĀJS │
│ nosaukums│         │ svitrkods  │         │ izsniegts   │         │ vards    │
│ autors   │         │ stavoklis  │         │ atgriezts   │         │ epasts   │
│ gads     │         └────────────┘         └─────────────┘         └──────────┘
└──────────┘
```

**3. Tabulas** — mehāniski pēc soļiem augstāk:

```
gramatas(id, nosaukums, autors, gads)
eksemplari(id, gramata_id → gramatas, svitrkods, stavoklis)
lasitaji(id, vards, epasts)
izsniegumi(id, eksemplars_id → eksemplari, lasitajs_id → lasitaji, izsniegts, atgriezts)
```

Biežākās kļūdas: grāmatai lauks `lasitajs_id` (tad nav vēstures — skat. situāciju
krājumu K2); nav atšķirta grāmata no eksemplāra; N:M saistība bez starptabulas.

Vairāk situāciju vingrināšanai — [`situacijas.md`](situacijas.md) A–C daļa.

## §2 Normalizācija

Normalizācija ir datu dublēšanās novēršana. Trīs pirmās normālformas cilvēku valodā:

**1NF — vienā laukā viena vērtība.**
Slikti: `telefoni = "26123456, 29876543"`. Labi: atsevišķa tabula `telefoni`.

**2NF — katrs lauks ir atkarīgs no visas primārās atslēgas.**
Ja tabulai `pasutijuma_rindas(pasutijums_id, prece_id, daudzums, preces_nosaukums)`
primārā atslēga ir abas pirmās kolonnas, tad `preces_nosaukums` ir atkarīgs tikai no
`prece_id` — tam te nav vietas.

**3NF — neviens lauks nav atkarīgs no cita ne-atslēgas lauka.**
Ja tabulā `skoleni(id, vards, klase_id, klases_audzinatajs)`, tad audzinātājs ir atkarīgs no
klases, ne no skolēna. Tam jābūt tabulā `klases`.

**Pazīme, ka kaut kas nav kārtībā:** to pašu informāciju labo divās vietās. Ja skolotājs
maina uzvārdu un tas jālabo 200 rindās, shēma nav normalizēta.

**Trīs anomālijas** — tas, kas notiek ar nenormalizētu tabulu:

| Anomālija | Kas notiek | Piemērs tabulā `skoleni(id, vards, klase, audzinatajs)` |
| --- | --- | --- |
| atjaunināšanas | to pašu faktu jālabo daudzās rindās; aizmirst vienu — dati pretrunīgi | maina audzinātāju — jālabo visiem klases skolēniem |
| ievietošanas | faktu nevar ierakstīt, kamēr nav kaut kā cita | jaunai klasei nevar ierakstīt audzinātāju, kamēr tajā nav neviena skolēna |
| dzēšanas | dzēšot vienu faktu, pazūd cits | izdzēšot klases pēdējo skolēnu, pazūd ziņas par audzinātāju |

### Soli pa solim

1. **Atrodi primāro atslēgu.** Kas viennozīmīgi identificē rindu? Ja tas ir lauku pāris,
   pieraksti abus.
2. **1NF.** Vai kādā laukā ir saraksts («a, b, c») vai atkārtotas kolonnas (`telefons1`,
   `telefons2`)? → saraksts kļūst par atsevišķu tabulu ar ārējo atslēgu.
3. **Katram laukam jautā: «No kā tas ir atkarīgs?»** Pieraksti `A → B` («ja zinu A, zinu
   arī B»).
   - atkarīgs no visas atslēgas → paliek;
   - atkarīgs tikai no atslēgas daļas → **2NF** pārkāpums;
   - atkarīgs no cita ne-atslēgas lauka → **3NF** pārkāpums.
4. **Grupē pēc tā, no kā atkarīgs.** Katrs `A` kļūst par savu tabulu ar `A` kā primāro
   atslēgu, un sākotnējā tabulā paliek tikai `A` kā ārējā atslēga.
5. **Pārbaudi:** vai katrs fakts tagad glabājas tieši vienā vietā?

Vingrināšanai — [`situacijas.md`](situacijas.md) D daļa (N0–N10).

**Kad normalizāciju apzināti pārkāpj:** ja vaicājums ar pieciem `JOIN` ir par lēnu un dati
gandrīz nemainās, daļu var apzināti dublēt. Tas ir lēmums ar pamatojumu, ne slinkums.

## §3 Datubāzes izveide

> Kā to visu dara no Python ar `sqlite3` — savienojums, ierobežojumi darbībā, indeksi,
> shēma no faila — skat. [`teorija.py`](teorija.py) §1–§7.

```sql
CREATE TABLE lasitaji (
    id INTEGER PRIMARY KEY,
    vards TEXT NOT NULL,
    epasts TEXT UNIQUE NOT NULL,
    registrets TEXT DEFAULT (date('now'))
);

CREATE TABLE gramatas (
    id INTEGER PRIMARY KEY,
    nosaukums TEXT NOT NULL,
    autors TEXT NOT NULL,
    gads INTEGER CHECK (gads BETWEEN 1450 AND 2100)
);

CREATE TABLE izsniegumi (
    id INTEGER PRIMARY KEY,
    lasitajs_id INTEGER NOT NULL REFERENCES lasitaji(id),
    gramata_id INTEGER NOT NULL REFERENCES gramatas(id),
    izsniegts TEXT NOT NULL,
    atgriezts TEXT
);

CREATE INDEX idx_izsniegumi_lasitajs ON izsniegumi(lasitajs_id);
```

**Indekss** ir kā satura rādītājs grāmatā: meklēšana kļūst ātrāka, bet ierakstīšana —
mazliet lēnāka, un datubāze aizņem vairāk vietas. Indeksu liek laukam, pēc kura **meklē
bieži**, parasti ārējām atslēgām.

Datubāzi vienmēr veido ar **skriptu**, ne klikšķinot. Skriptu var ielikt repozitorijā,
palaist no jauna un iedot citam.

## §4 Apakšvaicājumi un transakcijas

> Piemēri no Python, tostarp transakcija ar `ROLLBACK`, kad pietrūkst preces —
> [`teorija.py`](teorija.py) §8–§9.

Apakšvaicājums ir vaicājums vaicājumā:

```sql
SELECT nosaukums, gads
FROM gramatas
WHERE gads > (SELECT AVG(gads) FROM gramatas);
```

**Transakcija** ir vairākas darbības, kurām jānotiek visām vai nevienai:

```sql
BEGIN;
UPDATE konti SET atlikums = atlikums - 50 WHERE id = 1;
UPDATE konti SET atlikums = atlikums + 50 WHERE id = 2;
COMMIT;
```

Ja starp abām rindām kaut kas notiek greizi, `ROLLBACK` atgriež visu sākotnējā stāvoklī.
Bez transakcijas nauda pazustu no viena konta, neparādoties otrā.

Transakcija vajadzīga vienmēr, kad **divas vai vairāk izmaiņas ir loģiski viena darbība**.

## §5 Jaucējfunkcijas

Jaucējfunkcija pārvērš jebkuras garuma tekstu fiksēta garuma virknē tā, ka:

- vienam un tam pašam tekstam rezultāts vienmēr ir vienāds;
- no rezultāta tekstu atgūt **nevar**;
- viena simbola maiņa maina visu rezultātu.

```python
import hashlib

def jauceja(teksts):
    return hashlib.sha256(teksts.encode("utf-8")).hexdigest()

print(jauceja("parole123"))
print(jauceja("parole124"))   # pilnīgi atšķirīgs
```

Paroles glabā kā jaucējvērtību. Kad lietotājs piesakās, salīdzina jaucējvērtības, ne paroles.
Tāpēc reāla sistēma nevar «atgādināt» paroli — tikai ļaut to nomainīt.

**Sāls (salt)** ir nejaušs papildinājums katrai parolei atsevišķi:

```python
import hashlib, secrets

sals = secrets.token_hex(16)
jauceja_ar_salu = hashlib.sha256((sals + "parole123").encode()).hexdigest()
```

Bez sāls diviem lietotājiem ar vienādu paroli būtu vienāda jaucējvērtība, un uzbrucējs
varētu izmantot iepriekš sagatavotas tabulas. Ražošanas sistēmās lieto `bcrypt` vai
`argon2`, kas ir apzināti lēni — tas uzbrucējam sadārdzina minēšanu.

## §6 Šifrēšana

Trīs dažādas lietas, kuras bieži sajauc:

|                       | Var atgriezt atpakaļ?       | Kam lieto                        |
| --------------------- | --------------------------- | -------------------------------- |
| Jaukšana              | nē                          | paroles, datu integritāte        |
| Simetriskā šifrēšana  | jā, ar to pašu atslēgu      | datņu, datubāzes šifrēšana       |
| Asimetriskā šifrēšana | jā, ar otru atslēgu no pāra | HTTPS, paraksti, atslēgu apmaiņa |

**Asimetriskā** šifrēšana lieto atslēgu pāri: publisko un privāto. Ko šifrē ar vienu,
atšifrē tikai ar otru.

- Gribi nosūtīt man noslēpumu → šifrē ar **manu publisko** atslēgu. Atšifrēt varu tikai es.
- Gribi pierādīt, ka ziņa ir no tevis → šifrē ar **savu privāto**. Atšifrēt var jebkurš ar
  tavu publisko, un tas pierāda autorību.

Tā divi cilvēki var apmainīties ar noslēpumu, nekad nesatiekoties.

**HTTPS lieto abus:** asimetrisko, lai droši vienotos par kopīgu atslēgu, un tad simetrisko,
jo tā ir daudz ātrāka.

## §7 Datubāzes drošība

**SQL injekcija** rodas, kad vaicājumu saliek no virknēm:

```python
# BĪSTAMI — nekad tā nedari
vaicajums = f"SELECT * FROM lietotaji WHERE vards = '{ievade}'"
```

Ja lietotājs ievada `' OR '1'='1`, vaicājums kļūst par `... WHERE vards = '' OR '1'='1'`,
kas ir patiess vienmēr.

**Parametrizēts vaicājums** to novērš, jo ievade nekad nekļūst par koda daļu:

```python
con.execute("SELECT * FROM lietotaji WHERE vards = ?", (ievade,))
```

Personas datu principi: glabā tikai to, kas tiešām vajadzīgs; pieraksti, kāpēc katrs lauks
ir; neglabā to, ko nevari pasargāt.

## §8 Serveris izstrādātāja vajadzībām

Izstrādes serveris atšķiras no ražošanas servera:

|              | Izstrādē              | Ražošanā                                 |
| ------------ | --------------------- | ---------------------------------------- |
| Kļūdas       | pilns apraksts ekrānā | žurnālā, lietotājam vispārīgs paziņojums |
| Datubāze     | testa dati            | īsti dati, rezerves kopijas              |
| Restartēšana | pēc katras izmaiņas   | reti, plānoti                            |
| Pieejamība   | tikai savs dators     | internets, HTTPS                         |

**Žurnalēšana** ir tas, kas ļauj saprast, kas notika vakar naktī: laiks, maršruts, statusa
kods, ilgums. Bez tā kļūdu var atkārtot tikai nejauši.

## §9 Datortīkls

| Ierīce                | Loma                                      |
| --------------------- | ----------------------------------------- |
| Komutators (switch)   | savieno ierīces vienā tīklā               |
| Maršrutētājs (router) | savieno tīklus, izlaiž datus uz internetu |
| Piekļuves punkts      | bezvadu pieslēgums                        |

**IP adrese** identificē ierīci tīklā. **Apakštīkla maska** pasaka, kura adreses daļa ir
tīkls un kura — ierīce. Ar masku `255.255.255.0` tīklā ietilpst 254 ierīces (256 mīnus tīkla
un apraides adrese). **Vārteja** ir maršrutētāja adrese, uz kuru sūta visu, kas nav vietējais.
**DNS** pārtulko nosaukumu par adresi.

**Statiskā** adrese ir fiksēta un tiek iestatīta ar roku — to lieto serveriem un printeriem.
**Dinamisko** izsniedz DHCP serveris — to lieto parastām ierīcēm.

Komandas: `ipconfig` (Windows), `ifconfig` vai `ip addr` (macOS, Linux), `ping`, `tracert`
vai `traceroute`.

## §10 Maršrutētāja konfigurācija

Pirmās piecas darbības ar jaunu maršrutētāju:

1. nomaini administratora paroli (noklusētā ir zināma visiem);
2. iestati Wi-Fi paroli ar WPA2 vai WPA3;
3. nomaini tīkla nosaukumu tā, lai tas neatklāj ierīces modeli;
4. atslēdz attālināto administrēšanu no interneta;
5. atjaunini programmatūru.

**MAC filtrs** ļauj tīklā tikai norādītām ierīcēm. Tas ir ērts, bet **nav droša
aizsardzība** — MAC adresi var viltot.

**Portu pāradresācija** novirza pieprasījumus no maršrutētāja publiskās adreses uz konkrētu
ierīci tīklā. Tā ir vajadzīga, lai serveris mājās būtu pieejams no interneta — un tā ir
risks, jo tavu serveri tagad var atrast un pārbaudīt ikviens.

## §11 Servera pieejamība

`localhost` un `127.0.0.1` nozīmē «šis pats dators». Serveris, kas klausās tikai tur, nav
pieejams nevienam citam.

Lai serveris būtu pieejams lokālajā tīklā, tam jāklausās uz visām adresēm (`0.0.0.0`), un
citi to atver pēc tava datora lokālās IP adreses: `http://192.168.1.42:3000`.

Pirms to darīt, pārbaudi: vai serverī ir validācija? vai kļūdas neatklāj lieko? vai datubāzē
ir īsti dati?

## §12 Servera uzturēšana

| Kritērijs             | Savs serveris              | Nomāts                       |
| --------------------- | -------------------------- | ---------------------------- |
| Izmaksas              | vienreizējas + strāva      | regulāras                    |
| Kontrole              | pilna                      | ierobežota                   |
| Atbildība par darbību | tava                       | daļēji pakalpojuma sniedzēja |
| Fiziskā drošība       | jānodrošina pašam          | nodrošināta                  |
| Pieejamība            | atkarīga no tava interneta | augsta                       |

Savā serverī jādomā par strāvas padevi, mikroklimatu, fizisko piekļuvi un rezerves kopijām.

**Rezerves kopiju plāns** atbild uz četriem jautājumiem: ko kopē, cik bieži, kur glabā,
**kā pārbauda, ka kopija tiešām der**. Nepārbaudīta rezerves kopija ir cerība, ne plāns.
