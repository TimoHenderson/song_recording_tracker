from flask import Blueprint, render_template, request, redirect
from repositories import artist_repository
from models.artist import Artist


artists_blueprint = Blueprint("artists", __name__)

# View all
@artists_blueprint.route("/artists")
def show_all():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists=artists)


# View One
@artists_blueprint.route("/artists/<id>")
def show(id):
    artist = artist_repository.select(id)
    return render_template("artists/show.html", artist=artist)


# New
@artists_blueprint.route("/artists/new")
def new_artist():
    return render_template("artists/new.html")


# Create
@artists_blueprint.route("/artists", methods=["POST"])
def create():
    form = request.form
    new_artist = Artist(form["name"])
    artist_repository.save(new_artist)
    return redirect("/artists")


# Edit
@artists_blueprint.route("/artists/<id>/edit")
def edit(id):
    print(id)
    artist = artist_repository.select(id)
    return render_template("artists/edit.html", artist=artist)


# Update
@artists_blueprint.route("/artists/<id>/update", methods=["POST"])
def update(id):
    form = request.form
    artist = Artist(form["name"], id)
    artist_repository.update(artist)
    return redirect("/artists")
