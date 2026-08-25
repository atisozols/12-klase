## 1. Pāra summa sakārtotā masīvā

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums` un mērķa skaitlis `target`.

Atrodi divus elementus, kuru summa ir tieši `target`, un atgriez to indeksus kā sarakstu `[i, j]`.

Katram ievadei ir tieši viens risinājums. Nedrīkst izmantot vienu un to pašu elementu divreiz.

### Piemērs

```python
nums = [1, 3, 4, 7, 11]
target = 8

# Output: [1, 3]
# Paskaidrojums: nums[1] + nums[3] = 3 + 7 = 8
```

### Risinājums

```python
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return []
```

---

## 2. Palindroma pārbaude

### Uzdevums

Dota virkne `s`, kas var saturēt burtus, ciparus un speciālās rakstzīmes.

Nosaki, vai virkne ir **palindroms**, ja ignorē visas rakstzīmes, kas nav burti vai cipari, un nesalīdzina lielos/mazos burtus.

Atgriez `True` vai `False`.

### Piemērs

```python
s = "A man, a plan, a canal: Panama"
# Output: True
```

```python
s = "hello"
# Output: False
```

### Risinājums

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

---

## 3. Pārvietot nulles uz beigām

### Uzdevums

Dots veselu skaitļu saraksts `nums`.

Pārvieto visas nulles uz saraksta beigām, **saglabājot pārējo elementu secību**.

Izmaiņas jāveic **uz vietas** (in-place), neatgriežot jaunu sarakstu.

### Piemērs

```python
nums = [0, 1, 0, 3, 12]
# Pēc izsaukuma: [1, 3, 12, 0, 0]
```

### Risinājums

```python
def move_zeroes(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1
```

---

## 4. Apgriezt sarakstu uz vietas

### Uzdevums

Dots saraksts `nums`.

Apgriez sarakstu pretējā secībā **uz vietas**, neizmantojot papildu sarakstu.

### Piemērs

```python
nums = [1, 2, 3, 4, 5]
# Pēc izsaukuma: [5, 4, 3, 2, 1]
```

### Risinājums

```python
def reverse_list(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

---

## 5. Noņemt dublikātus no sakārtota masīva

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums`.

Noņem dublikātus **uz vietas** tā, lai katrs elements parādās tikai vienu reizi. Atgriez jauno garumu `k`.

Pirmajiem `k` elementiem sarakstā jābūt unikālajiem elementiem to sākotnējā secībā.

### Piemērs

```python
nums = [1, 1, 2, 3, 3, 4]
# Output: 4
# Pēc izsaukuma nums pirmie 4 elementi: [1, 2, 3, 4]
```

### Risinājums

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write
```

---

## 6. Sakārtota masīva kvadrāti

### Uzdevums

Dots sakārtots (augoši) veselu skaitļu saraksts `nums` (var saturēt negatīvus skaitļus).

Atgriez jaunu sarakstu, kurā ir katra elementa **kvadrāts**, sakārtotu augošā secībā.

### Piemērs

```python
nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
```

```python
nums = [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
```

---

## 7. Trīs skaitļu summa

### Uzdevums

Dots veselu skaitļu saraksts `nums`.

Atrodi visas unikālās trijniekus `[nums[i], nums[j], nums[k]]`, kur `i != j != k` un `nums[i] + nums[j] + nums[k] == 0`.

Rezultātā nedrīkst būt dublikātu trijnieku.

### Piemērs

```python
nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

```python
nums = [0, 0, 0, 0]
# Output: [[0, 0, 0]]
```

---

## 8. Konteiners ar visvairāk ūdens

### Uzdevums

Dots saraksts `height`, kur `height[i]` ir vertikālas līnijas augstums pozīcijā `i`.

Atrodi divas līnijas, kas kopā ar x-asi veido konteineru, kurš satur **visvairāk ūdens**.

Atgriez maksimālo ūdens daudzumu.

### Piemērs

```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Paskaidrojums: līnijas ar augstumu 8 (pozīcija 1) un 7 (pozīcija 8)
# platums = 8 - 1 = 7, augstums = min(8,7) = 7, laukums = 49
```

---

## 9. Vai ir apakšvirkne

### Uzdevums

Dotas divas virknes `s` un `t`.

Nosaki, vai `s` ir **apakšvirkne** (subsequence) virknei `t`.

Apakšvirkne nozīmē, ka `s` rakstzīmes parādās `t` tajā pašā secībā, bet ne obligāti blakus.

### Piemērs

```python
s = "ace"
t = "abcde"
# Output: True
```

```python
s = "aec"
t = "abcde"
# Output: False
```

---

## 10. Sapludināt divus sakārtotus sarakstus

### Uzdevums

Doti divi sakārtoti (augoši) saraksti `nums1` un `nums2`.

Sapludini tos vienā sakārtotā sarakstā un atgriez rezultātu.

### Piemērs

```python
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
```

```python
nums1 = [1, 1, 1]
nums2 = [2, 2]
# Output: [1, 1, 1, 2, 2]
```

---

## 11. Samazināt uz vietas: noņemt konkrētu vērtību

### Uzdevums

Dots saraksts `nums` un vērtība `val`.

Noņem visus `val` gadījumus **uz vietas** un atgriez jauno garumu `k`.

Pirmajiem `k` elementiem jāsatur tikai tie elementi, kas nav vienādi ar `val`.

### Piemērs

```python
nums = [3, 2, 2, 3]
val = 3
# Output: 2
# Pēc izsaukuma nums pirmie 2 elementi: [2, 2]
```

```python
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# Output: 5
# Pēc izsaukuma nums pirmie 5 elementi: [0, 1, 3, 0, 4]
```

---

## 12. Tuvākā pāra summa mērķim

### Uzdevums

Dots veselu skaitļu saraksts `nums` un mērķa skaitlis `target`.

Atrodi trīs elementus, kuru summa ir **vistuvāk** mērķa vērtībai.

Atgriez šo summu. Pieņem, ka katram ievadei ir tieši viens risinājums.

### Piemērs

```python
nums = [-1, 2, 1, -4]
target = 1
# Output: 2
# Paskaidrojums: (-1) + 2 + 1 = 2, kas ir vistuvāk 1
```

---

## 13. Palindroms ar vienu dzēšanu

### Uzdevums

Dota virkne `s`.

Nosaki, vai virkni var padarīt par **palindromu**, izdzēšot **ne vairāk kā vienu** rakstzīmi.

Atgriez `True` vai `False`.

### Piemērs

```python
s = "abca"
# Output: True
# Paskaidrojums: var izdzēst 'b' vai 'c'
```

```python
s = "abc"
# Output: False
```

---

## 14. Sadalīt masīvu pēc pivota

### Uzdevums

Dots veselu skaitļu saraksts `nums` un skaitlis `pivot`.

Pārkārto elementus tā, lai:

- visi elementi **mazāki** par `pivot` ir pirms tā,
- visi elementi **vienādi** ar `pivot` ir vidū,
- visi elementi **lielāki** par `pivot` ir pēc tā.

Atgriez jauno sarakstu.

### Piemērs

```python
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
# Output: [9, 5, 3, 10, 10, 12, 14]
```

---

## 15. Lietus ūdens uzkrāšana

### Uzdevums

Dots saraksts `height`, kas attēlo augstumu karti.

Aprēķini, cik daudz **lietus ūdens** var uzkrāties starp stieņiem pēc lietus.

### Piemērs

```python
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Paskaidrojums:
# - Starp indeksiem 1 (augstums 1) un 3 (augstums 2): ūdens līmenis = min(1,2) = 1
#   ūdens apjoms = 1 * (3-1-1) = 1 (viena vienība indeksā 2)
# - Starp indeksiem 3 (augstums 2) un 7 (augstums 3): ūdens līmenis = min(2,3) = 2
#   ūdens apjoms = 2 * (7-3-1) - 1 = 3 (indeksos 4,5,6, bet indeksā 4 ir 1, tāpēc 2-1=1)
# - Starp indeksiem 7 (augstums 3) un 10 (augstums 2): ūdens līmenis = min(3,2) = 2
#   ūdens apjoms = 2 * (10-7-1) - 2 = 2 (indeksos 8,9, bet indeksā 8 ir 2, tāpēc 2-2=0, indeksā 9: 2-1=1)
# Kopā: 1 + 3 + 2 = 6
```

```python
height = [4, 2, 0, 3, 2, 5]
# Output: 9
# Paskaidrojums:
# - Starp indeksiem 0 (augstums 4) un 5 (augstums 5): ūdens līmenis = min(4,5) = 4
#   ūdens apjoms = 4 * (5-0-1) - (2+0+3+2) = 16 - 7 = 9
#   (indeksos 1,2,3,4 ir ūdens, bet noņemam stieņu augstumus: 4-2=2, 4-0=4, 4-3=1, 4-2=2)
#   Kopā: 2 + 4 + 1 + 2 = 9
```

---
