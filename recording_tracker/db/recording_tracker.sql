DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS instruments;
DROP TABLE IF EXISTS songs;

CREATE TABLE songs(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    notes TEXT
);

CREATE TABLE instruments(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    icon VARCHAR(255)
);

CREATE TABLE parts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status INT,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    instrument_id INT REFERENCES instruments(id) ON DELETE CASCADE ,
    notes TEXT
);

