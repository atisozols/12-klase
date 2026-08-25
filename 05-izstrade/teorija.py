# ============================================================
# 05. BLOKS — PROGRAMMATŪRAS IZSTRĀDE
# ============================================================
# Šajā blokā jaunas vielas ir maz. Tā vietā ir disciplīna: kā
# uzrakstīt programmu, kuru pēc mēneša vēl var saprast, mainīt un
# pierādīt, ka tā strādā.
#
# Komentārs  # ?  nozīmē: vispirms uzmini rezultātu, tikai tad palaid.
# ============================================================

import unittest


# ============================================================
# 1. KODA STRUKTŪRA                                    [12-109]
# ============================================================
# Trīs slāņi, un atkarība iet TIKAI vienā virzienā:
#
#   saskarne  ->  loģika  ->  dati
#
#   dati/       datubāze, datnes, ārējās API
#   logika/     aprēķini, likumi, validācija
#   saskarne/   logs vai tīmekļa lapa
#
# Loģika NEZINA, vai virsū ir tkinter logs, tīmekļa lapa vai tests.
# Tieši tāpēc to var notestēt automātiski.
#
# Pārbaude: ja loģikas modulī ir `import tkinter` vai `print`, kaut kas
# ir sajaukts.

# Slikti — viss vienā:
# def apstrada():
#     summa = float(input("Summa: "))
#     if summa > 1000:
#         print("Par lielu")
#     else:
#         datubaze.saglaba(summa)

# Labi — trīs atsevišķas atbildības:
def parbaudi_summu(summa, limits=1000):
    """Loģika: atgriež kļūdas tekstu vai None, ja viss kārtībā."""
    if summa <= 0:
        return "Summai jabut pozitivai"
    if summa > limits:
        return f"Summa nedrikst parsniegt {limits}"
    return None


# ============================================================
# 2. LABĀS PRAKSES PRINCIPI                            [12-110]
# ============================================================
# Seši principi, pēc kuriem vērtē arī eksāmenā:
#
#   1) katrs priekšraksts jaunā rindā
#   2) loģiskās daļas atdalītas ar tukšu rindu
#   3) atkāpes parāda struktūru
#   4) nav garu rindu
#   5) jēgpilni nosaukumi
#   6) komentāri skaidro loģiskās daļas
#
# Papildus tam, ko prasa eksāmens:
#   - funkcija nav garāka par ekrānu (apmēram 30 rindas);
#   - funkcija dara vienu lietu; ja nosaukumā gribas «un», sadali;
#   - komentārs skaidro KĀPĒC, ne KO — «ko» jau ir kodā.
#
#   slikti:  x = x * 1.21          # reizina ar 1.21
#   labi:    cena = cena * 1.21    # PVN 21%, likme no 2011. gada


# ============================================================
# 3. VERSIJU PĀRVALDĪBA                                [12-111]
# ============================================================
# Zars ļauj strādāt pie kaut kā nepabeigta, neaiztiekot galveno versiju.
#
#   git switch -c jauna-funkcija     izveido zaru un pāriet uz to
#   git add . && git commit -m "..."  saglabā izmaiņas zarā
#   git switch main                   atgriežas galvenajā
#   git merge jauna-funkcija          pievieno izmaiņas galvenajam
#
# KONFLIKTS rodas, kad abos zaros mainīta viena un tā pati rinda.
# Git to neatrisina pats — failā parādās:
#
#   <<<<<<< HEAD
#   cena = 10
#   =======
#   cena = 12
#   >>>>>>> jauna-funkcija
#
# Tev jāizlemj, kas paliek, jāizdzēš marķieri un jāizdara commit.
#
# Labs commit apraksts pasaka, KAS mainīts un KĀPĒC:
#   slikti:  "update", "fix", "izmainijums"
#   labi:    "Pievieno validaciju pieteikumu formai"
#            "Salabo kluda, kad saraksts ir tukss"


# ============================================================
# 4. VIENĪBTESTĒŠANA                                   [12-115]
# ============================================================
# Vienībtests pārbauda VIENU funkciju atsevišķi. Tas ir kods, kas
# pārbauda kodu — un to var palaist tūkstoš reižu bez piepūles.

def videjais(skaitli):
    """Atgriež vidējo aritmētisko. Tukšam sarakstam atgriež 0."""
    if not skaitli:
        return 0
    return sum(skaitli) / len(skaitli)


def kategorija(vecums):
    if vecums < 0:
        raise ValueError("Vecums nevar but negativs")
    if vecums <= 12:
        return "berns"
    if vecums <= 18:
        return "jaunietis"
    return "pieaugusais"


class VidejaisTests(unittest.TestCase):
    def test_parasts_gadijums(self):
        self.assertEqual(videjais([4, 8, 6]), 6)

    def test_viens_elements(self):
        self.assertEqual(videjais([5]), 5)

    def test_tukss_saraksts(self):
        self.assertEqual(videjais([]), 0)          # robežgadījums

    def test_negativi_skaitli(self):
        self.assertEqual(videjais([-2, 2]), 0)


class KategorijaTests(unittest.TestCase):
    def test_robezas(self):
        self.assertEqual(kategorija(12), "berns")        # tieši uz robežas
        self.assertEqual(kategorija(13), "jaunietis")
        self.assertEqual(kategorija(18), "jaunietis")
        self.assertEqual(kategorija(19), "pieaugusais")

    def test_negativs_met_izniemumu(self):
        with self.assertRaises(ValueError):
            kategorija(-1)


# Palaiž ar:  python3 -m unittest teorija.py
#
# Testa nosaukums ir dokumentācija: no `test_tukss_saraksts` uzreiz
# redzams, ko funkcijai vajadzētu darīt tukšā gadījumā.


# ============================================================
# 5. ROBEŽGADĪJUMI                                     [12-116]
# ============================================================
# Kļūdas gandrīz vienmēr ir uz robežām, ne vidū.
#
# Ko pārbaudīt katrai funkcijai:
#   - tieši uz robežas un pa vienam uz katru pusi (12, 13 / 18, 19)
#   - tukša ievade: "", [], {}, None
#   - nulle un negatīvas vērtības
#   - viens elements
#   - ļoti liels apjoms
#
# EKVIVALENCES KLASES: nav jātestē visi 1000 gadījumi. Ja funkcija
# ar vecumu 5 un 7 rīkojas vienādi, pietiek ar vienu no tiem — plus
# robežas.


# ============================================================
# 6. ATKĻŪDOŠANA                                       [12-121]
# ============================================================
# Atkļūdošana ir izmeklēšana, ne minēšana:
#
#   1) atkārto kļūdu — precīzi, ar tiem pašiem datiem
#   2) sašaurini — kurā funkcijā tā notiek?
#   3) izvirzi hipotēzi — "es domāju, ka mainīgais te ir tukšs"
#   4) pārbaudi to — pārtraukumpunkts vai žurnāls
#   5) izlabo un uzraksti testu, lai tā neatgrieztos
#
# Žurnalēšana ir labāka par print, jo to var atstāt kodā:
#
#   import logging
#   logging.basicConfig(level=logging.INFO)
#   logging.info("Sanemts pieteikums: %s", dati)
#   logging.warning("Neizdevas saglabat: %s", kluda)
#
# Ja stundu neko neatrodi — pastāsti problēmu kādam citam skaļi.
# Puse kļūdu atrisinās stāstīšanas laikā.


# ============================================================
# 7. REFAKTORĒŠANA                                     [12-122]
# ============================================================
# Refaktorēšana ir koda uzlabošana, NEMAINOT tā uzvedību.
# Bez testiem to nedara — citādi nav zināms, vai kaut kas salūza.
#
# Biežākie paņēmieni:
#   - atkārtota koda izdalīšana funkcijā
#   - garas funkcijas sadalīšana
#   - neskaidra nosaukuma maiņa
#   - dziļi ligzdotu if pārveidošana par agrīnu return

# Pirms:
# def apstrada(pieteikums):
#     if pieteikums is not None:
#         if pieteikums.vards != "":
#             if pieteikums.vietas > 0:
#                 return saglabat(pieteikums)
#             else:
#                 return "Nederigs vietu skaits"
#         else:
#             return "Trukst varda"
#     else:
#         return "Nav pieteikuma"

# Pēc — agrīnie return, viens ligzdojuma līmenis:
def apstrada(pieteikums):
    if pieteikums is None:
        return "Nav pieteikuma"
    if not pieteikums.get("vards"):
        return "Trukst varda"
    if pieteikums.get("vietas", 0) <= 0:
        return "Nederigs vietu skaits"
    return "Saglabats"


# ============================================================
# 8. INTEGRĀCIJAS TESTĒŠANA                            [12-127]
# ============================================================
# Vienībtests pārbauda vienu funkciju. Integrācijas tests pārbauda,
# vai vairākas daļas strādā KOPĀ.
#
# Klasiskais gadījums: katra funkcija strādā, bet viena atgriež
# tekstu, kur otra gaida skaitli.
#
# class IntegracijasTests(unittest.TestCase):
#     def setUp(self):
#         """Izpildās pirms KATRA testa — sagatavo tīru vidi."""
#         self.datubaze = izveido_testa_datubazi()
#
#     def tearDown(self):
#         """Izpildās pēc katra testa — sakopj."""
#         self.datubaze.dzest()
#
#     def test_pilns_cels(self):
#         pieteikums = {"vards": "Anna", "vietas": 2}
#         apstrada_un_saglaba(pieteikums, self.datubaze)
#         saraksts = self.datubaze.visi_pieteikumi()
#         self.assertEqual(len(saraksts), 1)
#         self.assertEqual(saraksts[0]["vards"], "Anna")
#
# SVARĪGI: integrācijas testi lieto ATSEVIŠĶU testa datubāzi.
# Tests, kas sabojā īstos datus, ir sliktāks par testa neesamību.
#
# Testu piramīda: daudz ātru vienībtestu, mazāk integrācijas testu,
# vēl mazāk pilnu akcepttestu.


# ============================================================
# 9. AKCEPTTESTĒŠANA                                   [12-129]
# ============================================================
# Akcepttests atbild uz vienu jautājumu: vai SPECIFIKĀCIJAS prasība
# ir izpildīta? To raksta tabulā, ne kodā.
#
# | Nr | Prasība | Soļi | Sagaidāmais | Faktiskais | OK? |
# |----|---------|------|-------------|------------|-----|
# | F1 | Sistēma ļauj pieteikties, ja ir vietas | atver, izvēlas, apstiprina | pieteikums sarakstā | tā arī notiek | jā |
# | F3 | Nevar pieteikties, ja vietu nav | aizpilda pulciņu, mēģina vēl | paziņojums, pieteikums netiek pievienots | pieteikums TIEK pievienots | nē |
#
# Godīga tabula ar "nē" ir vērtīgāka par tabulu, kurā visur "jā", bet
# demonstrācijā izrādās citādi. "Nē" ir informācija; nepatiess "jā" ir
# problēma, kas atklāsies sliktākajā brīdī.


# ============================================================
# 10. IZVĒRŠANA UN UZTURĒŠANA                          [12-133]
# ============================================================
# IZVĒRŠANAS PLĀNS atbild: kā uzstādīt no nulles citā datorā?
#
#   1) priekšnosacījumi (Python versija, datubāze)
#   2) koda iegūšana
#   3) atkarību uzstādīšana
#   4) konfigurācija (.env, ceļi)
#   5) datubāzes izveide
#   6) palaišana
#   7) pārbaude, ka strādā
#
# Vienīgais veids, kā zināt, ka plāns ir pareizs — izmēģināt to uz
# tīras vides. Gandrīz vienmēr atklājas solis, kas «pats par sevi
# saprotams» tikai autoram.
#
# UZTURĒŠANAS PLĀNS atbild: kas jādara pēc tam?
#   - rezerves kopijas: ko, cik bieži, kur, kā pārbauda
#   - atkarību atjaunināšana
#   - žurnālu apskate
#   - ko darīt, ja sistēma nestrādā
#
# Un viens jautājums, kas atklāj visu: ja tev projekts būtu jānodod
# citam cilvēkam rīt, cik ilgi viņam vajadzētu, lai sāktu strādāt?


if __name__ == "__main__":
    unittest.main()
