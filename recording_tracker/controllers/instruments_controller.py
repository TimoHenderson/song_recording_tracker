from flask import Blueprint, render_template, request, redirect
from repositories import instrument_repository
from models.instrument import Instrument


instruments_blueprint = Blueprint("instruments", __name__)

# View all
@instruments_blueprint.route("/instruments")
def show_all():
    instruments = instrument_repository.select_all()
    return render_template("instruments/index.html", instruments=instruments)


# View One
@instruments_blueprint.route("/instruments/<id>")
def show(id):
    instrument = instrument_repository.select(id)
    return render_template("instruments/show.html", instrument=instrument)


# New
@instruments_blueprint.route("/instruments/new")
def new_instrument():
    icons = get_icons()
    return render_template("instruments/new.html", icons=icons)


# Create
@instruments_blueprint.route("/instruments", methods=["POST"])
def create():
    form = request.form
    new_instrument = Instrument(form["name"], form["icon"])
    instrument_repository.save(new_instrument)
    return redirect("/instruments")


def get_icons():
    return ["a", "b", "c", "d", "e", "f"]
