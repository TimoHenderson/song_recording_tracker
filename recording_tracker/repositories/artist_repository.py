from db.run_sql import run_sql
from models.artist import Artist

# Create
def save(artist):
    sql = """INSERT INTO artists (name) 
            VALUES (%s) RETURNING id"""
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]["id"]


# Read
def select_all():
    artists = []
    sql = "SELECT * FROM artists WHERE active = true"
    results = run_sql(sql)
    for row in results:
        artist = build_artist(row)
        artists.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        artist = build_artist(row)
    return artist


# Update
def update(artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


def build_artist(row):
    artist = Artist(row["name"], row["id"])
    return artist
