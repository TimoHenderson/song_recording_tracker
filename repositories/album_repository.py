from db.run_sql import run_sql
from models.album import Album


# Create
def save(album):
    sql = """INSERT INTO albums (name,artist_id) 
            VALUES (%s,%s) RETURNING id"""
    values = [album.name, album.artist.id]
    results = run_sql(sql, values)
    album.id = results[0]["id"]
