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
        [print(song.__dict__) for song in songs]
    else:
        print("No songs")


def print_parts():
    parts = part_repository.select_all()
    if parts:
        [print(part.__dict__) for part in parts]
    else:
        print("No parts")


def print_instruments():
    instruments = instrument_repository.select_all()
    if instruments:
        [print(instrument.__dict__) for instrument in instruments]
    else:
        print("No instruments")


def print_artists():
    artists = artist_repository.select_all()
    if artists:
        [print(artist.__dict__) for artist in artists]
    else:
        print("No Artists")


def print_albums():
    albums = album_repository.select_all()
    if albums:
        [print(album.__dict__) for album in albums]
    else:
        print("No albums")


artist1 = artist_repository.select(1)
album1 = Album("The eggmen", artist1)
album_repository.save(album1)
album_repository.save(album1)

# print(album_repository.select(album1.id))
# album1.name = "Fried egg"
# album_repository.update(album1)
# print(album_repository.select(album1.id))
# album_repository.deactivate(album1.id)
print_albums()
album_repository.delete(album1.id)
# print()

# album_repository.delete_all()
print_albums()

# breakpoint()
