from flask import Flask, render_template, request, redirect
from repositories import song_repository
from models.song import Song
from flask import Blueprint

songs_blueprint = Blueprint("songs", __name__)

# View all
@songs_blueprint.route("/songs")
def show_all():
    songs = song_repository.select_all()
    return render_template("songs/index.html", songs=songs)


# View One
@songs_blueprint.route("/songs/<id>")
def show(id):
    song = song_repository.select(id)
    return render_template("songs/show.html", song=song)


# New
@songs_blueprint.route("/songs/new")
def new():
    return render_template("songs/new.html")


# Create
@songs_blueprint.route("/songs", methods=["POST"])
def create():
    form = request.form
    new_song = Song(form["title"], form["artist"], form["album"], form["notes"])
    song_repository.save(new_song)
    return redirect("/songs")


# Edit
@songs_blueprint.route("/songs/<id>/edit")
def edit(id):
    song = song_repository.select(id)
    return render_template("songs/edit.html", song=song)


# Update
@songs_blueprint.route("/songs/<id>/update", methods=["POST"])
def update(id):
    form = request.form
    song = Song(form["title"], form["artist"], form["album"], form["notes"], id=id)
    song_repository.update(song)
    return redirect(f"/songs/{id}")


# Delete
@songs_blueprint.route("/songs/<id>/delete")
def delete(id):
    song = song_repository.select(id)
    return render_template("songs/delete.html", song=song)
