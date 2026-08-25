## 1. Maksimālā summa logā ar garumu `k`

### Uzdevums

Dots veselu skaitļu saraksts `nums` un loga izmērs `k`.

Atrodi maksimālo summu starp visiem nepārtrauktiem apakšmasīviem ar garumu tieši `k`.

### Piemērs

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3
# Output: 9
# Paskaidrojums: logs [5, 1, 3] dod summu 9
```

### Risinājums

```python
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best = max(best, window_sum)

    return best
```

---

## 2. Vidējā vērtība katrā logā

### Uzdevums

Dots veselu skaitļu saraksts `nums` un loga izmērs `k`.

Atgriez sarakstu, kur katram nepārtrauktam logam ar garumu `k` ir aprēķināta vidējā vērtība.

### Piemērs

```python
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]
```

### Risinājums

```python
def average_subarrays(nums, k):
    window_sum = sum(nums[:k])
    result = [window_sum / k]

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        result.append(window_sum / k)

    return result
```

---

## 3. Mazākais logs ar summu vismaz `target`

### Uzdevums

Dots pozitīvu veselu skaitļu saraksts `nums` un skaitlis `target`.

Atrodi mazākā nepārtrauktā apakšmasīva garumu, kura summa ir vismaz `target`.

Ja tāda apakšmasīva nav, atgriez `0`.

### Piemērs

```python
nums = [2, 1, 5, 2, 3, 2]
target = 7
# Output: 2
# Paskaidrojums: logs [5, 2] ir īsākais derīgais
```

### Risinājums

```python
def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    best = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    if best == float("inf"):
        return 0

    return best
```

---

## 4. Maksimālais patskaņu skaits logā

### Uzdevums

Dota virkne `s` un skaitlis `k`.

Atrodi lielāko patskaņu skaitu starp visām apakšvirknēm ar garumu `k`.

Par patskaņiem uzskati `a`, `e`, `i`, `o`, `u`.

### Piemērs

```python
s = "abciiidef"
k = 3
# Output: 3
# Paskaidrojums: apakšvirkne "iii" satur 3 patskaņus
```

### Risinājums

```python
def max_vowels(s, k):
    vowels = set("aeiou")
    count = 0

    for i in range(k):
        if s[i] in vowels:
            count += 1

    best = count

    for right in range(k, len(s)):
        if s[right] in vowels:
            count += 1
        if s[right - k] in vowels:
            count -= 1
        best = max(best, count)

    return best
```

---

## 5. Vai tuvumā ir dublikāts

### Uzdevums

Dots veselu skaitļu saraksts `nums` un skaitlis `k`.

Nosaki, vai eksistē divi vienādi elementi, kuru indeksu starpība ir ne lielāka par `k`.

Atgriez `True` vai `False`.

### Piemērs

```python
nums = [1, 2, 3, 1]
k = 3
# Output: True
```

```python
nums = [1, 2, 3, 1, 2, 3]
k = 2
# Output: False
```

### Risinājums

```python
def contains_nearby_duplicate(nums, k):
    window = set()
    left = 0

    for right in range(len(nums)):
        if nums[right] in window:
            return True

        window.add(nums[right])

        if right - left >= k:
            window.remove(nums[left])
            left += 1

    return False
```

---

## 6. Garākā apakšvirkne bez atkārtotiem simboliem

### Uzdevums

Dota virkne `s`.

Atgriez garumu garākajai apakšvirknei, kurā visi simboli ir unikāli.

### Piemērs

```python
s = "abcabcbb"
# Output: 3
# Paskaidrojums: "abc"
```

```python
s = "bbbbb"
# Output: 1
```

---

## 7. Garākā apakšvirkne ar ne vairāk kā `k` atšķirīgiem simboliem

### Uzdevums

Dota virkne `s` un skaitlis `k`.

Atgriez garumu garākajai apakšvirknei, kurā ir ne vairāk kā `k` atšķirīgi simboli.

### Piemērs

```python
s = "eceba"
k = 2
# Output: 3
# Paskaidrojums: "ece"
```

---

## 8. Vai virknē ir otras virknes permutācija

### Uzdevums

Dotas virknes `s1` un `s2`.

Nosaki, vai `s2` satur kādu `s1` simbolu permutāciju kā nepārtrauktu apakšvirkni.

Atgriez `True` vai `False`.

### Piemērs

```python
s1 = "ab"
s2 = "eidbaooo"
# Output: True
# Paskaidrojums: "ba" ir "ab" permutācija
```

```python
s1 = "ab"
s2 = "eidboaoo"
# Output: False
```

---

## 9. Atrast visus anagrammu sākuma indeksus

### Uzdevums

Dotas virknes `s` un `p`.

Atgriez sarakstu ar visiem indeksiem, kuros virknē `s` sākas `p` anagramma.

### Piemērs

```python
s = "cbaebabacd"
p = "abc"
# Output: [0, 6]
```

```python
s = "abab"
p = "ab"
# Output: [0, 1, 2]
```

---

## 10. Augļu grozi

### Uzdevums

Dots saraksts `fruits`, kur katrs elements apzīmē augļa tipu.

Tev ir divi grozi, un katrā drīkst glabāt tikai vienu augļa tipu.

Atgriez maksimālo augļu skaitu, ko var savākt no nepārtrauktas apakšvirknes, kurā ir ne vairāk kā divi atšķirīgi tipi.

### Piemērs

```python
fruits = [1, 2, 1]
# Output: 3
```

```python
fruits = [1, 2, 3, 2, 2]
# Output: 4
# Paskaidrojums: [2, 3, 2, 2]
```

---

## 11. Garākā vieninieku virkne pēc ne vairāk kā `k` nulles maiņām

### Uzdevums

Dots binārs saraksts `nums` un skaitlis `k`.

Tu drīksti nomainīt ne vairāk kā `k` nulles uz vieniniekiem.

Atgriez garumu garākajai nepārtrauktajai apakšvirknei, kas pēc šīm maiņām sastāv tikai no vieniniekiem.

### Piemērs

```python
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
# Output: 6
```

---

## 12. Garākā virkne pēc simbolu aizstāšanas

### Uzdevums

Dota virkne `s`, kas sastāv no lielajiem burtiem, un skaitlis `k`.

Tu drīksti aizstāt ne vairāk kā `k` simbolus tā, lai iegūtu apakšvirkni, kur visi simboli ir vienādi.

Atgriez maksimālo iespējamo šādas apakšvirknes garumu.

### Piemērs

```python
s = "AABABBA"
k = 1
# Output: 4
```

---

## 13. Mazākais logs, kas satur visus simbolus

### Uzdevums

Dotas virknes `s` un `t`.

Atrodi īsāko apakšvirkni virknē `s`, kas satur visus `t` simbolus ar pareizajiem biežumiem.

Ja tādas nav, atgriez tukšu virkni `""`.

### Piemērs

```python
s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"
```

---

## 14. Cik apakšmasīvu reizinājums ir mazāks par `k`

### Uzdevums

Dots pozitīvu veselu skaitļu saraksts `nums` un skaitlis `k`.

Atgriez, cik daudz nepārtrauktu apakšmasīvu reizinājums ir stingri mazāks par `k`.

### Piemērs

```python
nums = [10, 5, 2, 6]
k = 100
# Output: 8
```

---

## 15. Maksimums katrā bīdāmajā logā

### Uzdevums

Dots veselu skaitļu saraksts `nums` un loga izmērs `k`.

Atgriez sarakstu, kur katram logam ar garumu `k` ir dots tā maksimālais elements.

### Piemērs

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# Output: [3, 3, 5, 5, 6, 7]
```

---
