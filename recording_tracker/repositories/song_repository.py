from db.run_sql import run_sql
from models.song import Song

# Create
def save(song):
    sql = """INSERT INTO songs (title,artist,album,notes) 
            VALUES (%s,%s,%s,%s) RETURNING id"""
    values = [song.title, song.artist, song.album, song.notes]
    results = run_sql(sql, values)
    song.id = results[0]["id"]


# Read
# def select_all():
#     sql = "SELECT * FROM songs"
#     results = run_sql(sql)
