from flask import Blueprint, render_template, request, redirect
from repositories import album_repository
from repositories import artist_repository
from repositories import song_repository
from models.album import Album


albums_blueprint = Blueprint("albums", __name__)

# View all
@albums_blueprint.route("/albums")
def show_all():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)


# View One
@albums_blueprint.route("/artists/<artist_id>/albums/<id>")
def show(artist_id, id):
    album = album_repository.select(id)
    songs = song_repository.select_all_with_album(id)
    return render_template("albums/show.html", album=album, songs=songs)


# New
@albums_blueprint.route("/artists/<artist_id>/albums/new")
def new_album(artist_id):
    artist = artist_repository.select(artist_id)
    return render_template("albums/new.html", artist=artist)


# Create
@albums_blueprint.route("/artists/<artist_id>/albums", methods=["POST"])
def create(artist_id):
    form = request.form
    artist = artist_repository.select(artist_id)
    new_album = Album(form["name"], artist)
    album_repository.save(new_album)
    return redirect(f"/artists/<artist_id>/albums/<album_id>")


# Edit
@albums_blueprint.route("/artists/<artist_id>/albums/<id>/edit")
def edit(artist_id, id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    return render_template("albums/edit.html", album=album, artists=artists)


# Update
@albums_blueprint.route("/artists/<artist_id>/albums/<id>/update", methods=["POST"])
def update(artist_id, id):
    form = request.form
    artist = artist_repository.select(form["artist_id"])
    album = Album(form["name"], artist, id=id)
    album_repository.update(album)
    return redirect(f"artists/{artist_id}/albums/{id}")


# Delete Confirm
@albums_blueprint.route("/artists/<artist_id>/albums/<id>/delete")
def confirm_delete(artist_id, id):
    album = album_repository.select(id)
    return render_template(f"artists/{artist_id}albums/delete.html", album=album)


# Actually Delete
@albums_blueprint.route("/artists/<artist_id>/albums/<id>/delete", methods=["POST"])
def delete(artist_id, id):
    album_repository.deactivate(id)
    return redirect(f"/artists/{artist_id}")
