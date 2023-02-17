from db.run_sql import run_sql
from models.song import Song

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
        song = Song(row["title"], row["artist"], row["album"], row["notes"], row["id"])
        songs.append(song)
    return songs


def select(id):
    song = None
    sql = "SELECT * FROM songs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        song = Song(row["title"], row["artist"], row["album"], row["notes"], row["id"])
    return song
