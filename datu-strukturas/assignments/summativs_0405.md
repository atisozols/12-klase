# Summatīvais vērtējums — 04.05.

Pārbaudes darbs ietver visas piecas tēmas. Katram uzdevumam jāizvēlas atbilstošā datu struktūra.
Katra uzdevuma vērtēšanā 1 no 5 punktiem būs par atbilstošas datu struktūras izmantošanu.

---

## 1. Uzdevums

Dota virkne `s`.

Atrodi **pirmo simbolu**, kas virknē parādās **vairāk nekā vienu reizi**.

Atgriez šo simbolu. Ja tāda simbola nav, atgriez tukšu virkni `""`.

> Uzmanību: meklē pirmo simbolu, kas atkārtojas — nevis simbolu, kura otrā parādīšanās ir agrākā.

### Piemērs

```python
s = "abcdba"
# Output: "a"
# Paskaidrojums: 'a' parādās pozīcijās 0 un 4 — tā ir pirmā rakstzīme,
# kuru ieraugot zinām, ka tā jau ir bijusi.
```

```python
s = "abcdef"
# Output: ""
# Paskaidrojums: neviens simbols neatkārtojas
```

```python
s = "programming"
# Output: "r"
# Paskaidrojums: 'r' parādās pozīcijās 1 un 4
```

---

## 2. Uzdevums

Dota virkne `s`, kas sastāv no mazajiem un lielajiem latīņu burtiem.

Apgriez virknē **tikai patskaņus** to secībā, atstājot visus pārējos burtus tajās pašās pozīcijās.

Par patskaņiem uzskati `a`, `e`, `i`, `o`, `u` (gan mazos, gan lielos).

Atgriez jauno virkni.

Risini ar **diviem rādītājiem** no abiem galiem, neizmantojot papildu sarakstu visu patskaņu uzkrāšanai.

### Piemērs

```python
s = "hello"
# Output: "holle"
# Paskaidrojums: patskaņi ir 'e' (poz. 1) un 'o' (poz. 4) -> samainās vietām
```

```python
s = "leetcode"
# Output: "leotcede"
```

```python
s = "AEIou"
# Output: "uoIEA"
```

```python
s = "bcdfg"
# Output: "bcdfg"
# Paskaidrojums: nav neviena patskaņa
```

---

## 3. Uzdevums

Dota virkne `s` un vesels skaitlis `k`.

Atkārtoti dzēs no virknes **jebkurus `k` blakus esošus vienādus simbolus**, līdz vairs nav iespējams veikt nevienu šādu dzēšanu.

Atgriez gala virkni.

> Padoms: izmanto steku, kurā glabā pārus `[simbols, skaits]`. Kad skaits sasniedz `k`, noņem to.

### Piemērs

```python
s = "deeedbbcccbdaa"
k = 3
# Output: "aa"
# Soli pa solim:
# "deeedbbcccbdaa" -> noņem "eee" -> "ddbbcccbdaa"
# "ddbbcccbdaa"    -> noņem "ccc" -> "ddbbbdaa"
# "ddbbbdaa"       -> noņem "bbb" -> "dddaa"
# "dddaa"          -> noņem "ddd" -> "aa"
```

```python
s = "abcd"
k = 2
# Output: "abcd"
# Paskaidrojums: nav neviena pāra blakus esošu vienādu simbolu
```

```python
s = "pbbcggttciiippooaais"
k = 2
# Output: "ps"
```

---

## 4. Uzdevums

Dots veselu skaitļu saraksts `nums` un loga izmērs `k`.

Katram nepārtrauktajam logam ar garumu tieši `k` atgriez **pirmo negatīvo skaitli** šajā logā.

Ja logā nav neviena negatīva skaitļa, šai pozīcijai rezultātā ir `0`.

Risini ar bīdāmo logu un palīgrindu (queue / deque), kurā glabā tikai negatīvo skaitļu indeksus, lai algoritma sarežģītība būtu `O(n)`.

### Piemērs

```python
nums = [-8, 2, 3, -6, 10]
k = 2
# Output: [-8, 0, -6, -6]
# Logi: [-8,2] -> -8
#        [2,3]  -> nav negatīva -> 0
#        [3,-6] -> -6
#        [-6,10]-> -6
```

```python
nums = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
# Output: [-1, -1, -7, -15, -15, 0]
```

```python
nums = [1, 2, 3, 4]
k = 2
# Output: [0, 0, 0]
# Paskaidrojums: nevienā logā nav negatīva skaitļa
```

---

## 5. Uzdevums

Dots **sakārtots** (augoši) veselu skaitļu saraksts `nums`, kurā **katrs elements parādās tieši divreiz**, izņemot vienu, kas parādās tieši **vienu reizi**.

Atrodi un atgriez šo unikālo elementu.

Risinājumam jādarbojas ar `O(log n)` laika sarežģītību un `O(1)` atmiņas sarežģītību.

> Padoms: izmanto pāru indeksu īpašību. Pirms unikālā elementa pāri sākas pāra indeksos
> (`nums[2i] == nums[2i+1]`), bet aiz tā šī īpašība lūst.

### Piemērs

```python
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2
```

```python
nums = [3, 3, 7, 7, 10, 11, 11]
# Output: 10
```

```python
nums = [1, 1, 2]
# Output: 2
```

```python
nums = [0, 0, 1, 1, 2, 3, 3]
# Output: 2
```

---
