from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository


# Create
def save(album):
    sql = """INSERT INTO albums (name,artist_id) 
            VALUES (%s,%s) RETURNING id"""
    values = [album.name, album.artist.id]
    results = run_sql(sql, values)
    album.id = results[0]["id"]

    # Read


def select_all():
    albums = []
    sql = "SELECT * FROM albums WHERE active = true"
    results = run_sql(sql)
    for row in results:
        album = build_album(row)
        albums.append(album)
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        album = build_album(row)
    return album


def build_album(row):
    artist = artist_repository.select(row["artist_id"])
    album = Album(row["name"], artist, row["id"])
    return album
