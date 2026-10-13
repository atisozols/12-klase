# Summatīvais darbs — pakomāta sūtījumi

**Bloks:** 01 · **Forma:** pie datora · **Laiks:** 90 min

Šajā darbā tiek vērtēta klašu hierarhija, kolekcijas pārvaldība, datu saglabāšana,
grafiskā saskarne un izņēmumi. Saskarnes sākuma kods ir dots datnes beigās.

| Daļa | Ieteicamais laiks |
| --- | --- |
| 1. Klašu modelis | 20 min |
| 2. Kolekcija | 15 min |
| 3. Datu glabāšana | 15 min |
| 4. Grafiskā saskarne | 30 min |
| Rezerve un pārbaude | 10 min |

Ja kāda daļa aizņem ilgāk par ieteikto laiku, pārej pie nākamās.

---

## Situācija

Pakomātu uzņēmums reģistrē sūtījumus: **parastas pakas** un **ekspressūtījumus**. Katram
sūtījumam ir adresāts un svars kilogramos. Programma aprēķina katra sūtījuma cenu un kopējos
ieņēmumus.

## Prasības

### 1. Klašu modelis

- Abstrakta virsklase `Sutijums` ar atribūtiem `adresats` un `svars_kg` un ar abstraktu
  metodi `cena()`.
- Tieši **divas** apakšklases:

  | Klase      | Papildu atribūts | Cena (EUR)                   |
  | ---------- | ---------------- | ---------------------------- |
  | `Paka`     | —                | 2.50 + 0.90 × kg             |
  | `Ekspress` | `attalums_km`    | 2.50 + 0.90 × kg + 0.30 × km |

- `@classmethod` `no_vardnicas(dati)`, kas izveido pareizās apakšklases objektu no
  vārdnīcas, piemēram, `{"veids": "Ekspress", "adresats": "Anna", "svars_kg": 2, "attalums_km": 10}`.
- **Iekapsulēts** atribūts `svars_kg` ar `property`. Svaram jābūt skaitlim, lielākam par 0
  un ne lielākam par 30. Ja vērtība ir nederīga, jāizmet paša definēts izņēmums
  `NederigiDati`.

### 2. Kolekcija

Izveido klasi `Pakomats`, kas glabā sūtījumu sarakstu. Tajā jābūt šādām metodēm:

- `pievienot(sutijums)`: katrs sūtījums saņem unikālu numuru (id), metode to atgriež;
- `atrast(id)`: atgriež sūtījumu, bet, ja tāda nav, izmet paša definētu izņēmumu
  `SutijumsNavAtrasts`;
- `kopejie_ienemumi()`: saskaita visu sūtījumu cenas. Šajā metodē **nedrīkst būt**
  `isinstance` vai tipa pārbaudes, tai jāstrādā polimorfi.

### 3. Datu glabāšana

- `saglabat(datne)`: saglabā visus sūtījumus JSON datnē. Katrā ierakstā jāglabā arī
  sūtījuma veids.
- `ielasit(datne)`: ielasa sūtījumus no datnes, izmantojot `no_vardnicas`. Ja datnes vēl
  nav, programma nedrīkst avarēt.

### 4. Grafiskā saskarne

Izmanto doto sākuma kodu. Logs un visi elementi jau ir izveidoti — tev jāaizpilda trīs
funkcijas:

- `poga_pievienot()`: nolasa laukus, izveido sūtījumu, pievieno to, saglabā datni un
  parāda piešķirto id un cenu;
- `poga_atrast()`: atrod sūtījumu pēc id un parāda tā datus un cenu;
- `poga_kopsavilkums()`: parāda sūtījumu skaitu un kopējos ieņēmumus.

Saskarnes funkcijas tikai nolasa ievadi, izsauc `Pakomats` metodes un parāda rezultātu.
Ja ievade ir nederīga (burti svara laukā, svars `45`, neesošs id), programma parāda
paziņojumu (`messagebox`) un neavarē. Izņēmumus met klasēs, bet ķer saskarnē.

## ★ Ja atliek laiks

1. Pievieno metodi `dzest(id)` un pogu **Dzēst**.
2. Pievieno trešo veidu `Vestule` (cena 1.20, svars ne lielāks par 0.5 kg). Vai
   `kopejie_ienemumi` bija jāmaina?

---

## Sākuma kods (`saskarne.py`)

```python
import tkinter as tk
from tkinter import ttk, messagebox

# Pielāgo importu saviem moduļu nosaukumiem
from pakomats import Pakomats, Paka, Ekspress, NederigiDati, SutijumsNavAtrasts

DATNE = "sutijumi.json"
pakomats = Pakomats()
pakomats.ielasit(DATNE)


def paradit(teksts):
    rezultats.delete("1.0", tk.END)
    rezultats.insert(tk.END, teksts)


def poga_pievienot():
    # Lauku vērtības: veids.get(), lauks_adresats.get(), lauks_svars.get(), lauks_km.get()
    pass


def poga_atrast():
    # Lauka vērtība: lauks_id.get()
    pass


def poga_kopsavilkums():
    pass


logs = tk.Tk()
logs.title("Pakomāts")

tk.Label(logs, text="Veids").grid(row=0, column=0, sticky="w")
veids = ttk.Combobox(logs, values=["Paka", "Ekspress"], state="readonly")
veids.current(0)
veids.grid(row=0, column=1, columnspan=2, sticky="we")

tk.Label(logs, text="Adresāts").grid(row=1, column=0, sticky="w")
lauks_adresats = tk.Entry(logs)
lauks_adresats.grid(row=1, column=1, columnspan=2, sticky="we")

tk.Label(logs, text="Svars (kg)").grid(row=2, column=0, sticky="w")
lauks_svars = tk.Entry(logs)
lauks_svars.grid(row=2, column=1, columnspan=2, sticky="we")

tk.Label(logs, text="Attālums (km, tikai ekspresim)").grid(row=3, column=0, sticky="w")
lauks_km = tk.Entry(logs)
lauks_km.grid(row=3, column=1, columnspan=2, sticky="we")

tk.Label(logs, text="Sūtījuma id").grid(row=4, column=0, sticky="w")
lauks_id = tk.Entry(logs)
lauks_id.grid(row=4, column=1, columnspan=2, sticky="we")

tk.Button(logs, text="Pievienot", command=poga_pievienot).grid(row=5, column=0, sticky="we")
tk.Button(logs, text="Atrast", command=poga_atrast).grid(row=5, column=1, sticky="we")
tk.Button(logs, text="Kopsavilkums", command=poga_kopsavilkums).grid(row=5, column=2, sticky="we")

rezultats = tk.Text(logs, width=50, height=10)
rezultats.grid(row=6, column=0, columnspan=3, pady=(8, 0))

logs.mainloop()
```
