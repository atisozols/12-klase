-- ==========================================================
-- Bibliotēkas datubāze (12-031 ER modelis)
-- ==========================================================
-- autori 1 ── N gramatas 1 ── N eksemplari 1 ── N izsniegumi N ── 1 lasitaji

-- Dzēš tabulas pretējā secībā: vispirms tās, kas atsaucas.
DROP TABLE IF EXISTS izsniegumi;
DROP TABLE IF EXISTS eksemplari;
DROP TABLE IF EXISTS lasitaji;
DROP TABLE IF EXISTS gramatas;
DROP TABLE IF EXISTS autori;

CREATE TABLE autori (
    id      INTEGER PRIMARY KEY,
    vards   TEXT NOT NULL,
    uzvards TEXT NOT NULL
);

CREATE TABLE gramatas (
    id             INTEGER PRIMARY KEY,
    nosaukums      TEXT    NOT NULL,
    autors_id      INTEGER NOT NULL REFERENCES autori(id),
    izdosanas_gads INTEGER NOT NULL
                   CHECK (izdosanas_gads BETWEEN 1450 AND 2100)
);

-- Viena grāmata var būt vairākos fiziskos eksemplāros.
CREATE TABLE eksemplari (
    id         INTEGER PRIMARY KEY,
    gramata_id INTEGER NOT NULL REFERENCES gramatas(id),
    svitrkods  TEXT    NOT NULL UNIQUE
);

CREATE TABLE lasitaji (
    id      INTEGER PRIMARY KEY,
    vards   TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    epasts  TEXT NOT NULL UNIQUE,
    telefons TEXT                     -- drīkst nebūt
);

-- atgriezts IS NULL nozīmē, ka grāmata vēl ir pie lasītāja.
CREATE TABLE izsniegumi (
    id            INTEGER PRIMARY KEY,
    eksemplars_id INTEGER NOT NULL REFERENCES eksemplari(id),
    lasitajs_id   INTEGER NOT NULL REFERENCES lasitaji(id),
    izsniegts     TEXT    NOT NULL DEFAULT CURRENT_DATE,
    atgriezts     TEXT,
    CHECK (atgriezts IS NULL OR atgriezts >= izsniegts)
);
