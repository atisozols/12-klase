## 1. Korektu iekavu pārbaude

### Uzdevums

Dota virkne `s`, kas sastāv tikai no simboliem `(`, `)`, `{`, `}`, `[` un `]`.

Nosaki, vai iekavas ir korekti atvērtas un aizvērtas.

Virkne ir korekta, ja:

- katrai atverošajai iekavai ir atbilstoša aizverošā iekava,
- iekavas aizveras pareizajā secībā.

Atgriez `True` vai `False`.

### Piemērs

```python
s = "()[]{}"
# Output: True
```

```python
s = "([)]"
# Output: False
```

### Risinājums

```python
def is_valid_parentheses(s):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0
```

---

## 2. Apgriezt virkni ar steku

### Uzdevums

Dota virkne `s`.

Izmantojot steku, atgriez virkni apgrieztā secībā.

### Piemērs

```python
s = "skola"
# Output: "aloks"
```

### Risinājums

```python
def reverse_with_stack(s):
    stack = []

    for ch in s:
        stack.append(ch)

    result = []
    while stack:
        result.append(stack.pop())

    return "".join(result)
```

---

## 3. Noņemt blakus esošos dublikātus

### Uzdevums

Dota virkne `s`.

Kamēr virknē eksistē divi vienādi blakus esoši simboli, izdzēs tos.

Atgriez gala virkni pēc visu iespējamo dzēšanu veikšanas.

### Piemērs

```python
s = "abbaca"
# Output: "ca"
```

### Risinājums

```python
def remove_adjacent_duplicates(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)
```

---

## 4. Virkņu salīdzināšana ar atpakaļdzēšanu

### Uzdevums

Dotas divas virknes `s` un `t`.

Simbols `#` nozīmē, ka jāizdzēš iepriekšējais simbols, ja tāds eksistē.

Nosaki, vai pēc visu `#` apstrādes abas virknes kļūst vienādas.

Atgriez `True` vai `False`.

### Piemērs

```python
s = "ab#c"
t = "ad#c"
# Output: True
```

```python
s = "a#c"
t = "b"
# Output: False
```

### Risinājums

```python
def backspace_compare(s, t):
    def build(text):
        stack = []

        for ch in text:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

    return build(s) == build(t)
```

---

## 5. Reverse Polish izteiksmes aprēķins

### Uzdevums

Dots saraksts `tokens`, kas satur aritmētisku izteiksmi Reverse Polish pierakstā.

Atgriez izteiksmes vērtību.

Operatori var būt `+`, `-`, `*`, `/`.

Pieņem, ka dalīšana vienmēr nozīmē dalīšanu ar noapaļošanu uz `0`.

### Piemērs

```python
tokens = ["2", "1", "+", "3", "*"]
# Output: 9
# Paskaidrojums: (2 + 1) * 3 = 9
```

```python
tokens = ["4", "13", "5", "/", "+"]
# Output: 6
# Paskaidrojums: 4 + (13 / 5) = 4 + 2 = 6
```

### Risinājums

```python
def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))

    return stack[-1]
```

---

## 6. Steks ar minimālo elementu

### Uzdevums

Izveido datu struktūru `MinStack`, kas atbalsta darbības:

- `push(val)` pievieno elementu,
- `pop()` noņem pēdējo elementu,
- `top()` atgriež pēdējo elementu,
- `get_min()` atgriež mazāko elementu stekā.

Visām darbībām jāstrādā `O(1)` laikā.

### Piemērs

```python
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.get_min()   # Output: -3
stack.pop()
stack.top()       # Output: 0
stack.get_min()   # Output: -2
```

---

## 7. Nākamais lielākais elements

### Uzdevums

Dots veselu skaitļu saraksts `nums`.

Katram elementam atrodi pirmo lielāko elementu pa labi.

Ja tāda nav, rezultātā šai pozīcijai jābūt `-1`.

Atgriez rezultātu kā sarakstu.

### Piemērs

```python
nums = [2, 1, 2, 4, 3]
# Output: [4, 2, 4, -1, -1]
```

---

## 8. Ikdienas temperatūras

### Uzdevums

Dots saraksts `temperatures`, kur `temperatures[i]` ir temperatūra `i`-tajā dienā.

Katram indeksam atgriez, cik dienas jāgaida līdz parādās siltāka diena.

Ja siltāka diena nekad nepienāk, šai pozīcijai jābūt `0`.

### Piemērs

```python
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

---

## 9. Asteroīdu sadursme

### Uzdevums

Dots saraksts `asteroids`, kur katrs skaitlis apzīmē asteroīdu.

Absolūtā vērtība ir asteroīda izmērs, bet zīme norāda kustības virzienu:

- pozitīvs skaitlis kustas pa labi,
- negatīvs skaitlis kustas pa kreisi.

Kad divi asteroīdi saduras, mazākais tiek iznīcināts. Ja abi ir vienāda izmēra, tiek iznīcināti abi.

Atgriez gala stāvokli pēc visu sadursmju apstrādes.

### Piemērs

```python
asteroids = [5, 10, -5]
# Output: [5, 10]
```

```python
asteroids = [8, -8]
# Output: []
```

---

## 10. Unix ceļa vienkāršošana

### Uzdevums

Dots absolūts failu sistēmas ceļš `path`.

Vienkāršo to, izmantojot šādus noteikumus:

- `.` nozīmē palikt tajā pašā mapē,
- `..` nozīmē atgriezties vienu līmeni augstāk,
- vairāki `/` pēc kārtas jāuztver kā viens `/`.

Atgriez vienkāršoto ceļu.

### Piemērs

```python
path = "/home//foo/"
# Output: "/home/foo"
```

```python
path = "/a/./b/../../c/"
# Output: "/c"
```

---

## 11. Dekodēt iekodētu virkni

### Uzdevums

Dota virkne `s`, kur atkārtojumi ir kodēti formā `k[apakšvirkne]`.

Tas nozīmē, ka iekavās esošā daļa jāatkārto `k` reizes.

Atgriez atkodēto virkni.

### Piemērs

```python
s = "3[a]2[bc]"
# Output: "aaabcbc"
```

```python
s = "3[a2[c]]"
# Output: "accaccacc"
```

---

## 12. Lielākais taisnstūris histogrammā

### Uzdevums

Dots saraksts `heights`, kur `heights[i]` ir histogrammas stabiņa augstums.

Atrodi lielāko iespējamo taisnstūra laukumu, ko var izveidot no blakus esošiem stabiņiem.

Atgriez šo maksimālo laukumu.

### Piemērs

```python
heights = [2, 1, 5, 6, 2, 3]
# Output: 10
```

```python
heights = [2, 4]
# Output: 4
```

---

## 13. Izdzēst `k` ciparus, lai iegūtu mazāko skaitli

### Uzdevums

Dota ciparu virkne `num` un skaitlis `k`.

Izdzēs tieši `k` ciparus tā, lai iegūtais skaitlis būtu pēc iespējas mazāks.

Atgriez rezultātu kā virkni.

Ja rezultāts ir tukšs, atgriez `"0"`.

### Piemērs

```python
num = "1432219"
k = 3
# Output: "1219"
```

```python
num = "10200"
k = 1
# Output: "200"
```

---

## 14. Akciju cenu periods

### Uzdevums

Dots saraksts `prices`, kur `prices[i]` ir akcijas cena `i`-tajā dienā.

Katram datumam atgriez, cik secīgas dienas līdz šai dienai ieskaitot cena ir bijusi mazāka vai vienāda par šīs dienas cenu.

### Piemērs

```python
prices = [100, 80, 60, 70, 60, 75, 85]
# Output: [1, 1, 1, 2, 1, 4, 6]
```

---

## 15. Cik cilvēkus redz katrs rindā

### Uzdevums

Dots saraksts `heights`, kas attēlo cilvēku augstumus rindā no kreisās uz labo pusi.

Katram cilvēkam nosaki, cik cilvēkus viņš redz pa labi.

Cilvēks redz nākamo cilvēku pa labi, ja visi cilvēki starp viņiem ir zemāki par abiem. Pirmais cilvēks, kas ir vienāds vai augstāks, joprojām ir redzams, bet aiz viņa vairs nevar redzēt.

Atgriez rezultātu kā sarakstu.

### Piemērs

```python
heights = [10, 6, 8, 5, 11, 9]
# Output: [3, 1, 2, 1, 1, 0]
```

---
