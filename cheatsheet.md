# CE Programmēšanā

## 1. Relāciju datubāzes

### Datu tipi

- **Skaitļi**: INT, SMALLINT, BIGINT – ID, skaitītāji.
- **Decimālie**: DECIMAL(10,2) / NUMERIC(p,s) – cenas un summas (kritērijos ir atsevišķs punkts, lai "atļauj saglabāt decimālos skaitļus").
- **Teksts**: VARCHAR(n), TEXT.
- **Datumi/laiki**: DATE, TIMESTAMP.
- **Loģiskais**: BOOLEAN.

### Relāciju apzīmējumi

- **1 : 1** (one-to-one)
- **1 : N** (one-to-many)
- **N : M** (many-to-many)

### Kam pievērst uzmanību

1. ID lauki visās tabulās un pamatots datu tips
2. Angļu datu tipa nosaukums, bet lauku un tabulu nosaukumi latviski bez diakritēm un atstarpmēm ("adrese", nevis "adresē")
3. Vismaz 3 testa vērtības katrā laukā

### SQL piemērs

```sql
CREATE TABLE Kafejnicas (
    id SERIAL PRIMARY KEY,
    nosaukums VARCHAR(60),
    adrese VARCHAR(100)
);

CREATE TABLE Darbinieki (
    id SERIAL PRIMARY KEY,
    vards VARCHAR(30),
    uzvards VARCHAR(30),
    talrunis VARCHAR(15),
    amats VARCHAR(20),
    kafejnica_id INT REFERENCES Kafejnicas(id),
    atvalinajums BOOLEAN
);

CREATE TABLE Pasutijumi (
    id SERIAL PRIMARY KEY,
    summa DECIMAL(10,2),
    datums DATE,
    apraksts TEXT,
    darbinieks_id INT REFERENCES Darbinieki(id)
);
```

⸻

## 2. Objektorientētā programmēšana (OOP)

### 2.1 Bāzes klase “Transportlīdzeklis”

```python
class Transportlidzeklis:
    def __init__(self, zimols, modelis, reg_datums, pilna_masa, degviela):
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degviela = degviela

    def __str__(self):
        return f"{self.zimols} {self.modelis} ({self.reg_datums}) – {self.pilna_masa} kg, {self.degviela}"
```

Šī struktūra sakrīt ar kritērijiem, kur jāizdrukā Audi A4 testa objekts ￼ ￼.

### 2.2 Mantošana — “Kubs → Bloks”

```python
class Kubs:
    def __init__(self, malas_garums: int, krasa: str):
        if malas_garums < 2 or malas_garums > 10:
            print("Kļūda → iestatu malas garumu uz 2 cm")
            malas_garums = 2 # validācija
        self.malas_garums = malas_garums
        self.krasa = krasa

    def tilpums(self) -> int:
        return self.malas_garums ** 3

    def __del__(self):
        print(f"Izdzēsts {self.krasa} objekts")   # obligāts paziņojums

class Bloks(Kubs):
    def __init__(self, malas_garums, krasa, kubu_skaits, forma):
        super().__init__(malas_garums, krasa)
        if kubu_skaits not in range(1, 5):
            print("Kubu skaits jābūt 1-4!") # kritērijs
        self.__kubu_skaits = kubu_skaits
        self.forma = forma
        self.nosaukums = f"{krasa}{kubu_skaits}"
        self.derigums = 0 if forma in {11,12,13,14,22} else 1
```

Eksāmenā vērtē mantošanu, validāciju un tilpums() metodi.

## 3. Programmatūras izstrādes cikls & projektu vadība

Šajā daļā svarīgi atcerēties izstrādes modeļus, izpētes metodes, mērķauditorijas noteikšanu un tehnoloģiju izvēli, potenciālās atšķirības, izvēloties citu tehnoloģiju steku (ātrdarbība (piemēram, c++ ir ātrāks par Python), ierobežojumi (JavaScript un React Native būs atbilstošāks app izstrādei nekā Python), utt.)

| **Uzdevuma formulējums**             | **Atbilde/ieteikums**                                                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nosauc 4 iesaistītās puses**       | Kas būs izstrādājamā produkta lietotāji un kā tie mijiedabosies ar sistēmu                                                                           |
| **Mērķauditorija un izpētes metode** | Pielāgo atbilstoši mērķauditorijai: piemēram, Vadība → Intervija, Klienti → Tiešsaistes aptauja u.t.t.                                               |
| **Izpētes procesa 5 soļi**           | Piemēram: 1) Problēmas definēšana → 2) Datu vākšana → 3) Analīze → 4) Prototipa izveide → 5) Testēšana.                                              |
| **Izvēlēties izstrādes modeli**      | Ūdenskritums — nemainīgas prasības; Agile — daudz atgriezeniskās saites izstrādes procesā. Kritērijos minēta punktu piešķiršana par motivētu izvēli. |
| **Piedāvāt 2 īstenošanas variantus** | Apraksti steku + izvietošanu (piem., Node.js + Vercel pret Java + fiziskais serveris).                                                               |

## 4. Algoritmi, datu struktūras & API

### 4.1 Pamata Python sintakse (ko bieži prasa)

```python
# Nosacījums

if x > 10:
...

# Saraksts

vardi = ["Liepaja", "Riga"]
vardi.append("Jelgava")
vardi.sort()

# Cikls pa vārdnīcu

skaititajs = {"A":1}
for burts, sk in skaititajs.items():
print(burts, sk)

# Funkcija

def kvadrats(n: int) -> int:
    return n ** 2
```

### 4.2 API pieprasījums ar kļūdu kontroli (atkritumu punkta uzdevums)

```python
import requests, sys

URL = "https://data.gov.lv/..." # resursa ID redzams darba lapā
try:
    r = requests.get(URL, timeout=5)
    r.raise_for_status()
except requests.exceptions.Timeout:
    sys.exit("Savienojuma noildze")
except requests.exceptions.HTTPError:
    sys.exit("Serveris neatbild")

data = r.json()
if not data:
    sys.exit("Tukša atbilde")

baterijas = [p for p in data if "baterijas" in p["type"]]
for p in baterijas:
    print(p["adrese"], "|", p["pilseta"])
```

Šo var izpildīt arī JavaScript, kā tev ērtāk

```javascript
const fetch = require("node-fetch");

const URL = "https://data.gov.lv/..."; // resursa ID redzams darba lapā

fetch(URL, { timeout: 5000 })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP kļūda: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    if (!data || data.length === 0) {
      console.error("Tukša atbilde");
      process.exit(1);
    }

    const baterijas = data.filter(
      (p) => p.type && p.type.includes("baterijas")
    );
    baterijas.forEach((p) => {
      console.log(`${p.adrese} | ${p.pilseta}`);
    });
  })
  .catch((error) => {
    if (error.type === "request-timeout") {
      console.error("Savienojuma noildze");
    } else {
      console.error("Serveris neatbild");
    }
    process.exit(1);
  });
```

Kritēriji paredz punktus par bibliotēkas importu, 2 statusu pārbaudēm, tukša masīva apstrādi un lauku izvadi. Analogu uzdevumu ar restcountries.com skaties 2024. gada darbā.

⸻

## 5. Ātro pārbaužu saraksts pirms eksāmena

- **ER diagramma:** Uzrakstu 3 tabulu ER diagrammu (ar bultiņām) < 7 minūtēs
- **Datu tipi:** Zinu 5 datu tipus angļu valodā + kad lietot DECIMAL
- **OOP:** Varu no galvas uzrakstīt `Transportlidzeklis` klasi un izsaukt `print(obj)`
- **Validācija:** Protu validēt ievaddatus un izdrukāt destruktora paziņojumu
- **Izpēte:** Spēju nosaukt 3 izpētes metodes un sasaistīt tās ar atbilstošo mērķauditoriju
- **API:** Uzrakstu GET pieprasījumu, apstrādāju 200/404 un tukšu JSON < 10 min
- **Nosaukumi:** Praksē nelietoju diakritikas mainīgajos un lauku nosaukumos

Veiksmi — katrs pareizi pamatots sīkums dod punktus!
