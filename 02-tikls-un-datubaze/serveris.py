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


# ----------------------------------------------------------
# Maršruti
# ----------------------------------------------------------

@app.get("/")
def sakums():
    return jsonify({"zina": "Bibliotēkas serveris strādā"})


# 1. stunda — 2.–6. uzdevums
# GET /api/gramatas
# GET /api/gramatas/<int:id>
# GET /api/lasitaji
# ★ GET /api/autori/<int:id>/gramatas


# 2. stunda — 7.–12. uzdevums
# GET /api/gramatas?meklet=&no=&lidz=&limit=&offset=
# GET /api/izsniegti
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
