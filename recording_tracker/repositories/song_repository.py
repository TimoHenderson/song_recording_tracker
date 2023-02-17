from db.run_sql import run_sql
from models.song import Song
import repositories.part_repository as part_repository

# Create
def save(song):
    sql = """INSERT INTO songs (title,artist,album,notes) 
            VALUES (%s,%s,%s,%s) RETURNING id"""
    values = [song.title, song.artist, song.album, song.notes]
    results = run_sql(sql, values)
    song.id = results[0]["id"]


# TODO update to add part getting
# Read
def select_all():
    songs = []
    sql = "SELECT * FROM songs"
    results = run_sql(sql)
    for row in results:
        song = build_song(row)
        songs.append(song)
    return songs


def select(id):
    song = None
    sql = "SELECT * FROM songs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        song = build_song(row)
    return song


# Update
def update(song):
    sql = "UPDATE songs SET (title, artist, album, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [song.title, song.artist, song.album, song.notes, song.id]
    run_sql(sql, values)


# Delete
def delete_all():
    sql = "DELETE FROM songs"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM songs WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def build_song(row):
    parts = part_repository.select_all_with_song(row["id"])
    return Song(
        row["title"], row["artist"], row["album"], row["notes"], row["id"], parts
    )
