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


# Update
def update(album):
    sql = "UPDATE albums SET (name,artist_id) = (%s,%s) WHERE id = %s"
    values = [album.name, album.artist.id, album.id]
    run_sql(sql, values)


def deactivate(id):
    sql = "UPDATE albums SET active = false WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def build_album(row):
    artist = artist_repository.select(row["artist_id"])
    album = Album(row["name"], artist, row["id"])
    return album
