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

### Risinājums

```python
def dominant_with_threshold(nums, threshold):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    result = []
    for num, cnt in counts.items():
        if cnt > threshold:
            result.append(num)

    return result
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

### Risinājums

```python
def can_pair_all(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    for cnt in counts.values():
        if cnt % 2 != 0:
            return False

    return True
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

### Risinājums

```python
def has_common_symbol(s1, s2):
    seen = {}

    for ch in s1:
        seen[ch] = True

    for ch in s2:
        if ch in seen:
            return True

    return False
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

### Risinājums

```python
def invert_dict_to_lists(d):
    inverted = {}

    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)

    return inverted
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

### Risinājums

```python
def longest_unique_subarray(nums):
    last_seen = {}
    left = 0
    best = 0

    for right, num in enumerate(nums):
        if num in last_seen and last_seen[num] >= left:
            left = last_seen[num] + 1

        last_seen[num] = right
        best = max(best, right - left + 1)

    return best
```

---

## 6. Kopīgie elementi bez dublikātiem

### Uzdevums

Doti divi veselu skaitļu saraksti `nums1` un `nums2`.

Atgriez sarakstu ar elementiem, kas ir abos sarakstos, **bez dublikātiem**.

### Piemērs

```python
nums1 = [1,2,2,3]
nums2 = [2,2,4]
# Output: [2]
```

---

## 7. Divu skaitļu summa uz mērķi

### Uzdevums

Dots saraksts `nums` un skaitlis `target`.

Atgriez divu elementu indeksus, kuru summa ir `target`.

Vari pieņemt, ka risinājums vienmēr eksistē.

### Piemērs

```python
nums = [2,7,11,15]
target = 9
# Output: [0,1]
```

---

## 8. Biežākais elements

### Uzdevums

Dots veselu skaitļu saraksts `nums`.

Atgriez elementu, kas parādās visbiežāk.

Ja ir vairāki ar vienādu biežumu, vari atgriezt jebkuru no tiem.

### Piemērs

```python
nums = [5,1,5,2,5,2]
# Output: 5
```

---

## 9. Grupēšana pēc pirmā burta

### Uzdevums

Dots vārdu saraksts `words`.

Izveido dictionary, kur:

- atslēga ir vārda pirmais burts (mazajos burtos),
- vērtība ir saraksts ar visiem vārdiem, kas sākas ar šo burtu.

### Piemērs

```python
words = ["Apple", "ant", "Boat", "ball", "cat"]

# Output:
# {
#   "a": ["Apple", "ant"],
#   "b": ["Boat", "ball"],
#   "c": ["cat"]
# }
```

---

## 10. Atšķirīgo elementu skaits katrā logā

### Uzdevums

Dots saraksts `nums` un logs `k`.

Atgriez sarakstu, kur katram logam garumā `k` ir norādīts, cik tajā ir **atšķirīgu elementu**.

### Piemērs

```python
nums = [1,2,1,3,4,2,3]
k = 4
# Output: [3,4,4,3]
```

---
