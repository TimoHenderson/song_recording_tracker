from db.run_sql import run_sql
from models.song import Song
import repositories.part_repository as part_repository
import repositories.album_repository as album_repository

# Create
def save(song):
    sql = """INSERT INTO songs (title,album_id,notes) 
            VALUES (%s,%s,%s) RETURNING id"""
    values = [song.title, song.album.id, song.notes]
    results = run_sql(sql, values)
    song.id = results[0]["id"]


# Read
def select_all():
    songs = []
    sql = "SELECT * FROM songs"
    results = run_sql(sql)
    for row in results:
        song = _build_song(row)
        songs.append(song)
    return songs


def select(id):
    song = None
    sql = "SELECT * FROM songs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        song = _build_song(row)
    return song


def select_all_with_album(album_id):
    songs = []
    sql = "SELECT * FROM songs WHERE album_id = %s"
    values = [album_id]
    results = run_sql(sql, values)
    for row in results:
        song = _build_song(row)
        songs.append(song)
        print(song)
    print(album_id, ". num_songs:", len(songs))
    return songs


def select_all_completion_with_album(album_id):
    songs_completion = []
    sql = "SELECT id FROM songs WHERE album_id = %s"
    values = [album_id]
    results = run_sql(sql, values)
    for row in results:
        parts_status = part_repository.select_all_status_with_song(row["id"])
        song_completion = _calculate_song_completion(parts_status)
        songs_completion.append(song_completion)
    return songs_completion


# Update
def update(song):
    sql = "UPDATE songs SET (title, album_id, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [song.title, song.album.id, song.notes, song.id]
    run_sql(sql, values)


# Delete
def delete_all():
    sql = "DELETE FROM songs"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM songs WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def _calculate_song_completion(parts_status):
    completion = 0
    if parts_status:
        total = sum(status for status in parts_status)
        possible = len(parts_status) * 5
        completion = total / possible * 100
    return int(completion)


# Builder
def _build_song(row):
    album = album_repository.select(row["album_id"])
    parts_status = part_repository.select_all_status_with_song(row["id"])
    return Song(row["title"], album, parts_status, row["notes"], row["id"])
