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


# View One
@songs_blueprint.route("/songs/new")
def new():
    return render_template("songs/new.html")
