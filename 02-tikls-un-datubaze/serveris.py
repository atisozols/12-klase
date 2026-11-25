# ==========================================================
# 02. bloks — BIBLIOTĒKAS SERVERIS (praktiskais darbs, 4 stundas)
# ==========================================================
# Uzdevumi: praktiskais-serveris.md
# Datubāze: tava biblioteka.db no 12-033 (uzdevumi.py, 26. uzdevums)
#
# Palaišana:   python3 serveris.py
# Pārbaude:    pārlūkā atver http://127.0.0.1:5001/
# Apturēšana:  Ctrl+C terminālī

import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

MAPE = Path(__file__).parent
DB = MAPE / "biblioteka.db"

app = Flask(__name__)
app.json.ensure_ascii = False   # lai JSON rāda "Nāves ēnā", nevis "Nāves ēnā"


# ----------------------------------------------------------
# Palīgfunkcijas — tās jau ir gatavas
# ----------------------------------------------------------

def db():
    """Jauns savienojums katram pieprasījumam."""
    con = sqlite3.connect(DB, isolation_level=None)
    con.row_factory = sqlite3.Row             # rindas var pārvērst par dict
    con.execute("PRAGMA foreign_keys = ON")
    return con


def vaicajums(sql, parametri=()):
    """Izpilda SELECT un atgriež sarakstu ar vārdnīcām — tieši tas, ko var ielikt jsonify."""
    con = db()
    try:
        return [dict(rinda) for rinda in con.execute(sql, parametri)]
    finally:
        con.close()


def kluda(teksts, kods):
    """Vienmēr viena un tā pati kļūdas atbildes forma: {"kluda": "..."}."""
    return jsonify({"kluda": teksts}), kods

def vesels_skaitlis(nosaukums, noklusejums, min_v=None, max_v=None):
    """Nolasa request.args[nosaukums]; ja nav — noklusējums.
    Ja nav vesels skaitlis vai ir ārpus robežām — raise ValueError("…saprotams teksts…")."""
    teksts = request.args.get(nosaukums, "")
    if teksts == "":
        return noklusejums
    
    try:
        vertiba = int(teksts)
    except ValueError:
        raise ValueError(f"{nosaukums} jābūt veselam skaitlim")
    if min_v is not None and vertiba < min_v:
        raise ValueError(f"{nosaukums} nedrīkst būt mazāks par {min_v}")
    if max_v is not None and vertiba > max_v:
        raise ValueError(f"{nosaukums} nedrīkst būt lielāks par {max_v}")

    return vertiba



# ----------------------------------------------------------
# Maršruti
# ----------------------------------------------------------

@app.get("/")
def sakums():
    return jsonify({"zina": "Bibliotēkas serveris strādā"})

# 1. stunda — 2.–6. uzdevums
# GET /api/gramatas
@app.get("/api/gramatas")
def gramatas():
    meklet = request.args.get("meklet") or None
    try:
        no = vesels_skaitlis("no", None)
        lidz = vesels_skaitlis("lidz", None)
        limit = vesels_skaitlis("limit", 20, 1, 100)
        offset = vesels_skaitlis("offset", 0, 0)
    except ValueError as error:
        return kluda(str(error), 400)

    if no > lidz:
        return kluda("no nedrīkst būt lielāks par lidz", 400)


    result = vaicajums("""
            SELECT gramatas.id, nosaukums, izdosanas_gads, CONCAT(vards, ' ', uzvards) as autors, COUNT(eksemplari.id) as eksemplari 
            FROM gramatas 
            JOIN eksemplari ON eksemplari.gramata_id=gramatas.id
            JOIN autori ON autori.id=gramatas.autors_id
            WHERE 
                (:no IS NULL OR gramatas.izdosanas_gads >= :no) 
                AND 
                (:lidz IS NULL OR gramatas.izdosanas_gads <= :lidz)
                AND
                (:meklet IS NULL OR gramatas.nosaukums LIKE '%' || :meklet || '%') 
            GROUP BY gramatas.id
            LIMIT :limit OFFSET :offset;
        """, {"no": no, "lidz": lidz, "meklet": meklet, "limit": limit, "offset": offset})
        
    
    return jsonify({"skaits": len(result), "dati": result})

# GET /api/gramatas/<int:id>
@app.get("/api/gramatas/<int:id>")
def gramata_ar_eksemplariem(id):
    result = vaicajums("""
        SELECT * FROM gramatas
        JOIN eksemplari ON gramatas.id=eksemplari.gramata_id 
        WHERE gramatas.id = ?;
    """, (id, ))

    if len(result) == 0:
        return jsonify({"kluda": "Grāmata nav atrasta"}), 400

    return jsonify({"skaits": len(result), "dati": result})

# GET /api/lasitaji

@app.get("/api/lasitaji")
def lasitaji():
    result = vaicajums("""
        SELECT id, vards, uzvards FROM lasitaji;
    """)

    return jsonify({"skaits": len(result), "dati": result})

# ★ GET /api/autori/<int:id>/gramatas


# 2. stunda — 7.–12. uzdevums
# GET /api/izsniegti

@app.get("/api/izsniegti")
def izsniegti():
    result = vaicajums("""
        SELECT svitrkods, nosaukums, CONCAT(vards, ' ', uzvards) as lasitajs, CAST(JULIANDAY('now') - JULIANDAY(i.izsniegts) AS INTEGER) as dienas, i.izsniegts FROM izsniegumi i
        JOIN eksemplari e ON i.eksemplars_id=e.id
        JOIN lasitaji l ON i.lasitajs_id=l.id
        JOIN gramatas g ON g.id=e.gramata_id
        WHERE atgriezts IS NULL
        ORDER BY dienas DESC
    """)

    return jsonify({"skaits": len(result), "dati": result})

# GET /api/statistika


# 3. stunda — 13.–17. uzdevums
# POST /api/lasitaji
# POST /api/izsniegumi
# POST /api/izsniegumi/<int:id>/atgriezt
# kļūdu apstrādātāji 404, 405, 500
# ★ POST /api/izsniegumi/vairaki


# 4. stunda — 18.–22. uzdevums
# žurnalēšana: @app.before_request un @app.after_request


if __name__ == "__main__":
    # 4. stundā: debug=False un host="0.0.0.0" (19. uzdevums)
    app.run(port=5001, debug=True)
