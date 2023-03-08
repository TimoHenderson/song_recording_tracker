DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS instruments;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;






CREATE TABLE artists(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN DEFAULT true
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    artist_id INT REFERENCES artists(id),
    notes TEXT,
    active BOOLEAN DEFAULT true
);

CREATE TABLE songs(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    album_id INT REFERENCES albums(id),
    notes TEXT
);

CREATE TABLE instruments(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    icon VARCHAR(255),
    active BOOLEAN DEFAULT true
);

CREATE TABLE parts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status INT,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id) ON DELETE CASCADE ,
    notes TEXT 
);

