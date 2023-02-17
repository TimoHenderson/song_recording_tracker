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
        part = build_part(row)
        parts.append(part)
    return parts


def select(id):
    part = None
    sql = "SELECT * FROM parts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        part = build_part(row)
    return part


def select_all_with_song(song_id):
    parts = []
    sql = "SELECT * FROM parts WHERE song_id = %s"
    values = [song_id]
    results = run_sql(sql, values)
    for row in results:
        part = build_part(row)
        parts.append(part)
    return parts


# Update
def update(part):
    sql = """UPDATE parts SET (name,status,song_id,instrument,notes) 
            = (%s,%s,%s,%s,%s) WHERE id = %s"""
    values = [
        part.name,
        part.status,
        part.song_id,
        part.instrument,
        part.notes,
        part.id,
    ]
    run_sql(sql, values)


# Delete
def delete_all():
    sql = "DELETE FROM parts"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM parts WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Builder
def build_part(row):
    return Part(
        row["name"],
        row["status"],
        row["song_id"],
        row["instrument"],
        row["notes"],
        row["id"],
    )
