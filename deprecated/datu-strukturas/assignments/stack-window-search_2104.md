# Formatīvais vērtējums — 21.04.

---

## S1. Punkti ar bāzbola operācijām

### Uzdevums

Dots saraksts `ops`, kas sastāv no virknēm. Katra virkne ir viena no šīm operācijām:

- vesels skaitlis (piemēram, `"5"` vai `"-3"`) — pievieno šo vērtību kā **jaunu rezultātu**,
- `"+"` — pievieno jaunu rezultātu, kas ir vienāds ar **pēdējo divu** rezultātu summu,
- `"D"` — pievieno jaunu rezultātu, kas ir **divkāršs pēdējais** rezultāts,
- `"C"` — **izdzēš pēdējo** rezultātu.

Pēc visu operāciju apstrādes atgriez **visu atlikušo rezultātu summu**.

Var pieņemt, ka katra operācija ir derīga (piemēram, `"+"` vai `"D"` netiks izsaukta, ja nav pietiekami daudz iepriekšēju rezultātu).

### Piemērs

```python
ops = ["5", "2", "C", "D", "+"]
# Output: 30
# "5"  -> [5]
# "2"  -> [5, 2]
# "C"  -> [5]
# "D"  -> [5, 10]
# "+"  -> [5, 10, 15]
# Summa = 30
```

```python
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
# Output: 27
```

---

## W1. Maksimālais punktu skaits no kārtīm

### Uzdevums

Dots veselu skaitļu saraksts `cards` — kāršu punkti, kas sakārtotas rindā. Katrā solī var paņemt kārti **no saraksta sākuma** vai **no saraksta beigām**. Jāpaņem **tieši `k`** kārtis.

Atgriez maksimālo iespējamo paņemto kāršu punktu summu.

### Piemērs

```python
cards = [1, 2, 3, 4, 5, 6, 1]
k = 3
# Output: 12
# Paskaidrojums: paņemot pēdējās trīs kārtis (5, 6, 1) sanāk 12
```

```python
cards = [2, 2, 2]
k = 2
# Output: 4
```

```python
cards = [9, 7, 7, 9, 7, 7, 9]
k = 7
# Output: 55
```

---

## B1. Minimālais dalītājs ar ierobežojumu

### Uzdevums

Dots pozitīvu veselu skaitļu saraksts `nums` un skaitlis `threshold`.

Atrodi **mazāko veselo skaitli** `d`, lai summa, ko iegūst, katru `nums` elementu dalot ar `d` un noapaļojot **uz augšu**, būtu **ne lielāka par `threshold`**.

Risinājumam jādarbojas ar `O(n · log m)` sarežģītību, kur `m` ir lielākais elements `nums`.

### Piemērs

```python
nums = [1, 2, 5, 9]
threshold = 6
# Output: 5
# Paskaidrojums:
# Pie d = 4: ceil(1/4) + ceil(2/4) + ceil(5/4) + ceil(9/4) = 1 + 1 + 2 + 3 = 7  (par daudz)
# Pie d = 5: ceil(1/5) + ceil(2/5) + ceil(5/5) + ceil(9/5) = 1 + 1 + 1 + 2 = 5  (der)
```

```python
nums = [44, 22, 33, 11, 1]
threshold = 5
# Output: 44
```

---
