from flask import Blueprint, render_template, request, redirect
from repositories import artist_repository
from models.artist import Artist


artists_blueprint = Blueprint("artists", __name__)

# View all
@artists_blueprint.route("/artists")
def show_all():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists=artists)
