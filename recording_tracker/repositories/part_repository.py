from db.run_sql import run_sql
from models.part import Part

# Create
def save(part):
    sql = """INSERT INTO parts (name,status,song_id,instrument,notes) 
            VALUES (%s,%s,%s,%s,%s) RETURNING id"""
    values = [part.name, part.status, part.song_id, part.instrument, part.notes]
    results = run_sql(sql, values)
    part.id = results[0]["id"]
