from db.run_sql import run_sql
from models.part import Part

# Create
def save(part):
    sql = """INSERT INTO parts (name,status,song_id,instrument,notes) 
            VALUES (%s,%s,%s,%s,%s) RETURNING id"""
    values = [part.name, part.status, part.song_id, part.instrument, part.notes]
    results = run_sql(sql, values)
    part.id = results[0]["id"]


# Read
def select_all():
    parts = []
    sql = "SELECT * FROM parts"
    results = run_sql(sql)
    for row in results:
        part = Part(
            row["name"],
            row["status"],
            row["song_id"],
            row["instrument"],
            row["notes"],
            row["id"],
        )
        parts.append(part)
    return parts
