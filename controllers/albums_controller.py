from flask import Blueprint, render_template, request, redirect
from repositories import album_repository
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
