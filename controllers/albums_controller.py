from flask import Blueprint, render_template, request, redirect
from repositories import album_repository
from repositories import artist_repository
from models.album import Album


albums_blueprint = Blueprint("albums", __name__)

# View all
@albums_blueprint.route("/albums")
def show_all():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums=albums)


# View One
@albums_blueprint.route("/albums/<id>")
def show(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album=album)


# New
@albums_blueprint.route("/albums/new")
def new_album():
    artists = artist_repository.select_all()
    return render_template("albums/new.html", artists=artists)


# Create
@albums_blueprint.route("/albums", methods=["POST"])
def create():
    form = request.form
    artist = artist_repository.select(form["artist_id"])
    new_album = Album(form["name"], artist)
    album_repository.save(new_album)
    return redirect("/albums")
