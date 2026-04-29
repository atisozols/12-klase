## 1. Klasiskā binārā meklēšana

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums` un mērķa skaitlis `target`.

Atrodi `target` indeksu sarakstā. Ja elements nav atrasts, atgriez `-1`.

### Piemērs

```python
nums = [-1, 0, 3, 5, 9, 12]
target = 9
# Output: 4
```

```python
nums = [-1, 0, 3, 5, 9, 12]
target = 2
# Output: -1
```

### Risinājums

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

## 2. Ievietošanas pozīcija

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums` un mērķa skaitlis `target`.

Atrodi indeksu, kurā `target` atrodas. Ja nav atrasts, atgriez indeksu, kurā tas būtu jāievieto, lai saraksts paliktu sakārtots.

### Piemērs

```python
nums = [1, 3, 5, 6]
target = 5
# Output: 2
```

```python
nums = [1, 3, 5, 6]
target = 2
# Output: 1
```

```python
nums = [1, 3, 5, 6]
target = 7
# Output: 4
```

### Risinājums

```python
def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

---

## 3. Pirmā un pēdējā pozīcija sakārtotā masīvā

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums` un mērķa skaitlis `target`.

Atrodi `target` pirmo un pēdējo pozīciju masīvā. Ja `target` nav atrasts, atgriez `[-1, -1]`.

Risinājumam jādarbojas ar `O(log n)` sarežģītību.

### Piemērs

```python
nums = [5, 7, 7, 8, 8, 10]
target = 8
# Output: [3, 4]
```

```python
nums = [5, 7, 7, 8, 8, 10]
target = 6
# Output: [-1, -1]
```

### Risinājums

```python
def search_range(nums, target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [find_left(nums, target), find_right(nums, target)]
```

---

## 4. Kvadrātsakne

### Uzdevums

Dots nenegatīvs vesels skaitlis `x`.

Aprēķini un atgriez `x` kvadrātsakni, noapaļotu uz leju līdz tuvākajam veselam skaitlim.

Nedrīkst izmantot iebūvētās funkcijas (`math.sqrt`, `**0.5` u.c.).

### Piemērs

```python
x = 8
# Output: 2
# Paskaidrojums: sqrt(8) = 2.828..., noapaļots uz leju = 2
```

```python
x = 4
# Output: 2
```

### Risinājums

```python
def my_sqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
```

---

## 5. Atrast virsotni masīvā

### Uzdevums

Dots veselu skaitļu saraksts `nums`, kur `nums[i] != nums[i+1]`.

**Virsotne** ir elements, kas ir lielāks par saviem kaimiņiem.

Atrodi jebkuras virsotnes indeksu. Risinājumam jādarbojas ar `O(log n)` sarežģītību.

### Piemērs

```python
nums = [1, 2, 3, 1]
# Output: 2
# Paskaidrojums: nums[2] = 3 ir virsotne
```

```python
nums = [1, 2, 1, 3, 5, 6, 4]
# Output: 5
# Paskaidrojums: nums[5] = 6 ir virsotne (arī nums[1] = 2 būtu derīgs)
```

### Risinājums

```python
def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left
```

---

## 6. Meklēt pagrieztā sakārtotā masīvā

### Uzdevums

Dots sakārtots masīvs, kas ir **pagriezts** kādā nezināmā indeksā (piemēram, `[4,5,6,7,0,1,2]` ir pagriezts `[0,1,2,4,5,6,7]`).

Dots arī mērķa skaitlis `target`. Atrodi tā indeksu vai atgriez `-1`.

Risinājumam jādarbojas ar `O(log n)` sarežģītību.

### Piemērs

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# Output: 4
```

```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
# Output: -1
```

---

## 7. Minimālais elements pagrieztā masīvā

### Uzdevums

Dots sakārtots masīvs ar unikāliem elementiem, kas ir **pagriezts** kādā nezināmā indeksā.

Atrodi masīva minimālo elementu. Risinājumam jādarbojas ar `O(log n)` sarežģītību.

### Piemērs

```python
nums = [3, 4, 5, 1, 2]
# Output: 1
```

```python
nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
```

```python
nums = [11, 13, 15, 17]
# Output: 11
```

---

## 8. Atrast, cik reižu masīvs ir pagriezts

### Uzdevums

Dots sakārtots masīvs ar unikāliem elementiem, kas ir **pagriezts** kādā nezināmā indeksā.

Nosaki, cik reižu masīvs ir pagriezts (t.i., atrodi minimālā elementa indeksu).

### Piemērs

```python
nums = [3, 4, 5, 1, 2]
# Output: 3
# Paskaidrojums: minimālais elements 1 atrodas indeksā 3
```

```python
nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 4
```

```python
nums = [1, 2, 3, 4, 5]
# Output: 0
# Paskaidrojums: masīvs nav pagriezts
```

---

## 9. Pirmais slikts variants

### Uzdevums

Tu esi produkta vadītājs, un pašreizējais variants ir slikts. Katrs variants pēc pirmā sliktā varianta arī ir slikts.

Dota funkcija `is_bad(version)`, kas atgriez `True`, ja variants ir slikts.

Atrodi pirmo slikto variantu, izmantojot pēc iespējas mazāk izsaukumu.

### Piemērs

```python
n = 5
# Pirmais sliktais variants ir 4
# is_bad(3) -> False
# is_bad(4) -> True
# is_bad(5) -> True
# Output: 4
```

### Risinājums

```python
def first_bad_version(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if is_bad(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

---

## 10. Meklēt 2D matricā

### Uzdevums

Dota `m x n` matrica `matrix`, kur:

- katras rindas elementi ir sakārtoti augoši,
- katras rindas pirmais elements ir lielāks par iepriekšējās rindas pēdējo elementu.

Dots mērķa skaitlis `target`. Nosaki, vai `target` atrodas matricā.

Risinājumam jādarbojas ar `O(log(m * n))` sarežģītību.

### Piemērs

```python
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
# Output: True
```

```python
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13
# Output: False
```

---

## 11. Koko ēd banānus

### Uzdevums

Ir `n` kaudzes banānu, kur `piles[i]` ir banānu skaits `i`-tajā kaudzē. Sargs atgriezīsies pēc `h` stundām.

Koko var izvēlēties ēšanas ātrumu `k` (banāni stundā). Katrā stundā viņa izvēlas kaudzi un apēd `k` banānus. Ja kaudzē ir mazāk par `k`, viņa apēd visu un gaida līdz nākamajai stundai.

Atrodi minimālo `k`, lai Koko apēstu visus banānus `h` stundu laikā.

### Piemērs

```python
piles = [3, 6, 7, 11]
h = 8
# Output: 4
```

```python
piles = [30, 11, 23, 4, 20]
h = 5
# Output: 30
```

---

## 12. Atrast minimālo vērtību, kas apmierina nosacījumu

### Uzdevums

Dota funkcija `condition(x)`, kas atgriez `False` visiem `x < k` un `True` visiem `x >= k` (kur `k` ir nezināms).

Dots diapazons `[lo, hi]`. Atrodi mazāko `x` diapazonā, kuram `condition(x)` ir `True`.

### Piemērs

```python
# condition(x) atgriez True, ja x >= 5
lo = 1
hi = 10
# Output: 5
```

### Risinājums

```python
def binary_search_condition(lo, hi, condition):
    while lo < hi:
        mid = (lo + hi) // 2

        if condition(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo
```

---

## 13. Sadalīt masīvu ar minimālo maksimālo summu

### Uzdevums

Dots veselu skaitļu saraksts `nums` un skaitlis `k`.

Sadali `nums` tieši `k` nepārtrauktos apakšmasīvos tā, lai lielākā apakšmasīva summa būtu **minimāla**.

Atgriez šo minimālo iespējamo lielāko summu.

### Piemērs

```python
nums = [7, 2, 5, 10, 8]
k = 2
# Output: 18
# Paskaidrojums: [7, 2, 5] un [10, 8] -> summas 14 un 18 -> max = 18
```

```python
nums = [1, 2, 3, 4, 5]
k = 2
# Output: 9
# Paskaidrojums: [1, 2, 3, 4] un [5] -> summas 10 un 5 -> max = 10
# bet [1, 2, 3] un [4, 5] -> summas 6 un 9 -> max = 9
```

---

## 14. Mediāna divos sakārtotos masīvos

### Uzdevums

Doti divi sakārtoti (augoši) masīvi `nums1` un `nums2` ar garumiem `m` un `n`.

Atrodi abu masīvu apvienotā sakārtotā masīva **mediānu**.

Risinājumam jādarbojas ar `O(log(min(m, n)))` sarežģītību.

### Piemērs

```python
nums1 = [1, 3]
nums2 = [2]
# Output: 2.0
# Paskaidrojums: apvienotais masīvs = [1, 2, 3], mediāna = 2.0
```

```python
nums1 = [1, 2]
nums2 = [3, 4]
# Output: 2.5
# Paskaidrojums: apvienotais masīvs = [1, 2, 3, 4], mediāna = (2 + 3) / 2 = 2.5
```

---

## 15. Atrast k-to mazāko elementu sakārtotā matricā

### Uzdevums

Dota `n x n` matrica `matrix`, kur katras rindas un katras kolonnas elementi ir sakārtoti augoši.

Atrodi `k`-to mazāko elementu matricā.

### Piemērs

```python
matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
# Output: 13
# Paskaidrojums: sakārtoti elementi: [1, 5, 9, 10, 11, 12, 13, 13, 15], 8. mazākais = 13
```

---
