from db.run_sql import run_sql
from models.instrument import Instrument

# Create
def save(instrument):
    sql = """INSERT INTO instruments (name,icon) 
            VALUES (%s,%s) RETURNING id"""
    values = [instrument.name, instrument.icon]
    results = run_sql(sql, values)
    instrument.id = results[0]["id"]


# Read
def select_all():
    instruments = []
    sql = "SELECT * FROM instruments"
    results = run_sql(sql)
    for row in results:
        instrument = build_instrument(row)
        instruments.append(instrument)
    return instruments


def select(id):
    instrument = None
    sql = "SELECT * FROM instruments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        instrument = build_instrument(row)
    return instrument


# Update
def update(instrument):
    sql = "UPDATE instruments SET (name,icon) = (%s,%s) WHERE id = %s"
    values = [instrument.name, instrument.icon, instrument.id]
    run_sql(sql, values)


def build_instrument(row):
    return Instrument(row["name"], row["icon"], row["id"])
