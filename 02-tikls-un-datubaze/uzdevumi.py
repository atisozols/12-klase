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

def radit(sql, parametri=()):
    cur = con.execute(sql, parametri)
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


radit("SELECT * FROM skoleni")


# 22. SQL atkārtojums — viena tabula. Uzraksti vaicājumus:
#    - a) skolēni, kas dzimuši 2008. gadā, sakārtoti pēc uzvārda;
#    - b) skolēni, kuriem nav e-pasta;
#    - c) cik reižu ir likta katra atzīme no 1 līdz 10;
#    - d) cik skolēnu ir katrā klasē (pēc klase_id);
#    - e) desmit augstākās decembrī saņemtās atzīmes ar datumu.




# 23. SQL atkārtojums — vairākas tabulas. Uzraksti vaicājumus:
#    - a) katras klases nosaukums un audzinātāja vārds un uzvārds;
#    - b) katra priekšmeta vidējā atzīme, noapaļota līdz divām zīmēm, augstākā vispirms;
#    - c) klases, kuru vidējā atzīme ir augstāka par 6,7;
#    - d) skolēni, kuriem nav nevienas atzīmes;
#    - e) visi pulciņi ar dalībnieku skaitu, ieskaitot pulciņus bez dalībniekiem;
#    - f) ★ pieci skolēni ar augstāko vidējo atzīmi starp tiem, kam ir vismaz 10 atzīmes.




# 24. Uzraksti funkciju klases_skoleni(klase), kas atgriež dotās klases (piemēram, "12.a")
#    skolēnu vārdus un uzvārdus. Klases nosaukumu padod ar ?, nevis ar f-string.




# 25. Realizē savu 12-031 bibliotēkas ER modeli kā failu biblioteka.sql ar tabulām
#    gramatas, eksemplari, lasitaji, izsniegumi. Prasības:
#    - primārās un ārējās atslēgas;
#    - NOT NULL visur, kur tukša vērtība nav jēgpilna;
#    - UNIQUE svītrkodam un e-pastam;
#    - CHECK izdošanas gadam un tam, ka atgriešanas datums nav agrāks par izsniegšanas;
#    - DEFAULT izsniegšanas datumam.




# 26. Uzraksti funkciju izveidot_biblioteku(), kas izdzēš veco biblioteka.db, ieslēdz
#    ārējo atslēgu pārbaudi un izpilda biblioteka.sql (teorija.py §7). Ievieto testa
#    datus ar executemany: vismaz pieci ieraksti katrā tabulā.




# 27. Pārbaudi ierobežojumus. Katrai darbībai jābeidzas ar sqlite3.IntegrityError. Izdrukā
#    kļūdas tekstu un komentārā pieraksti, kurš ierobežojums to apturēja:
#    - a) lasītājs ar jau esošu e-pastu;
#    - b) eksemplārs grāmatai, kuras nav (gramata_id = 999);
#    - c) grāmata bez autora;
#    - d) grāmata ar izdošanas gadu 3025;
#    - e) izsniegums, kas atgriezts agrāk, nekā izsniegts;
#    - f) lasītāja dzēšana, ja viņam ir izsniegumi.




# 28. Pievieno indeksu laukam, pēc kura meklēsi visbiežāk. Ar EXPLAIN QUERY PLAN parādi
#    vaicājuma plānu pirms un pēc indeksa izveides un komentārā pamato izvēli.




# 29. ★ Uzraksti vaicājumu: kuri eksemplāri pašlaik ir izsniegti, kam un cik dienas.





# ----------------------------------------------------------
# 12-034 · Vaicājumi un transakcijas
# ----------------------------------------------------------

# 30. Apakšvaicājumi uz skola.db:
#    - a) skolēni, kuru vidējā atzīme ir augstāka par visas skolas vidējo;
#    - b) skolēni, kuri nav nevienā pulciņā;
#    - c) priekšmets, kurā ir likts visvairāk atzīmju;
#    - d) vidējais dalībnieku skaits pulciņos, kuros ir vismaz viens dalībnieks;
#    - e) ★ katram skolēnam viņa pēdējās atzīmes datums un pati atzīme.




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
