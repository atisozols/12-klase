# ============================================================
# 01. BLOKS — OBJEKTORIENTĒTĀ PROGRAMMĒŠANA UN BIBLIOTĒKAS
# ============================================================
# 11. klasē klases un objekti bija paņēmiens, kā sakārtot datus.
# Šeit tie kļūst par projektēšanas valodu: abstrakcija, iekapsulēšana,
# mantošana un polimorfisms ir četri principi, pēc kuriem izvēlas,
# KĀ programmu sadalīt.
#
# Eksāmenā šis ir 3. daļa — 31 % no punktiem.
#
# Komentārs  # ?  nozīmē: vispirms uzmini, ko rinda izvadīs, tikai tad palaid.
# ============================================================

from abc import ABC, abstractmethod
from collections import Counter, defaultdict
from datetime import date


# ============================================================
# 1. ATKĀRTOJUMS                                       [12-001]
# ============================================================
# Klase ir veidne, objekts ir eksemplārs.
#   __init__   izpildās objekta izveides brīdī
#   self       ir pats objekts, uz kura izsaukta metode
#
# Metode, kas kaut ko aprēķina, ATGRIEŽ vērtību.
# Metode, kas maina stāvokli, bieži atgriež True/False.


# ============================================================
# 2. KLASE, OBJEKTS, KONSTRUKTORS                      [12-002]
# ============================================================

class Rezervacija:
    def __init__(self, vards, datums, vietu_skaits=1):
        self.vards = vards
        self.datums = datums
        self.vietu_skaits = vietu_skaits

    def apraksts(self):
        return f"{self.vards} — {self.datums}, {self.vietu_skaits} vietas"

    def mainit_vietas(self, jauns_skaits):
        if jauns_skaits < 1:
            return False
        self.vietu_skaits = jauns_skaits
        return True


# r = Rezervacija("Anna", "2026-09-15", 3)
# print(r.apraksts())
# print(r.mainit_vietas(0))     # ?
# print(r.vietu_skaits)         # ?


# ============================================================
# 3. VAIRĀKI OBJEKTA IZVEIDES VEIDI                    [12-003]
# ============================================================
# C# un Java valodā klasei var būt vairāki konstruktori ar dažādiem
# parametriem. Python tā nav — tur ir viens __init__.
#
# Tā vietā lieto divus paņēmienus:
#   1) noklusējuma vērtības parametros;
#   2) @classmethod kā alternatīvu izveides veidu.

class Lidojums:
    def __init__(self, numurs, galamerkis, vietu_skaits=100):
        self.numurs = numurs
        self.galamerkis = galamerkis
        self.vietu_skaits = vietu_skaits

    @classmethod
    def no_rindas(cls, rinda):
        """Izveido objektu no CSV rindas: BT101,Riga,180"""
        lauki = rinda.strip().split(",")
        return cls(lauki[0], lauki[1], int(lauki[2]))

    @classmethod
    def tuksa(cls):
        """Izveido tukšu lidojumu ar noklusējuma vērtībām."""
        return cls("---", "nav noteikts")


# a = Lidojums("BT101", "Riga", 180)
# b = Lidojums.no_rindas("BT202,Vilnius,120")
# c = Lidojums.tuksa()
# print(a.vietu_skaits, b.galamerkis, c.numurs)

# cls ir tas pats, kas self, tikai attiecas uz KLASI, nevis objektu.
# Tāpēc cls(...) izsauc __init__ un atgriež jaunu objektu.


# ============================================================
# 4. IEKAPSULĒŠANA                                     [12-004]
# ============================================================
# Iekapsulēšana nozīmē, ka objekta iekšējais stāvoklis ir pasargāts:
# to maina tikai caur metodēm, kuras zina, kas ir atļauts.
#
# Python vienošanās: apakšsvītra priekšā nozīmē "iekšējs".

class Konts:
    def __init__(self, ipasnieks, atlikums=0):
        self.ipasnieks = ipasnieks
        self._atlikums = atlikums

    @property
    def atlikums(self):
        """Atlikumu var LASĪT kā parastu atribūtu."""
        return self._atlikums

    @atlikums.setter
    def atlikums(self, vertiba):
        """Bet mainīt — tikai caur pārbaudi."""
        if vertiba < 0:
            raise ValueError("Atlikums nevar but negativs")
        self._atlikums = vertiba

    def ieskaitit(self, summa):
        if summa <= 0:
            return False
        self._atlikums += summa
        return True


# k = Konts("Anna", 50)
# print(k.atlikums)         # 50   — lasa kā atribūtu, bet izsauc metodi
# k.atlikums = 100          # iet caur setter
# print(k.atlikums)
# k.atlikums = -5           # ?


# ============================================================
# 5. MANTOŠANA                                         [12-007]
# ============================================================
# Apakšklase pārņem virsklases atribūtus un metodes un var tās
# papildināt vai pārrakstīt.

class Transportlidzeklis:
    def __init__(self, marka, gads):
        self.marka = marka
        self.gads = gads

    def apraksts(self):
        return f"{self.marka} ({self.gads})"

    def parvietojas(self):
        return "parvietojas"


class Automasina(Transportlidzeklis):
    def __init__(self, marka, gads, degviela):
        super().__init__(marka, gads)      # virsklases konstruktors
        self.degviela = degviela

    def parvietojas(self):                 # pārraksta virsklases metodi
        return "brauc pa celu"


class Velosipeds(Transportlidzeklis):
    def parvietojas(self):
        return "brauc ar kajam"


# a = Automasina("Toyota", 2020, "benzins")
# v = Velosipeds("Merida", 2023)
# print(a.apraksts(), "|", a.parvietojas())
# print(v.apraksts(), "|", v.parvietojas())
# print(v.degviela)         # ?

# Mantošana ir pareizā atbilde tikai tad, ja apakšklase TIEŠĀM ir
# virsklases paveids. "Automašīna ir transportlīdzeklis" — der.
# "Ritenis ir automašīna" — neder, tā ir daļa, ne paveids.


# ============================================================
# 6. POLIMORFISMS                                      [12-008]
# ============================================================
# Viens un tas pats izsaukums dažādiem objektiem dara dažādas lietas.
# Kods, kas tos lieto, par to nezina un tam nav jāzina.

# transportlidzekli = [a, v, Automasina("Skoda", 2018, "dizelis")]
# for tl in transportlidzekli:
#     print(tl.apraksts(), "-", tl.parvietojas())

# Tieši tāpēc funkcija, kas strādā ar sarakstu, NAV jāmaina, kad
# pievieno jaunu apakšklasi. Tā ir polimorfisma praktiskā jēga.

def kopejais_laukums(figuras):
    """Strādā ar jebkuru objektu, kuram ir metode laukums()."""
    return sum(figura.laukums() for figura in figuras)


# ============================================================
# 7. ABSTRAKCIJA                                       [12-009]
# ============================================================
# Abstrakta klase nosaka, KO apakšklasēm jāprot, bet nepasaka, KĀ.
# No tās pašas objektu izveidot nevar.

class Figura(ABC):
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums

    @abstractmethod
    def laukums(self):
        """Katrai figūrai savs aprēķins."""

    def apraksts(self):
        return f"{self.nosaukums}: {self.laukums():.2f}"


class Kvadrats(Figura):
    def __init__(self, mala):
        super().__init__("kvadrats")
        self.mala = mala

    def laukums(self):
        return self.mala ** 2


class Rinkis(Figura):
    def __init__(self, radiuss):
        super().__init__("rinkis")
        self.radiuss = radiuss

    def laukums(self):
        return 3.14159 * self.radiuss ** 2


# print(Kvadrats(4).apraksts())
# print(Rinkis(2).apraksts())
# print(kopejais_laukums([Kvadrats(4), Rinkis(2)]))
# f = Figura("figura")      # ?  ko dara šī rinda?

# Četri principi vienā teikumā katrs:
#   ABSTRAKCIJA      slēpj detaļas un rāda tikai to, kas vajadzīgs
#   IEKAPSULĒŠANA    tur datus un darbības kopā un pasargā stāvokli
#   MANTOŠANA        ļauj apakšklasei pārņemt virsklases uzvedību
#   POLIMORFISMS     ļauj vienu izsaukumu dažādiem objektiem


# ============================================================
# 8. STANDARTA BIBLIOTĒKA                              [12-013]
# ============================================================
# Counter — biežuma skaitīšana vienā rindā
# print(Counter("programmesana"))
# print(Counter("programmesana").most_common(3))

# defaultdict — vārdnīca, kurā nav jāpārbauda, vai atslēga jau ir
# grupas = defaultdict(list)
# for skolens in [("Anna", "11.a"), ("Roberts", "11.b"), ("Elza", "11.a")]:
#     grupas[skolens[1]].append(skolens[0])
# print(dict(grupas))

# pathlib — ceļi un datnes
# from pathlib import Path
# for datne in Path(".").glob("*.py"):
#     print(datne.name, datne.stat().st_size)

# datetime — datumi
# print((date(2027, 5, 14) - date.today()).days)


# ============================================================
# 9. ĀRĒJĀS BIBLIOTĒKAS                                [12-014]
# ============================================================
# Pirms svešas bibliotēkas pievienošanas projektam pārbaudi:
#
#   1) UZTURĒŠANA   kad pēdējais atjauninājums? Vairāk par 2 gadiem — brīdinājums
#   2) LICENCE      vai tā atļauj to, ko tu gribi darīt?
#   3) LIETOTĀJI    cik projektu to lieto? Vai kāds ir atradis problēmas?
#   4) DOKUMENTĀCIJA vai ir piemēri, vai tikai funkciju saraksts?
#
# Riski: liekais kods, ievainojamības, atkarību ķēde. Viena bibliotēka
# var ievilkt desmitiem citu, kuras tu nekad neesi redzējis.
#
# Virtuālā vide un requirements.txt:
#   python3 -m venv vide
#   source vide/bin/activate
#   pip install <bibliotēka>
#   pip freeze > requirements.txt


# ============================================================
# 10. GRAFISKĀ SASKARNE: PAMATI                        [12-015]
# ============================================================
# tkinter nāk līdzi Python — nekas nav jāuzstāda.
#
# import tkinter as tk
#
# logs = tk.Tk()
# logs.title("Rezervacijas")
#
# tk.Label(logs, text="Vards:").grid(row=0, column=0)
# vards_lauks = tk.Entry(logs)
# vards_lauks.grid(row=0, column=1)
#
# tk.Label(logs, text="Vietas:").grid(row=1, column=0)
# vietas_lauks = tk.Entry(logs)
# vietas_lauks.grid(row=1, column=1)
#
# rezultats = tk.Label(logs, text="")
# rezultats.grid(row=3, column=0, columnspan=2)
#
# logs.mainloop()          # <- programma paliek atvērta un gaida
#
# mainloop() ir tas pats, kas serverim listen(): programma negaidīti
# "neapstājas", tā gaida lietotāja darbības.


# ============================================================
# 11. GRAFISKĀ SASKARNE: NOTIKUMI                      [12-016]
# ============================================================
# Poga izsauc funkciju. Funkcija nolasa laukus, izsauc KLASES metodi
# un parāda rezultātu.
#
# def rezerve():
#     try:
#         skaits = int(vietas_lauks.get())
#     except ValueError:
#         rezultats.config(text="Vietu skaitam jabut skaitlim")
#         return
#
#     if lidojums.rezervet(skaits):
#         rezultats.config(text=f"Rezervets. Brivas: {lidojums.brivas_vietas()}")
#     else:
#         rezultats.config(text="Nepietiek brivu vietu")
#
# tk.Button(logs, text="Rezervet", command=rezerve).grid(row=2, column=1)
#
# SVARĪGI: saskarnes funkcijā NAV aprēķinu. Tā nolasa, izsauc metodi
# un parāda. Visa loģika paliek klasē — tad to var testēt bez loga.


# ============================================================
# 12. DATU GLABĀŠANA                                   [12-019]
# ============================================================
# Objekts -> vārdnīca -> JSON un atpakaļ.

class Prece:
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena

    def uz_vardnicu(self):
        return {"nosaukums": self.nosaukums, "cena": self.cena}

    @classmethod
    def no_vardnicas(cls, dati):
        return cls(dati["nosaukums"], dati["cena"])


# import json
#
# preces = [Prece("Piens", 1.09), Prece("Maize", 2.45)]
#
# with open("preces.json", "w", encoding="utf-8") as datne:
#     json.dump([p.uz_vardnicu() for p in preces], datne, ensure_ascii=False, indent=2)
#
# with open("preces.json", "r", encoding="utf-8") as datne:
#     atjaunotas = [Prece.no_vardnicas(d) for d in json.load(datne)]
#
# print(atjaunotas[0].nosaukums)


# ============================================================
# 13. IZŅĒMUMI                                         [12-020]
# ============================================================
# Savs izņēmuma tips padara kļūdu apstrādi precīzu: var noķert tieši
# to, ko gaidi, nevis visu pēc kārtas.

class NepietiekVietuError(Exception):
    """Met, ja pieprasīts vairāk vietu, nekā ir brīvu."""


class LidojumsArIznemumiem:
    def __init__(self, numurs, vietu_skaits):
        self.numurs = numurs
        self.vietu_skaits = vietu_skaits
        self.rezervetas = 0

    def rezervet(self, skaits):
        if skaits > self.vietu_skaits - self.rezervetas:
            raise NepietiekVietuError(
                f"Brivas tikai {self.vietu_skaits - self.rezervetas} vietas")
        self.rezervetas += skaits


# l = LidojumsArIznemumiem("BT101", 5)
# try:
#     l.rezervet(10)
# except NepietiekVietuError as kluda:
#     print("Neizdevas:", kluda)
# finally:
#     print("Rezervetas:", l.rezervetas)

# Kad atgriezt False un kad mest izņēmumu?
#   False        — gaidāms, normāls gadījums (vietu nepietiek)
#   izņēmums     — kaut kas, kam nevajadzēja notikt (nederīgi dati, bojāta datne)
