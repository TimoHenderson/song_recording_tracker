import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
from models.song import Song
from models.part import Part


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


# song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")
# song_repository.save(song3)


# print_songs()

# song3.title = "XBGER"
# song_repository.update(song3)
# print_songs()

# song = song_repository.select(1)
# print(song.__dict__)

# song_repository.delete_all()
# print_songs()

# song_repository.delete(9)
# print_songs()

guitar1 = Part("Verse Chords", 5, 1)
part_repository.save(guitar1)

print_parts()
