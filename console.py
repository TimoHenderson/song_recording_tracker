import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
import repositories.instrument_repository as instrument_repository
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository
from models.song import Song
from models.part import Part
from models.instrument import Instrument
from models.artist import Artist
from models.album import Album


def print_songs():
    songs = song_repository.select_all()
    if songs:
        [print(song) for song in songs]
    else:
        print("No songs")


def print_parts():
    parts = part_repository.select_all()
    if parts:
        [print(part) for part in parts]
    else:
        print("No parts")


def print_instruments():
    instruments = instrument_repository.select_all()
    if instruments:
        [print(instrument) for instrument in instruments]
    else:
        print("No instruments")


def print_artists():
    artists = artist_repository.select_all()
    if artists:
        [print(artist) for artist in artists]
    else:
        print("No Artists")


def print_albums():
    albums = album_repository.select_all()
    if albums:
        [print(album) for album in albums]
    else:
        print("No albums")


breakpoint()
