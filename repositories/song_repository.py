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
    if results:
        songs = _build_songs(results)
    return songs


def select(id):
    song = None
    sql = "SELECT * FROM songs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        song = _build_songs(results)[0]
    return song


def select_for_parts(id):
    song = None
    sql = "SELECT * FROM songs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        song = _build_songs(results, False)[0]
    return song


def select_all_with_album(album_id):
    songs = []
    sql = "SELECT * FROM songs WHERE album_id = %s"
    values = [album_id]
    results = run_sql(sql, values)
    if results:
        songs = _build_songs(results)
    return songs


def select_all_completion_with_album(album_id):
    songs_completions = []
    sql = "SELECT id FROM songs WHERE album_id = %s"
    values = [album_id]
    results = run_sql(sql, values)
    for row in results:
        parts_status = part_repository.select_all_status_with_song(row["id"])
        song_completion = _calculate_song_completion(parts_status)
        songs_completions.append(song_completion)
    return songs_completions


# Update
def update(song):
    sql = "UPDATE songs SET (title, album_id, notes) = (%s, %s, %s) WHERE id = %s"
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


def _build_songs(rows, get_parts_status=True):
    albums = {}
    songs = []

    for song_dict in rows:
        album_id = song_dict["album_id"]
        if album_id not in albums.keys():
            album = album_repository.select_for_songs(album_id)
            albums[album_id] = album
        else:
            album = albums[album_id]
        song = _build_song(song_dict, album, get_parts_status)
        if get_parts_status:
            album.song_completion = _calculate_song_completion(song.parts_status)
        songs.append(song)
    return songs


# Builder
def _build_song(row, album, get_parts_status=True):

    parts_status = (
        part_repository.select_all_status_with_song(row["id"])
        if get_parts_status
        else []
    )

    return Song(row["title"], album, parts_status, row["notes"], row["id"])
