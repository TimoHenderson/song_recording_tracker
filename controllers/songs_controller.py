from flask import Blueprint, render_template, request, redirect
import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
import repositories.album_repository as album_repository
from models.song import Song

songs_blueprint = Blueprint("songs", __name__)

# View all
@songs_blueprint.route("/songs")
def show_all():
    songs = song_repository.select_all()
    return render_template("songs/index.html", songs=songs)


# View One
@songs_blueprint.route("/albums/<album_id>/songs/<id>")
def show(album_id, id):
    parts = part_repository.select_all_with_song(id)
    song = song_repository.select(id)
    return render_template("songs/show.html", song=song, parts=parts)


# New
@songs_blueprint.route("/albums/<album_id>/songs/new")
def new(album_id):
    album = album_repository.select(album_id)
    return render_template("songs/new.html", album=album)


# Create
@songs_blueprint.route("/albums/<album_id>/songs", methods=["POST"])
def create(album_id):
    form = request.form
    album = album_repository.select(album_id)
    new_song = Song(form["title"], album, form["notes"])
    song_repository.save(new_song)
    return redirect(f"/albums/{album_id}/songs/{new_song.id}")


# Edit
@songs_blueprint.route("/albums/<album_id>/songs/<id>/edit")
def edit(album_id, id):
    song = song_repository.select(id)
    albums = album_repository.select_all()
    return render_template("songs/edit.html", song=song, albums=albums)


# Update
@songs_blueprint.route("/albums/<album_id>/songs/<id>/update", methods=["POST"])
def update(album_id, id):
    form = request.form
    album = album_repository.select(int(album_id))
    song = Song(form["title"], album, form["notes"], id=id)
    song_repository.update(song)
    return redirect(f"/albums/{album_id}/songs/{id}")


# Delete Confirm
@songs_blueprint.route("/albums/<album_id>/songs/<id>/delete")
def confirm_delete(album_id, id):
    song = song_repository.select(id)
    return render_template("songs/delete.html", song=song)


# Actually Delete
@songs_blueprint.route("/albums/<album_id>/songs/<id>/delete", methods=["POST"])
def delete(album_id, id):
    album = album_repository.select(album_id)
    song_repository.delete(id)
    return redirect(f"/artists/{album.artist.id}/albums/{album_id}")
