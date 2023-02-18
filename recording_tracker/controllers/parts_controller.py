from flask import Blueprint, render_template, request, redirect
from repositories import part_repository, song_repository
from models.part import Part


parts_blueprint = Blueprint("parts", __name__)

# View all
@parts_blueprint.route("/parts")
def show_all():
    parts = part_repository.select_all()
    return render_template("parts/index.html", parts=parts)


# View One
@parts_blueprint.route("/parts/<id>")
def show(id):
    part = part_repository.select(id)
    return render_template("parts/show.html", part=part)


# New
@parts_blueprint.route("/songs/<song_id>/parts/new")
def new(song_id):
    song = song_repository.select(song_id)
    return render_template("parts/new.html", song=song)


# Create
@parts_blueprint.route("/parts", methods=["POST"])
def create():
    form = request.form
    song_id = form["song_id"]
    new_part = Part(form["name"], 0, song_id, form["instrument"], form["notes"])
    part_repository.save(new_part)
    return redirect(f"/songs/{song_id}")


# Edit
@parts_blueprint.route("/parts/<id>/edit")
def edit(id):
    part = part_repository.select(id)
    song = song_repository.select(part.song_id)
    return render_template("parts/edit.html", part=part, song=song)
