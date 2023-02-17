DROP TABLE IF EXISTS parts;
DROP TABLE IF EXISTS songs;

CREATE TABLE songs(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    notes TEXT
);

CREATE TABLE parts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status INT,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE,
    instrument VARCHAR(255),
    notes TEXT
);