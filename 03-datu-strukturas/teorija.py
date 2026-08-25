# ============================================================
# 03. BLOKS — DATU STRUKTŪRAS, PROGRAMMSASKARNE, MAŠĪNMĀCĪŠANĀS
# ============================================================
# Eksāmenā šis ir 4. daļa — 35 % no punktiem, lielākā daļa visā darbā.
#
# Galvenais jautājums visā blokā ir viens: KURA struktūra kuram
# uzdevumam un CIK tas maksā.
#
# Komentārs  # ?  nozīmē: vispirms uzmini rezultātu, tikai tad palaid.
# ============================================================

import time
from collections import deque, namedtuple
from dataclasses import dataclass


# ============================================================
# 1. DATU STRUKTŪRU PĀRSKATS                           [12-057]
# ============================================================
# Divi jautājumi, pēc kuriem izvēlas:
#   1) vai SECĪBA ir svarīga?
#   2) kā es MEKLĒŠU — pēc pozīcijas, pēc nosaukuma vai vispār ne?
#
#   struktūra    secība   meklēšana    tipisks lietojums
#   ---------    ------   ---------    -----------------
#   saraksts     jā       lēna O(n)    virkne, kārtība, indeksi
#   kopa         nē       ātra O(1)    unikalitāte, piederība
#   vārdnīca     nē*      ātra O(1)    meklēšana pēc atslēgas
#   steks        jā       —            atsaukšana, iekavas, vēsture
#   rinda        jā       —            apkalpošana ierašanās secībā
#   koks         daļēji   O(log n)     hierarhija, sakārtota meklēšana
#   grafs        nē       —            savienojumi, maršruti
#
# * Python vārdnīca saglabā ievietošanas secību, bet uz to nepaļaujas
#   kā uz kārtošanu.


# ============================================================
# 2. SARAKSTS UN TĀ CENA                               [12-058]
# ============================================================
#   darbība              cena
#   -------              ----
#   s.append(x)          O(1)   lēti
#   s[i]                 O(1)   lēti
#   s.insert(0, x)       O(n)   visi elementi jāpabīda
#   s.pop(0)             O(n)   tas pats
#   x in s               O(n)   jāapskata visi
#   s.sort()             O(n log n)

def merit(funkcija, *args):
    """Atgriež, cik sekundes aizņēma funkcijas izpilde."""
    sakums = time.perf_counter()
    funkcija(*args)
    return time.perf_counter() - sakums


def daudz_append(n):
    s = []
    for i in range(n):
        s.append(i)


def daudz_insert(n):
    s = []
    for i in range(n):
        s.insert(0, i)


# print(round(merit(daudz_append, 50000), 4))
# print(round(merit(daudz_insert, 50000), 4))     # ?  cik reižu lēnāk?

# Pie 100 elementiem starpība nav manāma. Pie miljona tā ir starpība
# starp sekundi un stundu.


# ============================================================
# 3. KOPA                                              [12-061]
# ============================================================
# Kopā katra vērtība ir tikai vienu reizi, un piederības pārbaude ir
# ātra neatkarīgi no izmēra.

a_klase = {"Anna", "Roberts", "Elza"}
b_klase = {"Elza", "Kārlis", "Anna"}

# print(a_klase | b_klase)     # apvienojums — visi
# print(a_klase & b_klase)     # šķēlums — tie, kas abās
# print(a_klase - b_klase)     # starpība — tikai a klasē
# print(a_klase ^ b_klase)     # simetriskā starpība — tikai vienā

# Dublikātu noņemšana, SAGLABĀJOT secību — tikai ar kopu nepietiek,
# jo kopa secību nesaglabā:
def bez_dublikatiem(saraksts):
    redzets = set()
    rezultats = []
    for elements in saraksts:
        if elements not in redzets:      # O(1), nevis O(n)
            redzets.add(elements)
            rezultats.append(elements)
    return rezultats


# print(bez_dublikatiem([3, 1, 3, 7, 1, 9]))


# ============================================================
# 4. IERAKSTS                                          [12-062]
# ============================================================
# Trīs veidi, kā glabāt vienu strukturētu ierakstu.

# 1) vārdnīca — elastīga, bet neviens negarantē, kādi lauki tajā ir
skolens_v = {"vards": "Anna", "klase": "12.a", "atzime": 8}

# 2) namedtuple — nemaināms, viegls, lauki ar nosaukumiem
SkolensT = namedtuple("SkolensT", ["vards", "klase", "atzime"])
skolens_t = SkolensT("Anna", "12.a", 8)

# 3) dataclass — maināms, var pievienot metodes, ir noklusējuma vērtības
@dataclass
class Skolens:
    vards: str
    klase: str
    atzime: int = 0

    def sekmigs(self):
        return self.atzime >= 4


# print(skolens_v["vards"], skolens_t.vards, Skolens("Anna", "12.a", 8).vards)
# print(Skolens("Anna", "12.a", 3).sekmigs())     # ?

# Kāpēc ne vienkārši tuple? Jo pēc mēneša neviens neatceras, ko nozīmē
# dati[2]. Nosaukums ir dokumentācija, kas nekad nenoveco.


# ============================================================
# 5. STEKS                                             [12-063]
# ============================================================
# Pēdējais iekšā — pirmais ārā (LIFO).

class Steks:
    def __init__(self):
        self._elementi = []

    def pievienot(self, elements):
        self._elementi.append(elements)

    def iznemt(self):
        if self.ir_tukss():
            raise IndexError("Steks ir tukss")
        return self._elementi.pop()

    def apskatit(self):
        if self.ir_tukss():
            return None
        return self._elementi[-1]

    def ir_tukss(self):
        return len(self._elementi) == 0

    def __len__(self):
        return len(self._elementi)


def iekavas_sabalanseetas(teksts):
    """Pārbauda, vai iekavas ir pareizi sabalansētas."""
    pari = {")": "(", "]": "[", "}": "{"}
    steks = Steks()
    for simbols in teksts:
        if simbols in "([{":
            steks.pievienot(simbols)
        elif simbols in pari:
            if steks.ir_tukss() or steks.iznemt() != pari[simbols]:
                return False
    return steks.ir_tukss()


# print(iekavas_sabalanseetas("(a[b]{c})"))    # True
# print(iekavas_sabalanseetas("(a[b)]"))       # ?


# ============================================================
# 6. RINDA                                             [12-064]
# ============================================================
# Pirmais iekšā — pirmais ārā (FIFO).
# Parasts saraksts te neder: s.pop(0) ir O(n). deque ir O(1).

class Rinda:
    def __init__(self):
        self._elementi = deque()

    def pievienot(self, elements):
        self._elementi.append(elements)

    def apkalpot(self):
        if not self._elementi:
            raise IndexError("Rinda ir tuksa")
        return self._elementi.popleft()

    def ir_tuksa(self):
        return len(self._elementi) == 0


# r = Rinda()
# for klients in ["Anna", "Roberts", "Elza"]:
#     r.pievienot(klients)
# while not r.ir_tuksa():
#     print(r.apkalpot())      # ?  kādā secībā?


# ============================================================
# 7. SAISTĪTAIS SARAKSTS                               [12-067]
# ============================================================
# Katrs mezgls glabā vērtību un norādi uz nākamo. Masīvs glabā visu
# blakus atmiņā; saistītais saraksts — izkaisīti, savienoti ar norādēm.
#
#   [4|·]--->[8|·]--->[15|None]

class Mezgls:
    def __init__(self, vertiba):
        self.vertiba = vertiba
        self.nakamais = None


class SaistitaisSaraksts:
    def __init__(self):
        self.sakums = None

    def pievienot(self, vertiba):
        jauns = Mezgls(vertiba)
        if self.sakums is None:
            self.sakums = jauns
            return
        mezgls = self.sakums
        while mezgls.nakamais is not None:
            mezgls = mezgls.nakamais
        mezgls.nakamais = jauns

    def uz_sarakstu(self):
        rezultats = []
        mezgls = self.sakums
        while mezgls is not None:
            rezultats.append(mezgls.vertiba)
            mezgls = mezgls.nakamais
        return rezultats

    def mekle(self, vertiba):
        pozicija = 0
        mezgls = self.sakums
        while mezgls is not None:
            if mezgls.vertiba == vertiba:
                return pozicija
            mezgls = mezgls.nakamais
            pozicija += 1
        return -1


# Masīvs pret saistīto sarakstu:
#   darbība              masīvs      saistītais saraksts
#   piekļuve pēc indeksa O(1)        O(n)
#   ievietošana sākumā   O(n)        O(1)
#   meklēšana            O(n)        O(n)


# ============================================================
# 8. KOKS                                              [12-068]
# ============================================================
# Binārā meklēšanas kokā katram mezglam pa kreisi ir mazākie,
# pa labi — lielākie. Tāpēc meklēšana ir O(log n).

class KokaMezgls:
    def __init__(self, vertiba):
        self.vertiba = vertiba
        self.pa_kreisi = None
        self.pa_labi = None


class BinaraisKoks:
    def __init__(self):
        self.sakne = None

    def pievienot(self, vertiba):
        self.sakne = self._pievienot(self.sakne, vertiba)

    def _pievienot(self, mezgls, vertiba):
        if mezgls is None:
            return KokaMezgls(vertiba)
        if vertiba < mezgls.vertiba:
            mezgls.pa_kreisi = self._pievienot(mezgls.pa_kreisi, vertiba)
        elif vertiba > mezgls.vertiba:
            mezgls.pa_labi = self._pievienot(mezgls.pa_labi, vertiba)
        return mezgls

    def mekle(self, vertiba):
        mezgls = self.sakne
        while mezgls is not None:
            if vertiba == mezgls.vertiba:
                return True
            mezgls = mezgls.pa_kreisi if vertiba < mezgls.vertiba else mezgls.pa_labi
        return False

    # ========================================================
    # 9. KOKA APSTAIGĀŠANA                             [12-069]
    # ========================================================
    def in_order(self):
        """Kreisais - mezgls - labais. Dod SAKĀRTOTU virkni."""
        rezultats = []
        self._in_order(self.sakne, rezultats)
        return rezultats

    def _in_order(self, mezgls, rezultats):
        if mezgls is None:
            return                      # <- bāzes gadījums
        self._in_order(mezgls.pa_kreisi, rezultats)
        rezultats.append(mezgls.vertiba)
        self._in_order(mezgls.pa_labi, rezultats)

    def dzilums(self):
        return self._dzilums(self.sakne)

    def _dzilums(self, mezgls):
        if mezgls is None:
            return 0
        return 1 + max(self._dzilums(mezgls.pa_kreisi), self._dzilums(mezgls.pa_labi))


# Rekursijā vienmēr ir divi jautājumi:
#   1) kad funkcija beidz sevi izsaukt? (bāzes gadījums)
#   2) kā uzdevums kļūst mazāks katrā izsaukumā?


# ============================================================
# 10. GRAFS                                            [12-070]
# ============================================================
# Grafs ir virsotnes un savienojumi. Atšķirībā no koka tajā var būt
# cikli un vairāki ceļi starp divām virsotnēm.

grafs = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}


def bfs(grafs, sakums):
    """Apstaigāšana plašumā — ar RINDU."""
    apmekletas = [sakums]
    rinda = deque([sakums])
    while rinda:
        virsotne = rinda.popleft()
        for kaimins in grafs[virsotne]:
            if kaimins not in apmekletas:
                apmekletas.append(kaimins)
                rinda.append(kaimins)
    return apmekletas


def dfs(grafs, virsotne, apmekletas=None):
    """Apstaigāšana dziļumā — ar REKURSIJU (jeb steku)."""
    if apmekletas is None:
        apmekletas = []
    apmekletas.append(virsotne)
    for kaimins in grafs[virsotne]:
        if kaimins not in apmekletas:
            dfs(grafs, kaimins, apmekletas)
    return apmekletas


def isakais_cels(grafs, no_virsotnes, uz_virsotni):
    """BFS atrod īsāko ceļu, jo iet pa slāņiem."""
    rinda = deque([[no_virsotnes]])
    apmekletas = {no_virsotnes}
    while rinda:
        cels = rinda.popleft()
        if cels[-1] == uz_virsotni:
            return cels
        for kaimins in grafs[cels[-1]]:
            if kaimins not in apmekletas:
                apmekletas.add(kaimins)
                rinda.append(cels + [kaimins])
    return None


# print(bfs(grafs, "A"))
# print(dfs(grafs, "A"))
# print(isakais_cels(grafs, "A", "E"))     # ?


# ============================================================
# 11. MEKLĒŠANA                                        [12-073]
# ============================================================

def lineara_meklesana(saraksts, vertiba):
    """O(n) — apskata visus pēc kārtas."""
    for i, elements in enumerate(saraksts):
        if elements == vertiba:
            return i
    return -1


def binara_meklesana(sakartots, vertiba):
    """O(log n) — katrā solī atmet pusi. Saraksts JĀBŪT sakārtotam."""
    kreisais, labais = 0, len(sakartots) - 1
    while kreisais <= labais:
        vidus = (kreisais + labais) // 2
        if sakartots[vidus] == vertiba:
            return vidus
        if sakartots[vidus] < vertiba:
            kreisais = vidus + 1
        else:
            labais = vidus - 1
    return -1


# Miljonam elementu lineārā meklēšana sliktākajā gadījumā apskata
# 1 000 000 elementu, binārā — 20.


# ============================================================
# 12. KĀRTOŠANA                                        [12-074]
# ============================================================

def burbulkartosana(saraksts):
    """O(n²) — divi ligzdoti cikli."""
    s = saraksts[:]
    for i in range(len(s)):
        for j in range(len(s) - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s


def ievietosanas_kartosana(saraksts):
    """O(n²), bet gandrīz sakārtotiem datiem tuvu O(n)."""
    s = saraksts[:]
    for i in range(1, len(s)):
        vertiba = s[i]
        j = i - 1
        while j >= 0 and s[j] > vertiba:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = vertiba
    return s


def sapludinasanas_kartosana(saraksts):
    """O(n log n) — sadala uz pusēm un sapludina."""
    if len(saraksts) <= 1:
        return saraksts
    vidus = len(saraksts) // 2
    kreisa = sapludinasanas_kartosana(saraksts[:vidus])
    laba = sapludinasanas_kartosana(saraksts[vidus:])
    return _sapludinat(kreisa, laba)


def _sapludinat(a, b):
    rezultats = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            rezultats.append(a[i]); i += 1
        else:
            rezultats.append(b[j]); j += 1
    return rezultats + a[i:] + b[j:]


# Praksē vienmēr lieto sorted() — tas ir O(n log n) un uzrakstīts C
# valodā. Pašam kārtošanu raksta, lai saprastu, kā tā strādā.


# ============================================================
# 13. SAREŽĢĪTĪBA                                      [12-075]
# ============================================================
#   O(1)         nemainās ar n            vārdnīcas piekļuve
#   O(log n)     dalīšana uz pusēm        binārā meklēšana
#   O(n)         viens cikls              summa, meklēšana
#   O(n log n)   kārtošana                sorted()
#   O(n²)        divi ligzdoti cikli      burbuļkārtošana
#
# Kā nolasīt no koda:
#   viens cikls pa n            -> O(n)
#   cikls ciklā, abi pa n       -> O(n²)
#   katrā solī n dalās uz pusēm -> O(log n)
#
# Konstantes neraksta: O(2n) ir O(n). Svarīgi ir, kā aug, ne cik.
#
# Pie n = 1 000 000:
#   O(n)      apmēram miljons darbību
#   O(n²)     apmēram triljons — nepagaidīsi


# ============================================================
# 14. API LIETOŠANA                                    [12-079]
# ============================================================
# Svešas API un bibliotēkas riski:
#   1) tā var pārstāt strādāt vai mainīties bez brīdinājuma;
#   2) tā var tikt pamesta un vairs netikt labota;
#   3) tā var ievilkt desmitiem citu atkarību;
#   4) tajā var būt ievainojamība, kas kļūst par tavas sistēmas problēmu.
#
# Tāpēc: sveša atbilde vienmēr jāpārbauda, pirms to lieto.
#
# import requests
#
# def iegut(adrese, params=None):
#     try:
#         atbilde = requests.get(adrese, params=params, timeout=5)
#     except requests.exceptions.RequestException:
#         return None
#     if atbilde.status_code != 200:
#         return None
#     dati = atbilde.json()
#     if "results" not in dati:          # <- pārbaudi struktūru!
#         return None
#     return dati["results"]


# ============================================================
# 15. SAVA API                                         [12-080]
# ============================================================
# Tagad tu esi tas, kurš atbild.
#
# from flask import Flask, request, jsonify
# app = Flask(__name__)
#
# @app.get("/api/skoleni")
# def skoleni():
#     klase = request.args.get("klase")
#     limits = int(request.args.get("limit", 50))
#     rindas = datubaze_vaicajums(klase, limits)
#     return jsonify({"skaits": len(rindas), "dati": rindas})
#
# @app.get("/api/skoleni/<int:id>")
# def skolens(id):
#     ieraksts = atrast(id)
#     if ieraksts is None:
#         return jsonify({"kluda": "Nav atrasts"}), 404
#     return jsonify(ieraksts)
#
# Laba API atbilde ir PAREDZAMA: vienmēr viena un tā pati struktūra,
# arī kļūdas gadījumā. Tad klientam nav jāmin.
#
# Lappušošana (limit un offset) vajadzīga tāpēc, ka 100 000 ierakstu
# vienā atbildē nav noderīgi nevienam.


# ============================================================
# 16. API DROŠĪBA                                      [12-081]
# ============================================================
# API atslēga identificē, KURŠ prasa. Tā ir kā parole:
#   - nekad kodā, tikai .env;
#   - nekad repozitorijā;
#   - nekad čatā vai e-pastā — komandā to nodod ar paroļu pārvaldnieku;
#   - ja noplūdusi, to atsauc un ģenerē jaunu. Dzēst komitu nepietiek.
#
# Pieprasījumu ierobežošana (rate limiting) ir drošības jautājums:
# bez tā viens klients var pārslogot serveri vai lēni izvilkt visus datus.


# ============================================================
# 17. MAŠĪNMĀCĪŠANĀS                                   [12-082]
# ============================================================
# Algoritms:  cilvēks uzraksta LIKUMUS, programma tos izpilda.
# Modelis:    cilvēks dod PIEMĒRUS, programma atrod likumus pati.
#
# Vadītā mācīšanās      dati ar atbildēm    "šis ir surogātpasts, šis nav"
# Nevadītā mācīšanās    dati bez atbildēm   "sagrupē šos klientus pēc līdzības"
#
# Datus sadala divās daļās:
#   apmācības dati   — uz tiem modelis mācās
#   pārbaudes dati   — uz tiem pārbauda; modelis tos NAV redzējis
#
# Ja to nedara, sanāk PĀRMĀCĪŠANĀS: modelis iemācās apmācības datus
# no galvas un uz jauniem datiem strādā slikti.
#
# Rezultāta kvalitāte ir tik laba, cik dati:
#   - par maz datu       -> modelis neko nav iemācījies
#   - neobjektīvi dati   -> modelis atkārto to pašu neobjektivitāti
#   - nepilnīgi dati     -> modelis kļūdās tieši tur, kur datu trūka
#
# Ētikas jautājumi, uz kuriem jāatbild pirms lietošanas:
#   Kas atbild par kļūdu? Vai cilvēks var saprast, kāpēc modelis tā lēma?
#   Vai lēmumu var pārsūdzēt?
