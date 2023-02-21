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


def run_seeds():
    part_repository.delete_all()
    instrument_repository.delete_all()
    song_repository.delete_all()
    album_repository.delete_all()
    artist_repository.delete_all()

    # Artists

    artist1 = Artist("The Purple Felts")
    artist_repository.save(artist1)

    artist2 = Artist("Bar Room Crawl")
    artist_repository.save(artist2)

    artist3 = Artist("Red Pine Timber co.")
    artist_repository.save(artist3)

    # Albums

    album1 = Album("The Jester's Game", artist1)
    album_repository.save(album1)

    album2 = Album("Darker", artist1)
    album_repository.save(album2)

    album3 = Album("Are you Papylonian?", artist2)
    album_repository.save(album3)

    album4 = Album("Paradigm Lost", artist2)
    album_repository.save(album4)

    album5 = Album("Different Lonesome", artist3)
    album_repository.save(album5)

    album6 = Album("Sorry for the Good Times", artist3)
    album_repository.save(album6)

    # Songs

    song1 = Song("SDKMN", album1)
    song_repository.save(song1)
    song2 = Song("Candyfloss", album1)
    song_repository.save(song2)
    song3 = Song("The Jester", album1)
    song_repository.save(song3)

    song4 = Song("EHOB", album2)
    song_repository.save(song4)
    song5 = Song("Darker", album2)
    song_repository.save(song5)

    # Instruments
    instrument1 = Instrument("Guitar", "e900")
    instrument_repository.save(instrument1)
    instrument2 = Instrument("Drums", "e92c")
    instrument_repository.save(instrument2)
    instrument3 = Instrument("Saxophone", "e92c")
    instrument_repository.save(instrument3)

    # Parts
    part1 = Part("Verse Chords", 2, song1, instrument1, "Really Sloppy")
    part_repository.save(part1)
    part2 = Part(
        "Drum Solo!",
        3,
        song1,
        instrument2,
        "Could be tighter, maybe make it more relevant to the rest of the parts",
    )
    part_repository.save(part2)
    part3 = Part(
        "Chorus Stabs",
        2,
        song1,
        instrument3,
        "Really tight, try using take 1 and 2 to comp",
    )
    part_repository.save(part3)


if __name__ == "__main__":
    run_seeds()
