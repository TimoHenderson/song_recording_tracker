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
    parts = []
    sql = "SELECT * FROM parts"
    results = run_sql(sql)
    if results:
        parts = _build_parts(results)
    return parts


def select(id):
    part = None
    sql = "SELECT * FROM parts WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        part = _build_parts(results)[0]
    return part


def select_all_with_song(song_id):
    parts = []
    sql = "SELECT * FROM parts WHERE song_id = %s"
    values = [song_id]
    results = run_sql(sql, values)
    if results:
        parts = _build_parts(results)
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
    insts = {}
    songs = {}
    parts = []

    for part_dict in rows:
        song_id = part_dict["song_id"]
        if song_id not in songs.keys():
            song = song_repository.select_for_parts(song_id)
            songs[song_id] = song
        else:
            song = songs[song_id]
        song.parts_status.append(part_dict["status"])

        inst_id = part_dict["instrument_id"]
        if inst_id not in insts.keys():
            inst = instrument_repository.select(inst_id)
            insts[inst_id] = inst
        else:
            inst = insts[inst_id]

        parts.append(_build_part(part_dict, song, inst))
    return parts


def _build_part(row, song, instrument):
    return Part(
        row["name"],
        row["status"],
        song,
        instrument,
        row["notes"],
        row["id"],
    )
