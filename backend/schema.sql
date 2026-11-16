-- GameHub – Grundstein: Teams und Spieler (Pflichtbereich 1)
-- SQLite

PRAGMA foreign_keys = ON;

CREATE TABLE team (
    team_code   TEXT PRIMARY KEY,       -- z.B. 'T01'
    name        TEXT NOT NULL,
    kuerzel     TEXT NOT NULL
);

CREATE TABLE spieler (
    spieler_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL UNIQUE,   -- Spielername muss eindeutig sein
    team_code   TEXT NOT NULL,
    FOREIGN KEY (team_code) REFERENCES team(team_code)
);

-- Beispiel-Testdaten (4 Teams, je 2 Spieler = 8 Spieler)
INSERT INTO team (team_code, name, kuerzel) VALUES
    ('T01', 'Red Falcons', 'RFA'),
    ('T02', 'Blue Wolves', 'BWO'),
    ('T03', 'Green Titans', 'GTI'),
    ('T04', 'Data Wolves', 'DWO');

INSERT INTO spieler (name, team_code) VALUES
    ('SpielerA1', 'T01'), ('SpielerA2', 'T01'),
    ('SpielerB1', 'T02'), ('SpielerB2', 'T02'),
    ('SpielerC1', 'T03'), ('SpielerC2', 'T03'),
    ('SpielerD1', 'T04'), ('SpielerD2', 'T04');
