# DATUBAZE.md — veidne

Nokopē šo failu savā projektā kā `DATUBAZE.md` un aizpildi. Slīprakstā rakstītie
paskaidrojumi ir tev — tos izdzēs.

Pārbaude: cits izstrādātājs, kurš tavu sistēmu redz pirmo reizi, pēc šī faila spēj
(1) izveidot datubāzi, (2) saprast, kas glabājas katrā tabulā, (3) uzrakstīt vaicājumu.

---

# <Sistēmas nosaukums> — datubāze

## Par sistēmu

*Divi trīs teikumi: ko sistēma dara un kas to lieto.*

## Kā izveidot

```
python3 izveidot.py
```

*Kas notiek: kuri faili tiek izpildīti un kādā secībā. Kur atrodas `.db` fails.*

## ER modelis

![ER modelis](er-modelis.png)

*Attēls vai shēma tekstā. Katrai saistībai jābūt redzamai kardinalitātei.*

## Tabulas

### `<tabula>`

*Ko šī tabula glabā. Kāpēc tā ir atsevišķa tabula — kuru dublēšanos tā novērš.*

| Lauks | Tips | Ierobežojumi | Nozīme |
| --- | --- | --- | --- |
| `id` | INTEGER | PRIMARY KEY | |
| `...` | TEXT | NOT NULL, UNIQUE | |
| `..._id` | INTEGER | REFERENCES `...`(id) | |

*Atkārto katrai tabulai.*

## Ierobežojumi un indeksi

| Kas | Kur | Kāpēc |
| --- | --- | --- |
| `CHECK (...)` | `tabula.lauks` | *kādus nederīgus datus tas aptur* |
| `UNIQUE` | `tabula.lauks` | |
| indekss `idx_...` | `tabula.lauks` | *kurš vaicājums no tā kļūst ātrāks* |

## Normalizācija

*Vai shēma atbilst 3NF? Ja kaut kur ir apzināta dublēšana, pieraksti kur un kāpēc.*

## Transakcijas

*Kuras darbības sistēmā ir jāveic kā viena transakcija un kāpēc.*

## Vaicājumu piemēri

*Divi trīs biežāk vajadzīgie vaicājumi ar paskaidrojumu. Pārējie — `vaicajumi.sql`.*

```sql
-- Kuri ... ?
SELECT ...
```
