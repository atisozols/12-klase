## 1. Dominējošais elements ar slieksni

### Uzdevums

Dots veselu skaitļu saraksts `nums` un skaitlis `threshold`.

Atgriez visus elementus, kas parādās **vairāk nekā `threshold` reizes**.

Rezultātu atgriez saraksta veidā jebkurā secībā.

### Piemērs

```python
nums = [1,2,2,3,3,3,4]
threshold = 2

# Output: [3]
```

---

## 2. Pāru līdzsvars

### Uzdevums

Dots skaitļu saraksts `nums`.

Nosaki, vai ir iespējams sadalīt sarakstu tā, lai **katrs elements parādās pāra skaitā reižu**.

Atgriez `True` vai `False`.

### Piemērs

```python
nums = [4,4,2,2,1,1]
# Output: True
```

```python
nums = [4,4,2,2,1]
# Output: False
```

---

## 3. Rakstzīmju konflikts

### Uzdevums

Dotas divas virknes `s1` un `s2`.

Nosaki, vai abām virknēm ir **vismaz viens kopīgs simbols**.

### Piemērs

```python
s1 = "house"
s2 = "mouse"
# Output: True
```

```python
s1 = "cat"
s2 = "dog"
# Output: False
```

---

## 4. Apgriezta vārdnīca

### Uzdevums

Dots dictionary `d`, kur `key -> value`.

Izveido jaunu dictionary, kur `value -> saraksts ar visiem key`.

### Piemērs

```python
d = {
    "Anna": "Math",
    "Juris": "Math",
    "Līga": "Physics"
}

# Output:
# {
#     "Math": ["Anna", "Juris"],
#     "Physics": ["Līga"]
# }
```

---

## 5. Garākā unikālo elementu apakšvirkne

### Uzdevums

Dots veselu skaitļu saraksts `nums`.

Atgriez **garākās nepārtrauktās apakšvirknes garumu**, kur visi elementi ir unikāli.

### Piemērs

```python
nums = [1,2,3,2,4,5]
# Output: 4
# Paskaidrojums: garākā unikālā apakšvirkne ir [3,2,4,5]
```

---
