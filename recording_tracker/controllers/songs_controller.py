from flask import Flask, render_template, request, redirect
from repositories import song_repository
from models.song import Song
from flask import Blueprint

songs_blueprint = Blueprint("songs", __name__)


@songs_blueprint.route("/songs")
def show_all():
    songs = song_repository.select_all()
    return render_template("songs/index.html", songs=songs)
