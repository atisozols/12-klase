# 3. nodevums - testēšana

### **1. uzdevums: Vienībtestēšana (Unit Testing)**

- **1.1. Funkciju izvēle:** Izvēlies divas būtiskas funkcijas savā programmā, kuras testēt atsevišķi.
- **1.2. Definē testu scenārijus katrai funkcijai.**
- **1.3. Veic testēšanu:** izpildi funkciju ar dažādiem ievades datiem un dokumentē rezultātus.
- **1.4.** **Pieraksti veiktos testus un rezultātus tabulas formā.**
- **1.5.** **Pēc testēšanas pievieno secinājumus**, piemēram, ja testos tika konstatēta kļūda, kā to var labot.

**Piemērs:**

Ja programma apstrādā atlaides pirkumiem, tad viena no testējamajām funkcijām varētu būt aprēķināt_galīgo_cenu(sākotnējā_cena, atlaide).

| **Tests** | **Ievade (sākotnējā cena, atlaide)** | **Sagaidāmais rezultāts** | **Faktiskais rezultāts** | **Rezultāts (✓/✗)** |
| --- | --- | --- | --- | --- |
| 1 | 100€, 10% | 90€ | 90€ | ✓ |
| 2 | 50€, 20% | 40€ | 40€ | ✓ |
| 3 | 200€, -5% (nepareiza ievade) | Kļūda | Kļūda | ✓ |

---

### **2. uzdevums: Integrācijas testēšana (Integration Testing)**

- **2.1. Integrācijas identificēšana:** Identificē divas vai vairākas sistēmas komponentes, kas sadarbojas (piemēram, datubāze un lietotāja reģistrācija, API pieprasījumi).
- **2.2. Definē testu scenārijus, kas pārbauda šo integrāciju.**
- **2.3. Veic testēšanu,** pārbaudot, vai dati tiek pareizi apstrādāti starp dažādām sistēmas daļām
- **2.4.** **Pieraksti veiktos testus un rezultātus tabulas formā.**
- **2.5.** **Pēc testēšanas pievieno secinājumus**, piemēram, ja testos tika konstatēta kļūda, kā to var labot.

| **Tests** | **Scenārijs** | **Sagaidāmais rezultāts** | **Faktiskais rezultāts** | **Rezultāts (✓/✗)** |
| --- | --- | --- | --- | --- |
| 1 | Reģistrēt jaunu lietotāju (vārds: Anna, e-pasts: anna@example.com) | Lietotājs saglabāts datubāzē | Lietotājs saglabāts datubāzē | ✓ |
| 2 | Reģistrēt lietotāju ar jau esošu e-pastu | Kļūda: “E-pasts jau tiek izmantots” | Lietotājs netiek saglabāts | ✓ |
| 3 | Reģistrēt lietotāju bez e-pasta | Kļūda: “Obligāts lauks” | Kļūda attēlota | ✓ |

**Dokumentācija:** Ja integrācijas testēšanā tiek atklātas kļūdas (piemēram, dati netiek saglabāti pareizi), apraksti, kā tās var novērst.

---

### **3. uzdevums: Akcepttestēšana (Acceptance Testing)**

- **3.1. Izveido divus scenārijus,** kas pārbauda programmatūras darbību no lietotāja skatpunkta.
- **3.2. Veic testēšanu,** sekojot līdzi scenārijam
- **3.3.** **Pieraksti veiktos testus un rezultātus tabulas formā.**
- **3.4.** **Pēc testēšanas pievieno secinājumus**, piemēram, ja testos tika konstatēta kļūda, kā to var labot.

**Piemērs:**

Ja programmatūra ir tiešsaistes rezervācijas sistēma, tad viens no testiem varētu būt “Rezervācijas veikšana un apstiprinājums e-pastā”.

| **Tests** | **Scenārijs** | **Sagaidāmais rezultāts** | **Faktiskais rezultāts** | **Rezultāts (✓/✗)** |
| --- | --- | --- | --- | --- |
| 1 | Lietotājs rezervē laiku caur sistēmu | Paziņojums: “Rezervācija veiksmīga” un apstiprinājuma e-pasts | Rezervācija veikta, e-pasts saņemts | ✓ |
| 2 | Lietotājs mēģina rezervēt aizņemtu laiku | Paziņojums: “Šis laiks jau ir aizņemts” | Paziņojums par kļūdu parādīts | ✓ |

---

### **4. Papilduzdevums: Automatizēts tests**

- **4.1. Izvēlies vienu** no iepriekš veiktajiem testiem.
- **4.2. Uzraksti vienkāršu automatizētu testu,** kas pārbauda šo funkcionalitāti.
- **4.3.** **Palaid testu un dokumentē rezultātu.**

**Piemērs: Automatizēts vienībtests ar Jest (vai kādu citu automatizēto testu bibliotēku, ja projekts nav rakstīts JavaScript)**

**Scenārijs:** Ir funkcija calculateTotal(price, discount), kas aprēķina gala cenu, ņemot vērā atlaidi. Funkcija nedrīkst pieļaut negatīvu atlaidi.

**1. Funkcijas kods, kuru testēsim (utils.js):**

```jsx
function calculateTotal(price, discount) {
    if (discount < 0) {
        throw new Error("Atlaide nevar būt negatīva");
    }
    return price - (price * (discount / 100));
}

module.exports = calculateTotal;
```

---

**2. Automatizēts tests ar Jest (utils.test.js):**

```jsx
const calculateTotal = require('./utils');

test('Aprēķina gala cenu ar atlaidi', () => {
    expect(calculateTotal(100, 10)).toBe(90);
    expect(calculateTotal(50, 20)).toBe(40);
});

test('Neļauj negatīvas atlaides', () => {
    expect(() => calculateTotal(200, -5)).toThrow("Atlaide nevar būt negatīva");
});
```

---

**3. Kā palaist testus?**

**Instalē Jest savā projektā** (ja tas vēl nav izdarīts):

```
npm install --save-dev jest
```

**Pievieno package.json failā sadaļu scripts**, lai varētu palaist testus:

```json
"scripts": {
   "test": "jest"
}
```

**Palaid testus ar šādu komandu:**

```
npm test
```

**Sagaidāmais rezultāts:**

Ja funkcija darbojas pareizi, Jest parādīs, ka visi testi ir veiksmīgi izpildīti.

Ja kāds tests neizdodas, Jest norādīs kļūdu un precīzu problēmu.
