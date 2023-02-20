from db.run_sql import run_sql
from models.artist import Artist

# Create
def save(artist):
    sql = """INSERT INTO artists (name) 
            VALUES (%s) RETURNING id"""
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]["id"]
