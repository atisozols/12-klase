# ============================================================
# 02. BLOKS — DATUBĀZE NO PYTHON (sqlite3)
# ============================================================
# 11. klasē SQL rakstījām sqlite3 konsolē un no JavaScript ar knex.
# Tagad to pašu darām no Python. SQL valoda ir tā pati — mainās tikai
# tas, kā vaicājumu aizsūta un kā saņem atbildi.
#
# Šis fails ir piemēri stundām 12-033 un 12-034. Pārējā bloka
# teorija (ER modelis, normalizācija, drošība, tīkls) ir teorija.md.
#
# Datubāze te tiek veidota atmiņā (":memory:"), tāpēc failu var
# palaist cik reižu grib — katru reizi sākas no tīras lapas.
#
# Komentārs  # ?  nozīmē: vispirms uzmini, ko rinda izvadīs, tikai tad palaid.
# ============================================================

import sqlite3


# ============================================================
# 1. SAVIENOJUMS UN PIRMAIS VAICĀJUMS                  [12-033]
# ============================================================
# Visa sqlite3 darbība ir trīs soļos:
#   con = sqlite3.connect("fails.db")   atver (vai izveido) datubāzi
#   con.execute("SQL", (parametri,))    izpilda vaicājumu
#   .fetchall() / .fetchone()           paņem rezultātu
#
# isolation_level=None nozīmē: katra izmaiņa saglabājas UZREIZ.
# Transakcijas (§9) tad sāc pats ar BEGIN. Ja internetā redzi kodu ar
# con.commit() — tas ir otrs režīms, kurā izmaiņas jāapstiprina ar roku
# un kurā visbiežākā kļūda ir "dati nesaglabājās".

con = sqlite3.connect(":memory:", isolation_level=None)
con.execute("PRAGMA foreign_keys = ON")   # SVARĪGI — skat. §3

rinda = con.execute("SELECT 2 + 3, upper('sveiki'), date('now')").fetchone()
# print(rinda)        # ?   — viena rinda ir korte (tuple)


def radit(sql, parametri=()):
    """Izpilda vaicājumu un izdrukā rezultātu kā tabulu."""
    kursors = con.execute(sql, parametri)
    kolonnas = [k[0] for k in kursors.description]
    rindas = kursors.fetchall()
    print(" | ".join(kolonnas))
    for r in rindas:
        print(" | ".join(str(v) for v in r))
    print(f"({len(rindas)} rindas)\n")


# ============================================================
# 2. SQL ATGĀDNE                                       [12-033]
# ============================================================
# SELECT daļu SECĪBA vienmēr ir šāda (ne visas ir obligātas):
#
#   SELECT    kolonnas, COUNT(*), AVG(x)    ko rādīt
#   FROM      tabula
#   JOIN      cita ON cita.id = tabula.cita_id
#   WHERE     nosacījums rindām             pirms grupēšanas
#   GROUP BY  kolonna                       kā grupēt
#   HAVING    nosacījums grupām             pēc grupēšanas
#   ORDER BY  kolonna DESC                  kārtošana
#   LIMIT     5                             cik rindu
#
# WHERE pret HAVING:  WHERE atlasa RINDAS, HAVING atlasa GRUPAS.
#   WHERE atzime >= 9            — tikai labās atzīmes
#   HAVING AVG(atzime) >= 9      — tikai tie, kam VIDĒJĀ ir laba
#
# JOIN pret LEFT JOIN:
#   JOIN       — tikai rindas, kurām ir pāris otrā tabulā
#   LEFT JOIN  — visas kreisās tabulas rindas; ja pāra nav, labajā NULL
#   "kuriem NAV neviena ..." = LEFT JOIN ... WHERE otra.id IS NULL
#
# COUNT(*) skaita rindas, COUNT(kolonna) — tikai tās, kur nav NULL.
# Ar LEFT JOIN tas ir svarīgi: tukšai grupai COUNT(*) būs 1, nevis 0.
#
# NULL salīdzina ar IS NULL / IS NOT NULL, nekad ar = NULL.


# ============================================================
# 3. TABULAS AR IEROBEŽOJUMIEM                         [12-033]
# ============================================================
# Ierobežojums ir noteikums, ko pārbauda PATI datubāze — neatkarīgi no
# tā, cik kļūdaina ir programma, kas datus ieraksta.
#
#   PRIMARY KEY     unikāls identifikators
#   REFERENCES      ārējā atslēga — vērtībai jāeksistē citā tabulā
#   NOT NULL        lauks nedrīkst būt tukšs
#   UNIQUE          divās rindās nedrīkst būt vienāda vērtība
#   CHECK (...)     jebkurš nosacījums, kam jābūt patiesam
#   DEFAULT ...     vērtība, ja to nenorāda
#
# SQLite īpatnība: ārējās atslēgas pēc noklusējuma NETIEK pārbaudītas!
# Tāpēc katru savienojumu sāc ar  PRAGMA foreign_keys = ON.
#
# Piemērs: neliels interneta veikals. Pasūtījumā var būt daudz preču,
# prece var būt daudzos pasūtījumos — N:M, tāpēc starptabula.

SHEMA = """
CREATE TABLE klienti (
    id      INTEGER PRIMARY KEY,
    vards   TEXT NOT NULL,
    epasts  TEXT NOT NULL UNIQUE
);

CREATE TABLE preces (
    id        INTEGER PRIMARY KEY,
    nosaukums TEXT NOT NULL UNIQUE,
    cena      REAL NOT NULL CHECK (cena > 0),
    atlikums  INTEGER NOT NULL DEFAULT 0 CHECK (atlikums >= 0)
);

CREATE TABLE pasutijumi (
    id         INTEGER PRIMARY KEY,
    klients_id INTEGER NOT NULL REFERENCES klienti(id),
    datums     TEXT NOT NULL DEFAULT (date('now'))
);

-- starptabula: primārā atslēga ir abu ārējo atslēgu pāris
CREATE TABLE pasutijuma_rindas (
    pasutijums_id INTEGER NOT NULL REFERENCES pasutijumi(id),
    prece_id      INTEGER NOT NULL REFERENCES preces(id),
    daudzums      INTEGER NOT NULL CHECK (daudzums > 0),
    cena          REAL NOT NULL,   -- kāpēc cena arī šeit? (situāciju krājums, N10)
    PRIMARY KEY (pasutijums_id, prece_id)
);
"""

con.executescript(SHEMA)   # executescript izpilda vairākus vaicājumus pēc kārtas

# Kādas tabulas ir datubāzē? Tās glabājas speciālā tabulā sqlite_master.
# radit("SELECT name FROM sqlite_master WHERE type = 'table'")       # ?


# ============================================================
# 4. DATU IEVIETOŠANA                                  [12-033]
# ============================================================
# Vērtības vaicājumā NEKAD neieliek ar f-string. Vietā raksta ?, un
# vērtības padod atsevišķi. Kāpēc tieši tā — 12-039 (SQL injekcija).

con.execute("INSERT INTO klienti (vards, epasts) VALUES (?, ?)",("Anna", "anna@epasts.lv"))

# lastrowid — jaunās rindas id (vajadzīgs, lai uz to atsauktos)
kursors = con.execute("INSERT INTO klienti (vards, epasts) VALUES (?, ?)",
                      ("Kārlis", "karlis@epasts.lv"))
# print(kursors.lastrowid)      # ?

# Daudz rindu uzreiz — executemany ar sarakstu
con.executemany("INSERT INTO preces (nosaukums, cena, atlikums) VALUES (?, ?, ?)", [
    ("Maize", 1.20, 30),
    ("Piens", 0.95, 20),
    ("Siers", 4.50, 5),
    ("Kafija", 7.90, 2),
    ("Tēja", 2.30, 0),
])

con.execute("INSERT INTO pasutijumi (klients_id, datums) VALUES (1, '2026-10-20')")
con.execute("INSERT INTO pasutijumi (klients_id, datums) VALUES (1, '2026-10-24')")
con.execute("INSERT INTO pasutijumi (klients_id, datums) VALUES (2, '2026-10-25')")
con.executemany("INSERT INTO pasutijuma_rindas VALUES (?, ?, ?, ?)", [
    (1, 1, 2, 1.20), (1, 2, 1, 0.95),
    (2, 3, 1, 4.50), (2, 1, 1, 1.10),      # maize toreiz maksāja mazāk
    (3, 4, 1, 7.90),
])

# radit("SELECT * FROM preces WHERE atlikums < ?", (10,))           # ?

# Pasūtījumu summas: JOIN + GROUP BY
# radit("""
#     SELECT k.vards, p.id AS pasutijums, ROUND(SUM(r.daudzums * r.cena), 2) AS summa
#     FROM pasutijumi p
#     JOIN klienti k ON k.id = p.klients_id
#     JOIN pasutijuma_rindas r ON r.pasutijums_id = p.id
#     GROUP BY p.id
#     ORDER BY summa DESC
# """)                                                                # ?

# Rezultātu var apstaigāt ar ciklu — katra rinda ir korte
for nosaukums, cena in con.execute("SELECT nosaukums, cena FROM preces"):
    pass   # print(f"{nosaukums}: {cena:.2f} €")

# Ja gribi rindu kā vārdnīcu (r["nosaukums"]), ieslēdz sqlite3.Row:
#   con.row_factory = sqlite3.Row


# ============================================================
# 5. IEROBEŽOJUMI DARBĪBĀ                              [12-033]
# ============================================================
# Ja dati pārkāpj ierobežojumu, sqlite3 met sqlite3.IntegrityError.
# Programma to noķer un pasaka lietotājam ko saprotamu.

def meginat(sql, parametri=()):
    try:
        con.execute(sql, parametri)
        print("OK      ", sql)
    except sqlite3.IntegrityError as kluda:
        print("ATTEIKTS", sql, "->", kluda)


# meginat("INSERT INTO klienti (vards, epasts) VALUES ('Ilze', 'anna@epasts.lv')")      # ?
# meginat("INSERT INTO klienti (vards) VALUES ('Bez e-pasta')")                         # ?
# meginat("INSERT INTO preces (nosaukums, cena) VALUES ('Ūdens', -1)")                  # ?
# meginat("INSERT INTO pasutijumi (klients_id) VALUES (99)")                            # ?
# meginat("UPDATE preces SET atlikums = atlikums - 10 WHERE nosaukums = 'Kafija'")      # ?
# meginat("DELETE FROM klienti WHERE id = 1")                                           # ?

# Pēdējais: klientu dzēst nevar, jo uz viņu atsaucas pasūtījumi.
# Bez PRAGMA foreign_keys = ON tas IZDOTOS, un pasūtījumi paliktu "bāreņi".


# ============================================================
# 6. INDEKSS                                           [12-033]
# ============================================================
# Indekss ir kā alfabētiskais rādītājs grāmatas beigās: lai atrastu
# vārdu, nav jālasa visa grāmata. Datubāze bez indeksa SKENĒ visu tabulu.
#
# EXPLAIN QUERY PLAN parāda, kā datubāze vaicājumu izpildīs:
#   SCAN    — pārlasa visu tabulu
#   SEARCH  — izmanto indeksu

VAICAJUMS = "SELECT * FROM pasutijumi WHERE klients_id = 1"

# radit("EXPLAIN QUERY PLAN " + VAICAJUMS)                          # ?
con.execute("CREATE INDEX idx_pasutijumi_klients ON pasutijumi(klients_id)")
# radit("EXPLAIN QUERY PLAN " + VAICAJUMS)                          # ?

# Indeksu liek laukiem, pēc kuriem bieži MEKLĒ vai SAVIENO (parasti
# ārējām atslēgām). PRIMARY KEY un UNIQUE laukiem indekss ir jau tāpat.
# Cena: ierakstīšana kļūst nedaudz lēnāka, fails — lielāks.


# ============================================================
# 7. SHĒMA NO FAILA                                    [12-033]
# ============================================================
# Īstā projektā SQL neglabā Python virknē, bet atsevišķā failā
# shema.sql. To var ielikt repozitorijā, izlasīt un palaist no jauna.
#
#   from pathlib import Path
#
#   MAPE = Path(__file__).parent          # mape, kurā ir šis .py fails
#
#   def izveidot_datubazi(cels):
#       cels.unlink(missing_ok=True)      # dzēš veco — sāk no nulles
#       con = sqlite3.connect(cels, isolation_level=None)
#       con.execute("PRAGMA foreign_keys = ON")
#       con.executescript((MAPE / "shema.sql").read_text(encoding="utf-8"))
#       con.executescript((MAPE / "dati.sql").read_text(encoding="utf-8"))
#       return con
#
# Path(__file__).parent nozīmē, ka faili tiek meklēti blakus .py failam,
# nevis tur, no kurienes programmu palaida.
#
# Ja dzēš tabulas ar DROP TABLE, secība ir svarīga: vispirms tās, kas
# atsaucas (pasutijuma_rindas), pēdējās tās, uz kurām atsaucas (klienti).
#   DROP TABLE IF EXISTS pasutijuma_rindas;
#   DROP TABLE IF EXISTS pasutijumi;
#   ...


# ============================================================
# 8. APAKŠVAICĀJUMI                                    [12-034]
# ============================================================
# Apakšvaicājums ir vaicājums iekavās citā vaicājumā. Ārējais vaicājums
# izmanto iekšējā rezultātu kā vienu vērtību, sarakstu vai tabulu.

# a) VIENA VĒRTĪBA — preces, kas dārgākas par vidējo
# radit("""
#     SELECT nosaukums, cena FROM preces
#     WHERE cena > (SELECT AVG(cena) FROM preces)
# """)                                                                # ?

# b) SARAKSTS — preces, kuras nav pasūtījis neviens
# radit("""
#     SELECT nosaukums FROM preces
#     WHERE id NOT IN (SELECT prece_id FROM pasutijuma_rindas)
# """)                                                                # ?
# To pašu var ar LEFT JOIN ... IS NULL. Izmanto to, kas tev skaidrāk.

# c) TABULA — apakšvaicājums FROM daļā. Vispirms aprēķina katra
#    pasūtījuma summu, tad no tām ņem vidējo.
# radit("""
#     SELECT ROUND(AVG(summa), 2) AS videja_summa
#     FROM (SELECT pasutijums_id, SUM(daudzums * cena) AS summa
#           FROM pasutijuma_rindas
#           GROUP BY pasutijums_id)
# """)                                                                # ?

# d) ★ KORELĒTS — iekšējais vaicājums atsaucas uz ārējā rindu un tiek
#    izpildīts katrai rindai no jauna. Katra klienta pēdējais pasūtījums:
# radit("""
#     SELECT k.vards, p.datums
#     FROM klienti k JOIN pasutijumi p ON p.klients_id = k.id
#     WHERE p.datums = (SELECT MAX(p2.datums) FROM pasutijumi p2
#                       WHERE p2.klients_id = k.id)
# """)                                                                # ?


# ============================================================
# 9. TRANSAKCIJAS                                      [12-034]
# ============================================================
# Transakcija ir vairākas izmaiņas, kurām jānotiek VISĀM VAI NEVIENAI.
#
#   BEGIN       sākas transakcija — izmaiņas vēl nav galīgas
#   COMMIT      apstiprina visas izmaiņas
#   ROLLBACK    atceļ visas izmaiņas kopš BEGIN
#
# Pasūtījuma noformēšana ir trīs izmaiņas: jauns pasūtījums, rindas un
# samazināts atlikums. Ja preces nepietiek, CHECK (atlikums >= 0)
# izmet kļūdu — bet pasūtījums jau būtu ierakstīts. Tāpēc transakcija.

def noformet_pasutijumu(klients_id, preces):
    """preces = [(prece_id, daudzums), ...]. Atgriež pasūtījuma id vai None."""
    try:
        con.execute("BEGIN")
        pasutijums_id = con.execute(
            "INSERT INTO pasutijumi (klients_id) VALUES (?)", (klients_id,)).lastrowid
        for prece_id, daudzums in preces:
            cena = con.execute("SELECT cena FROM preces WHERE id = ?",
                               (prece_id,)).fetchone()[0]
            con.execute("INSERT INTO pasutijuma_rindas VALUES (?, ?, ?, ?)",
                        (pasutijums_id, prece_id, daudzums, cena))
            con.execute("UPDATE preces SET atlikums = atlikums - ? WHERE id = ?",
                        (daudzums, prece_id))
        con.execute("COMMIT")
        return pasutijums_id
    except sqlite3.Error as kluda:
        con.execute("ROLLBACK")
        print("Pasūtījums atcelts:", kluda)
        return None


def stavoklis():
    pasutijumi = con.execute("SELECT COUNT(*) FROM pasutijumi").fetchone()[0]
    atlikumi = con.execute("SELECT nosaukums, atlikums FROM preces").fetchall()
    print(f"pasūtījumi: {pasutijumi}, atlikumi: {atlikumi}")


# stavoklis()
# print(noformet_pasutijumu(2, [(1, 3), (2, 2)]))     # ?   pietiek visa
# stavoklis()
# print(noformet_pasutijumu(2, [(1, 1), (4, 5)]))     # ?   kafijas ir tikai 2
# stavoklis()                                         # ?   vai maizes atlikums mainījās?

# Kas notiktu bez BEGIN / ROLLBACK? Pasūtījums un maizes rinda paliktu
# datubāzē, maizes atlikums samazinātos, bet kafijas — ne. Dati vairs
# nesakristu ar realitāti, un neviens to nepamanītu.
#
# Kad vajadzīga transakcija: kad divas vai vairāk izmaiņas ir LOĢISKI
# VIENA DARBĪBA. Naudas pārskaitījums, pasūtījums, biļešu pirkšana,
# grāmatas izsniegšana (izsniegums + eksemplāra statuss).
#
# ★ Bonuss: 1000 INSERT vienā transakcijā ir daudzkārt ātrāki nekā
# 1000 atsevišķi, jo disks tiek rakstīts vienreiz, nevis 1000 reižu.
