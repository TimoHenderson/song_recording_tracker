from flask import Blueprint, render_template, request, redirect
from repositories import instrument_repository
from models.instrument import Instrument


instruments_blueprint = Blueprint("instruments", __name__)

# View all
@instruments_blueprint.route("/instruments")
def show_all():
    instruments = instrument_repository.select_all()
    return render_template("instruments/index.html", instruments=instruments)
