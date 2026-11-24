# ==========================================================
# 02. DATORTĪKLS, SERVERIS UN DROŠA DATUBĀZE — DARBA FAILS
# ==========================================================
# Šeit raksti savus risinājumus.
# Teorija, piemēri un atgādne: teorija.py
# Uzdevumu numuri iet cauri visam blokam.
# Pārējo stundu uzdevumi: uzdevumi.md
# ==========================================================


# ----------------------------------------------------------
# 12-033 · Datubāze no Python
# ----------------------------------------------------------

# 20. Izveido mācību datubāzi: no repozitorija saknes palaid
#    python3 bin/izveido_db.py 02-tikls-un-datubaze/skola.db. Savienojies ar to no Python
#    un izdrukā visu tabulu nosaukumus (teorija.py §1 un §3). Ja redzi no such table,
#    datubāze nav tajā mapē, kur to meklē.

import sqlite3
from pathlib import Path

MAPE = Path(__file__).parent
con = sqlite3.connect(MAPE / "skola.db", isolation_level=None)
con.execute("PRAGMA foreign_keys = ON")


# 21. Uzraksti funkciju radit(sql, parametri=()), kas izpilda vaicājumu un izdrukā kolonnu
#    nosaukumus, rindas un rindu skaitu.

def radit(sql, parametri=(), db=None):
    cur = (db or con).execute(sql, parametri)
    rindas = cur.fetchall()
    kolonnas = [k[0] for k in cur.description]

    platumi = [len(k) for k in kolonnas]
    for rinda in rindas:
        for i, elem in enumerate(rinda):
            platumi[i] = max(platumi[i], len(str(elem)))

    for i, k in enumerate(kolonnas):
        print(f"{k:<{platumi[i]}}", end="  ")
    print()
    for rinda in rindas:
        for i, elem in enumerate(rinda):
            print(f"{str(elem):<{platumi[i]}}", end="  ")
        print()
    print(f"Rindu skaits: {len(rindas)}")

# 22. SQL atkārtojums — viena tabula. Uzraksti vaicājumus:
#    - a) skolēni, kas dzimuši 2008. gadā, sakārtoti pēc uzvārda;

# radit("SELECT vards, uzvards, epasts FROM skoleni WHERE dzimsanas_gads = 2008 ORDER BY uzvards")

#    - b) skolēni, kuriem nav e-pasta;

# radit("select vards, uzvards from skoleni where epasts is null")

#    - c) cik reižu ir likta katra atzīme no 1 līdz 10;

# radit("SELECT atzime, COUNT(*) AS skaits FROM atzimes GROUP BY atzime")

#    - d) cik skolēnu ir katrā klasē (pēc klase_id);

# radit("SELECT klase_id, COUNT(*) as skaits FROM skoleni GROUP BY klase_id ORDER BY skaits DESC LIMIT 3")

#    - e) desmit augstākās decembrī saņemtās atzīmes ar datumu.

# radit("SELECT * FROM atzimes WHERE datums LIKE '%-12-%' ORDER BY atzime DESC LIMIT 10")


# 23. SQL atkārtojums — vairākas tabulas. Uzraksti vaicājumus:
#    - a) katras klases nosaukums un audzinātāja vārds un uzvārds;

# radit("SELECT nosaukums, vards, uzvards FROM klases JOIN skolotaji ON klases.audzinatajs_id = skolotaji.id")

#    - b) katra priekšmeta vidējā atzīme, noapaļota līdz divām zīmēm, augstākā vispirms;

# radit("""
#         SELECT prieksmeti.nosaukums, ROUND(AVG(atzimes.atzime), 2) as videja 
#         FROM prieksmeti 
#         JOIN atzimes ON prieksmeti.id = atzimes.prieksmets_id
#         GROUP BY prieksmeti.id
#         ORDER BY videja DESC
#         """)

#    - c) klases, kuru vidējā atzīme ir augstāka par 6,7;

# radit("""
#         SELECT klases.nosaukums, ROUND(AVG(atzimes.atzime), 2) as videja_atzime
#         FROM klases
#         JOIN skoleni ON klases.id = skoleni.klase_id
#         JOIN atzimes ON skoleni.id = atzimes.skolens_id
#         GROUP BY klases.nosaukums
#         HAVING videja_atzime > 6.7
#         """)

#    - d) skolēni, kuriem nav nevienas atzīmes;

# # SELECT iekš SELECT jeb apakšvaicājums
# radit("""
#         SELECT vards, uzvards FROM skoleni WHERE id NOT IN (SELECT DISTINCT skolens_id FROM atzimes);
#         """)

# # LEFT JOIN 
# radit("""
#     SELECT vards, uzvards FROM skoleni LEFT JOIN atzimes ON skoleni.id = atzimes.skolens_id WHERE atzimes.skolens_id IS NULL;
# """)

#    - e) visi pulciņi ar dalībnieku skaitu, ieskaitot pulciņus bez dalībniekiem;

# radit("""
#     SELECT nosaukums, COUNT(dalibnieki.id) AS dalibnieku_skaits 
#     FROM pulcini 
#     LEFT JOIN dalibnieki ON pulcini.id = dalibnieki.pulcins_id
#     GROUP BY pulcini.id
#     ORDER BY dalibnieku_skaits DESC;
# """)

#    - f) ★ pieci skolēni ar augstāko vidējo atzīmi starp tiem, kam ir vismaz 10 atzīmes.

# radit("""
#     SELECT vards, uzvards, ROUND(AVG(atzime), 2) as vid_atzime, COUNT(atzimes.id) as atzimju_skaits 
#     FROM skoleni
#     JOIN atzimes ON skoleni.id = atzimes.skolens_id
#     GROUP BY skoleni.id
#     HAVING atzimju_skaits >= 10
#     ORDER BY vid_atzime DESC
#     LIMIT 5
# """)

# 24. Uzraksti funkciju klases_skoleni(klase), kas atgriež dotās klases (piemēram, "12.a")
#    skolēnu vārdus un uzvārdus. Klases nosaukumu padod ar ?, nevis ar f-string.

# def klases_skoleni(klase):
#     cur = con.execute("""
#         SELECT vards, uzvards, epasts, dzimsanas_gads 
#         FROM klases 
#         JOIN skoleni ON klases.id = skoleni.klase_id 
#         WHERE klases.nosaukums = ?
#     """, (klase, ))

#     rindas = cur.fetchall()
#     return rindas

# for skolens in klases_skoleni("10.b"):
#     print(skolens)


# 25. Realizē savu 12-031 bibliotēkas ER modeli kā failu biblioteka.sql ar tabulām
#    gramatas, autori, eksemplari, lasitaji, izsniegumi. Prasības:
#    - primārās un ārējās atslēgas;
#    - NOT NULL visur, kur tukša vērtība nav jēgpilna;
#    - UNIQUE svītrkodam un e-pastam;
#    - CHECK izdošanas gadam un tam, ka atgriešanas datums nav agrāks par izsniegšanas;
#    - DEFAULT izsniegšanas datumam.

# Risinājums: biblioteka.sql (blakus šim failam).


# 26. Uzraksti funkciju izveidot_biblioteku(), kas izdzēš veco biblioteka.db, ieslēdz
#    ārējo atslēgu pārbaudi un izpilda biblioteka.sql (teorija.py §7). Ievieto testa
#    datus ar executemany: vismaz pieci ieraksti katrā tabulā.

def izveidot_biblioteku():
    cels = MAPE / "biblioteka.db"
    cels.unlink(missing_ok=True)
    bib = sqlite3.connect(cels, isolation_level=None)
    bib.execute("PRAGMA foreign_keys = ON")
    bib.executescript((MAPE / "biblioteka.sql").read_text(encoding="utf-8"))

    bib.executemany("INSERT INTO autori (id, vards, uzvards) VALUES (?, ?, ?)", [
        (1, "Rūdolfs", "Blaumanis"),
        (2, "Regīna", "Ezera"),
        (3, "Nora", "Ikstena"),
        (4, "Anšlavs", "Eglītis"),
        (5, "Jānis", "Poruks"),
    ])
    bib.executemany("INSERT INTO gramatas (id, nosaukums, autors_id, izdosanas_gads) VALUES (?, ?, ?, ?)", [
        (1, "Skroderdienas Silmačos", 1, 1902),
        (2, "Nāves ēnā", 1, 1899),
        (3, "Mātes piens", 3, 2015),
        (4, "Līgavu mednieki", 4, 1940),
        (5, "Pērļu zvejnieks", 5, 1895),
        (6, "Aka", 2, 1972),
    ])
    bib.executemany("INSERT INTO eksemplari (id, gramata_id, svitrkods) VALUES (?, ?, ?)", [
        (1, 1, "LV-0001"),
        (2, 1, "LV-0002"),
        (3, 2, "LV-0003"),
        (4, 3, "LV-0004"),
        (5, 4, "LV-0005"),
        (6, 5, "LV-0006"),
        (7, 6, "LV-0007"),
    ])
    bib.executemany("INSERT INTO lasitaji (id, vards, uzvards, epasts, telefons) VALUES (?, ?, ?, ?, ?)", [
        (1, "Anna", "Bērziņa", "anna@skola.lv", "20000001"),
        (2, "Kārlis", "Ozols", "karlis@skola.lv", None),
        (3, "Elza", "Kalniņa", "elza@skola.lv", "20000003"),
        (4, "Mārtiņš", "Liepa", "martins@skola.lv", None),
        (5, "Laura", "Zariņa", "laura@skola.lv", "20000005"),
    ])
    # atgriezts = None -> grāmata vēl nav atnesta atpakaļ
    bib.executemany("INSERT INTO izsniegumi (eksemplars_id, lasitajs_id, izsniegts, atgriezts) VALUES (?, ?, ?, ?)", [
        (1, 1, "2026-09-01", "2026-09-20"),
        (3, 1, "2026-10-15", None),
        (4, 2, "2026-10-01", "2026-10-10"),
        (5, 3, "2026-10-20", None),
        (6, 4, "2026-11-01", None),
    ])
    # Bez izsniegts -> stājas spēkā DEFAULT CURRENT_DATE
    bib.execute("INSERT INTO izsniegumi (eksemplars_id, lasitajs_id) VALUES (7, 5)")
    return bib

bib = izveidot_biblioteku()
# radit("SELECT * FROM izsniegumi", db=bib)


# 27. Pārbaudi ierobežojumus. Katrai darbībai jābeidzas ar sqlite3.IntegrityError. Izdrukā
#    kļūdas tekstu un komentārā pieraksti, kurš ierobežojums to apturēja:
#    - a) lasītājs ar jau esošu e-pastu;
#    - b) eksemplārs grāmatai, kuras nav (gramata_id = 999);
#    - c) grāmata bez autora;
#    - d) grāmata ar izdošanas gadu 3025;
#    - e) izsniegums, kas atgriezts agrāk, nekā izsniegts;
#    - f) lasītāja dzēšana, ja viņam ir izsniegumi.

# parbaudes = [
#     # a) UNIQUE uz lasitaji.epasts
#     ("a", "INSERT INTO lasitaji (vards, uzvards, epasts) VALUES ('Cita', 'Anna', 'anna@skola.lv')"),
#     # b) FOREIGN KEY eksemplari.gramata_id -> gramatas(id)
#     ("b", "INSERT INTO eksemplari (gramata_id, svitrkods) VALUES (999, 'LV-9999')"),
#     # c) NOT NULL uz gramatas.autors_id
#     ("c", "INSERT INTO gramatas (nosaukums, izdosanas_gads) VALUES ('Bez autora', 2020)"),
#     # d) CHECK (izdosanas_gads BETWEEN 1450 AND 2100)
#     ("d", "INSERT INTO gramatas (nosaukums, autors_id, izdosanas_gads) VALUES ('Nākotne', 1, 3025)"),
#     # e) CHECK (atgriezts IS NULL OR atgriezts >= izsniegts)
#     ("e", "INSERT INTO izsniegumi (eksemplars_id, lasitajs_id, izsniegts, atgriezts) VALUES (2, 2, '2026-11-05', '2026-11-01')"),
#     # f) FOREIGN KEY izsniegumi.lasitajs_id -> lasitaji(id): uz Annu vēl atsaucas izsniegumi
#     ("f", "DELETE FROM lasitaji WHERE id = 1"),
# ]

# for burts, sql in parbaudes:
#     try:
#         bib.execute(sql)
#         print(f"{burts}) IZDEVĀS — ierobežojums nestrādā!")
#     except sqlite3.IntegrityError as e:
#         print(f"{burts}) IntegrityError: {e}")


# 28. Pievieno indeksu laukam, pēc kura meklēsi visbiežāk. Ar EXPLAIN QUERY PLAN parādi
#    vaicājuma plānu pirms un pēc indeksa izveides un komentārā pamato izvēli.

# Izvēle: izsniegumi.lasitajs_id.
# Visbiežāk bibliotekārs skatās "kas ir paņemts uz šī lasītāja vārda" — tas ir
# WHERE lasitajs_id = ?. Ārējās atslēgas laukam SQLite indeksu pati NEizveido
# (atšķirībā no PRIMARY KEY un UNIQUE, piem., svitrkods un epasts, kam tas jau ir),
# tāpēc bez indeksa jāpārlasa VISA izsniegumu tabula (SCAN). Izsniegumu tabula aug
# visātrāk — katra izsniegšana ir jauna rinda. Indekss palīdz arī 27.f: dzēšot
# lasītāju, SQLite meklē izsniegumus ar viņa id.

# VAICAJUMS = "SELECT * FROM izsniegumi WHERE lasitajs_id = 1"

# print("Pirms indeksa:")
# radit("EXPLAIN QUERY PLAN " + VAICAJUMS, db=bib)    # SCAN izsniegumi

# bib.execute("CREATE INDEX idx_izsniegumi_lasitajs ON izsniegumi(lasitajs_id)")

# print("Pēc indeksa:")
# radit("EXPLAIN QUERY PLAN " + VAICAJUMS, db=bib)    # SEARCH izsniegumi USING INDEX idx_izsniegumi_lasitajs (lasitajs_id=?)


# 29. ★ Uzraksti vaicājumu: kuri eksemplāri pašlaik ir izsniegti, kam un cik dienas.


# radit("""
#     SELECT epasts, autori.vards, autori.uzvards, nosaukums, izsniegts, atgriezts FROM izsniegumi
#     JOIN lasitaji ON izsniegumi.lasitajs_id=lasitaji.id
#     JOIN eksemplari ON izsniegumi.eksemplars_id=eksemplari.id
#     JOIN gramatas ON eksemplari.gramata_id=gramatas.id
#     JOIN autori ON gramatas.autors_id=autori.id;
# """, db=bib)


# ----------------------------------------------------------
# 12-034 · Vaicājumi un transakcijas
# ----------------------------------------------------------

# 30. Apakšvaicājumi uz skola.db:
#    - a) skolēni, kuru vidējā atzīme ir augstāka par visas skolas vidējo;

# radit("""
#     SELECT AVG(atzime) AS vid_atzime FROM atzimes;
# """)

# radit("""
#     SELECT skoleni.vards, skoleni.uzvards, AVG(atzime) as avg
#     FROM skoleni 
#     JOIN atzimes ON skoleni.id=atzimes.skolens_id
#     GROUP BY skoleni.id
#     HAVING avg > (
#         SELECT ROUND(AVG(atzime), 1) AS vid_atzime FROM atzimes
#     );
# """)

#    - b) skolēni, kuri nav nevienā pulciņā;

# radit("""
#     SELECT DISTINCT pulcins_id FROM dalibnieki;
# """)

# radit("SELECT * ")

# radit("""
#     SELECT DISTINCT skolens_id FROM dalibnieki;
# """)

# radit("""
#     SELECT vards, uzvards FROM skoleni
#     WHERE id NOT IN (
#         SELECT DISTINCT skolens_id FROM dalibnieki
#     );
# """)

#    - c) priekšmets, kurā ir likts visvairāk atzīmju;

# radit("""
#     SELECT prieksmeti.nosaukums, COUNT(*) AS skaits FROM prieksmeti
#     JOIN atzimes ON prieksmeti.id=atzimes.prieksmets_id
#     GROUP BY prieksmeti.id;
# """)

# radit("""
#     SELECT nosaukums, MAX(skaits) as skaits FROM (
#        SELECT prieksmeti.nosaukums, COUNT(*) AS skaits FROM prieksmeti
#         JOIN atzimes ON prieksmeti.id=atzimes.prieksmets_id
#         GROUP BY prieksmeti.id 
#     )
# """)

#    - d) vidējais dalībnieku skaits pulciņos, kuros ir vismaz viens dalībnieks;

# radit("""
#     SELECT nosaukums, COUNT(*) AS skaits FROM pulcini 
#     JOIN dalibnieki ON pulcini.id=dalibnieki.pulcins_id
#     GROUP BY pulcini.id;
# """)

# radit("""
#     SELECT ROUND(AVG(skaits), 2) AS videjais FROM (
#         SELECT nosaukums, COUNT(*) AS skaits FROM pulcini 
#         JOIN dalibnieki ON pulcini.id=dalibnieki.pulcins_id
#         GROUP BY pulcini.id    
#     )
# """)

#    - e) ★ katram skolēnam viņa pēdējās atzīmes datums un pati atzīme.

# radit("""
#     SELECT vards, uzvards, atzime, MAX(datums) 
#     FROM skoleni JOIN atzimes ON skoleni.id=atzimes.skolens_id 
#     GROUP BY skoleni.id;
# """)

# OPTIMĀlS
# radit("""
#     SELECT s.vards, s.uzvards, a.datums, a.atzime
#     FROM skoleni s
#     JOIN atzimes a ON a.skolens_id = s.id
#     WHERE a.datums = (
#         SELECT MAX(a2.datums)
#         FROM atzimes a2
#         WHERE a2.skolens_id = s.id 
#     )
#     ORDER BY s.uzvards;
# """)

# radit("""
#     SELECT s.vards, s.uzvards, a.datums, a.atzime
#     FROM skoleni s
#     JOIN atzimes a ON a.skolens_id = s.id
#     WHERE a.id = (
#         SELECT a2.id
#         FROM atzimes a2
#         WHERE a2.skolens_id = s.id
#         ORDER BY a2.datums DESC, a2.id DESC
#         LIMIT 1
#     );
# """)


#    - f) katram pulciņam brīvo vietu skaits (vietu_skaits mīnus dalībnieku skaits),
#         ieskaitot pulciņus bez dalībniekiem — skaitu iegūsti ar apakšvaicājumu SELECT daļā;

# radit("""
#     SELECT 
#         nosaukums,
#         vietu_skaits, 
#         COUNT(skolens_id) AS dalibnieku_skaits,
#         vietu_skaits - COUNT(skolens_id) AS brivo_vietu_skaits
#     FROM pulcini p 
#     LEFT JOIN dalibnieki d ON p.id=d.pulcins_id
#     GROUP BY p.id;
# """)

#    - g) skolotāji, kuri nav nevienas klases audzinātāji un nevada nevienu pulciņu;

radit("""
    SELECT DISTINCT skolotajs_id FROM pulcini;
""")

radit("""
    SELECT DISTINCT audzinatajs_id FROM klases;
""")

radit("""
    SELECT * FROM skolotaji 
    WHERE skolotaji.id NOT IN (
        SELECT DISTINCT audzinatajs_id FROM klases
        )
    AND 
    skolotaji.id NOT IN (
        SELECT DISTINCT skolotajs_id FROM pulcini
        );
""")


#    - h) klases, kurās ir vairāk skolēnu nekā vidēji vienā klasē;



#    - i) skolēni, kuri ir saņēmuši vismaz vienu 10, bet nevienu atzīmi zem 4;



#    - j) ★ katrā priekšmetā skolēns (vai skolēni) ar augstāko vidējo atzīmi šajā priekšmetā.






# 31. Bankas konti. Atmiņā (":memory:") izveido tabulu
#    konti(id, ipasnieks, atlikums) ar CHECK (atlikums >= 0) un divus kontus ar 100 €
#    katrā. Uzraksti funkciju kopsumma(), kas atgriež visu kontu atlikumu summu.




# 32. Uzraksti funkciju parskaitit_bez_transakcijas(no_id, uz_id, summa): divi UPDATE
#    pēc kārtas, bet starp tiem if summa > 50: raise RuntimeError("Strāva pazuda!").
#    Izsauc to ar 80 €, noķer kļūdu un izdrukā kopsummu. Kur palika nauda?




# 33. Uzraksti funkciju parskaitit(no_id, uz_id, summa) ar BEGIN / COMMIT / ROLLBACK
#    un tādu pašu «strāvas zudumu». Pārbaudi: kopsummai jāpaliek 200 €.




# 34. Mēģini pārskaitīt vairāk, nekā ir kontā. Kurš ierobežojums to aptur? Samaini abus
#    UPDATE vietām (vispirms pieskaita, tad atņem) un pārbaudi vēlreiz: kas bez ROLLBACK
#    notiktu ar otra konta atlikumu?




# 35. Kinoteātris. Atmiņā izveido tabulu biletes un uzraksti funkciju
#    nopirkt(seanss_id, vietas, epasts), kur vietas ir saraksts ar (rinda, vieta).
#    Vai nu tiek nopirktas visas biļetes, vai neviena. Funkcija atgriež True vai False.
#    CREATE TABLE biletes (
#        id        INTEGER PRIMARY KEY,
#        seanss_id INTEGER NOT NULL,
#        rinda     INTEGER NOT NULL CHECK (rinda BETWEEN 1 AND 10),
#        vieta     INTEGER NOT NULL CHECK (vieta BETWEEN 1 AND 12),
#        epasts    TEXT NOT NULL,
#        UNIQUE (seanss_id, rinda, vieta)
#    );




# 36. Pārbaudi: Anna pērk seansam 1 vietas (5, 7) un (5, 8). Pēc tam Kārlis pērk (5, 8) un
#    (5, 9). Cik biļešu ir Kārlim? Vai vieta (5, 9) palika brīva? Pēc tam pamēģini nopirkt
#    vietu (11, 1).




# 37. ★ Pieraksti savā sistēmā (18. uzdevums) vienu vietu, kur būs vajadzīga transakcija, un
#    kāpēc.





# ----------------------------------------------------------
# 12-035 · Sprints: sava datubāze
# ----------------------------------------------------------

# 38. Pārvērs savas sistēmas ER modeli (18. uzdevums, izlabots pēc 12-032) failā shema.sql:
#    visas tabulas, primārās un ārējās atslēgas, NOT NULL, UNIQUE, vismaz viens CHECK
#    un vismaz viens indekss ar komentāru, kāpēc tieši tur.




# 39. Uzraksti dati.sql ar testa datiem (vismaz pieci ieraksti katrā tabulā) un Python
#    funkciju, kas datubāzi izveido no nulles no abiem failiem.




# 40. Uzraksti vaicajumi.sql ar desmit vaicājumiem, kas atbild uz reāliem jautājumiem par
#    taviem datiem. Pirms katra vaicājuma komentārā uzraksti jautājumu. Starp tiem jābūt
#    JOIN, LEFT JOIN, GROUP BY ar HAVING un apakšvaicājumam.




# 41. Uzraksti vienu Python funkciju ar transakciju — darbību, kurā divas vai vairākas
#    izmaiņas jāveic kopā. Notestē gan veiksmīgu, gan neveiksmīgu gadījumu.




# 42. Katram ierobežojumam uzraksti vienu mēģinājumu ievadīt nederīgus datus, kas beidzas ar
#    IntegrityError.




# 43. ★ Uzraksti vaicājumu, kas atrod datus, kuri pārkāpj kādu loģisku noteikumu, ko datubāze
#    pati nepārbauda.
