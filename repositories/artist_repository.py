from db.run_sql import run_sql
from models.artist import Artist
import repositories.album_repository as album_repository

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
        artist = _build_artist(row)
        artists.append(artist)
    return artists


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        artist = _build_artist(row)
    return artist


# Update
def update(artist):
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


def deactivate(id):
    sql = "UPDATE artists SET active = false WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def _build_artist(row):
    albums_completion = album_repository.select_all_completion_with_artist(row["id"])
    artist = Artist(row["name"], albums_completion, row["id"])
    return artist
