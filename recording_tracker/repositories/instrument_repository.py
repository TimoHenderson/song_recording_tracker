from db.run_sql import run_sql
from models.instrument import Instrument

# Create
def save(instrument):
    sql = """INSERT INTO instruments (name,icon) 
            VALUES (%s,%s) RETURNING id"""
    values = [instrument.name, instrument.icon]
    results = run_sql(sql, values)
    instrument.id = results[0]["id"]
