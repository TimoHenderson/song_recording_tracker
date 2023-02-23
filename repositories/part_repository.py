from db.run_sql import run_sql
from models.part import Part
import repositories.instrument_repository as instrument_repository
import repositories.song_repository as song_repository
from pprint import pprint


# Create
def save(part):
    sql = """INSERT INTO parts (name,status,song_id,instrument_id,notes) 
            VALUES (%s,%s,%s,%s,%s) RETURNING id"""
    values = [part.name, part.status, part.song.id, part.instrument.id, part.notes]
    results = run_sql(sql, values)
    part.id = results[0]["id"]


# Read
def select_all():

    sql = "SELECT * FROM parts"
    results = run_sql(sql)
    parts = _build_parts(results)
    return parts


def select(id):
    part = None
    sql = "SELECT * FROM parts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        part = _build_part(row)
    return part


def select_all_with_song(song_id):
    parts = []
    sql = "SELECT * FROM parts WHERE song_id = %s"
    values = [song_id]
    results = run_sql(sql, values)
    for row in results:
        part = _build_part(row)
        parts.append(part)
    return parts


def select_all_status_with_song(song_id):
    parts_status = []
    sql = "SELECT status FROM parts WHERE song_id = %s"
    values = [song_id]
    results = run_sql(sql, values)
    for row in results:
        parts_status.append(row["status"])
    return parts_status


# Update
def update(part):
    sql = """UPDATE parts SET (name,status,song_id,instrument_id,notes) 
            = (%s,%s,%s,%s,%s) WHERE id = %s"""
    values = [
        part.name,
        part.status,
        part.song.id,
        part.instrument.id,
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
def _build_parts(rows):
    # split rows into dictionaries with key song_id
    parts_by_song_id = {}
    for part_dict in rows:
        song_id = part_dict["song_id"]
        if song_id not in parts_by_song_id:
            parts_by_song_id[song_id] = [part_dict]
        else:
            parts_by_song_id[song_id].append(part_dict)
    pprint(parts_by_song_id.keys())
    songs_by_id = {}
    for song_id in parts_by_song_id.keys():
        songs_by_id[song_id] = song_repository.select(song_id)

    pprint(songs_by_id)
    breakpoint()

    # instrument = instrument_repository.select(row["instrument_id"])
    # song = song_repository.select(row["song_id"])
    # return Part(
    #     row["name"],
    #     row["status"],
    #     song,
    #     instrument,
    #     row["notes"],
    #     row["id"],
    # )
