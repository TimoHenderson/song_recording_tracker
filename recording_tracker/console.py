import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
import repositories.instrument_repository as instrument_repository
import repositories.artist_repository as artist_repository
from models.song import Song
from models.part import Part
from models.instrument import Instrument
from models.artist import Artist


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


artist1 = Artist("U2")
artist_repository.save(artist1)


artist1.name = "Egg"
artist_repository.update(artist1)

print(artist_repository.select(artist1.id))
# print_artists()

# breakpoint()
