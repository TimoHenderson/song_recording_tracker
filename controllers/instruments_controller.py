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
@instruments_blueprint.route("/songs/<song_id>/parts/<part_id>/instruments/new")
@instruments_blueprint.route("/songs/<song_id>/instruments/new")
def new_instrument(song_id=None, part_id=None):
    icons = get_icons()
    return render_template(
        "instruments/new.html", icons=icons, song_id=song_id, part_id=part_id
    )


# Create
@instruments_blueprint.route("/instruments", methods=["POST"])
def create():
    form = request.form
    new_instrument = Instrument(form["name"], form["icon"])
    instrument_repository.save(new_instrument)
    if "song_id" in form and "part_id" in form:
        url_string = f"/songs/{form['song_id']}/parts/{form['part_id']}"
    elif "song_id" in form:
        url_string = f"/songs/{form['song_id']}/parts/new"
    else:
        url_string = "/instruments"
    return redirect(url_string)


# Edit
@instruments_blueprint.route("/instruments/<id>/edit")
def edit(id):
    instrument = instrument_repository.select(id)
    icons = get_icons()
    return render_template("instruments/edit.html", instrument=instrument, icons=icons)


# Update
@instruments_blueprint.route("/instruments/<id>/update", methods=["POST"])
def update(id):
    form = request.form
    instrument = Instrument(form["name"], form["icon"], id)
    instrument_repository.update(instrument)
    return redirect("/instruments")


# Delete Confirm
@instruments_blueprint.route("/instruments/<id>/delete")
def confirm_delete(id):
    instrument = instrument_repository.select(id)
    return render_template("instruments/delete.html", instrument=instrument)


# Actually Delete
@instruments_blueprint.route("/instruments/<id>/delete", methods=["POST"])
def delete(id):
    instrument_repository.deactivate(id)
    return redirect("/instruments")


def get_icons():
    icon_list = [
        "e92c",
        "e923",
        "e928",
        "e920",
        "e912",
        "e910",
        "e907",
        "e91e",
        "e917",
        "e91d",
        "e911",
        "e927",
        "e913",
        "e90f",
        "e90c",
        "e915",
        "e922",
        "e92b",
    ]
    return icon_list
