# Formatīvais vērtējums — 24.03.

---

## H1. Izomorfu virkņu pārbaude

### Uzdevums

Dotas divas virknes `s` un `t` vienādā garumā.

Nosaki, vai tās ir **izomorfas** — katru `s` simbolu var aizstāt ar citu (vai to pašu) simbolu, lai iegūtu `t`, saglabājot simbolu secību. Divi dažādi `s` simboli nedrīkst attēloties uz vienu un to pašu `t` simbolu.

Atgriez `True` vai `False`.

### Piemērs

```python
s = "egg"
t = "add"
# Output: True
# Paskaidrojums: e -> a, g -> d
```

```python
s = "foo"
t = "bar"
# Output: False
# Paskaidrojums: o nevar attēloties uz 'a' UN 'r' vienlaicīgi
```

```python
s = "paper"
t = "title"
# Output: True
```

---

## H2. Pāru skaits ar doto starpību

### Uzdevums

Dots veselu skaitļu saraksts `nums` un skaitlis `k`.

Saskaitī, cik daudz **unikālu pāru** `(a, b)` eksistē, kur `a - b == k` un `a != b` (ja `k > 0`).

Katrs pāris tiek skaitīts tikai vienu reizi.

### Piemērs

```python
nums = [1, 5, 3, 4, 2]
k = 2
# Output: 3
# Paskaidrojums: pāri ir (3,1), (4,2), (5,3)
```

```python
nums = [1, 2, 3, 4, 5]
k = 1
# Output: 4
# Paskaidrojums: (2,1), (3,2), (4,3), (5,4)
```

---

## T1. Sakārtot krāsas (Nīderlandes karoga problēma)

### Uzdevums

Dots saraksts `nums`, kas satur tikai vērtības `0`, `1` un `2`.

Sakārto sarakstu **uz vietas** tā, lai visi `0` ir sākumā, tad visi `1`, tad visi `2`.

Neizmanto iebūvēto `sort()` funkciju.

### Piemērs

```python
nums = [2, 0, 2, 1, 1, 0]
# Pēc izsaukuma: [0, 0, 1, 1, 2, 2]
```

```python
nums = [2, 0, 1]
# Pēc izsaukuma: [0, 1, 2]
```

---

## T2. Virkņu salīdzināšana ar atpakaļatkāpi

### Uzdevums

Dotas divas virknes `s` un `t`, kas var saturēt rakstzīmi `#`, kura nozīmē **atpakaļatkāpi** (backspace) — dzēš iepriekšējo simbolu.

Nosaki, vai abas virknes pēc visu `#` apstrādes ir **vienādas**.

Risini ar diviem rādītājiem no beigām, bez papildu masīviem.

### Piemērs

```python
s = "ab#c"
t = "ad#c"
# Output: True
# Paskaidrojums: abas virknes kļūst par "ac"
```

```python
s = "a##c"
t = "#a#c"
# Output: True
# Paskaidrojums: abas virknes kļūst par "c"
```

```python
s = "ab##"
t = "c#d#"
# Output: True
# Paskaidrojums: abas virknes kļūst par ""
```

---
