from flask import Blueprint, render_template, request, redirect
from repositories import part_repository, song_repository, instrument_repository
from models.part import Part


parts_blueprint = Blueprint("parts", __name__)

# View all
@parts_blueprint.route("/parts")
def show_all():
    parts = part_repository.select_all()
    return render_template("parts/index.html", parts=parts)


# View One
@parts_blueprint.route("/songs/<song_id>/parts/<id>")
def show(song_id, id):
    return redirect(f"/songs/{song_id}/parts/{id}/edit")


# New
@parts_blueprint.route("/songs/<song_id>/parts/new")
def new_part(song_id):
    song = song_repository.select(song_id)
    instruments = instrument_repository.select_all()
    return render_template("parts/new.html", song=song, instruments=instruments)


# Create
@parts_blueprint.route("/songs/<song_id>/parts", methods=["POST"])
def create(song_id):
    form = request.form
    song = song_repository.select(song_id)
    instrument = instrument_repository.select(form["instrument_id"])
    new_part = Part(form["name"], form["status"], song, instrument, form["notes"])
    part_repository.save(new_part)
    return redirect(f"/albums/{song.album.id}/songs/{song_id}")


# Edit
@parts_blueprint.route("/songs/<song_id>/parts/<id>/edit")
def edit(song_id, id):
    part = part_repository.select(id)
    instruments = instrument_repository.select_all()
    return render_template("parts/edit.html", part=part, instruments=instruments)


# Update
@parts_blueprint.route("/songs/<song_id>/parts/<id>/update", methods=["POST"])
def update(song_id, id):
    form = request.form
    print(form.keys())
    print(form["notes"])
    song = song_repository.select(song_id)
    if len(form.keys()) == 1 and form["notes"]:
        part = part_repository.select(id)
        part.notes = form["notes"]
    else:
        instrument = instrument_repository.select(form["instrument_id"])
        part = Part(
            form["name"],
            form["status"],
            song,
            instrument,
            form["notes"],
            id,
        )
    part_repository.update(part)
    return redirect(f"/albums/{song.album.id}/songs/{song_id}")


# Delete Confirm
@parts_blueprint.route("/songs/<song_id>/parts/<id>/delete")
def confirm_delete(song_id, id):
    part = part_repository.select(id)
    song = part.song
    return render_template("parts/delete.html", part=part, song=song)


# Actually Delete
@parts_blueprint.route("/songs/<song_id>/parts/<id>/delete", methods=["POST"])
def delete(song_id, id):
    song = song_repository.select(song_id)
    part_repository.delete(id)
    return redirect(f"/albums/{song.album.id}/songs/{song.id}")
