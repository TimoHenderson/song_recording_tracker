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

# song1 = Song(
#     "The Jester",
#     "The Purple Felts",
#     "The Jester's Game",
#     "This needs more parts",
# )
# song_repository.save(song1)

# print_songs()


breakpoint()

# song3.title = "XBGER"
# song_repository.update(song3)
# print_songs()

# song = song_repository.select(1)
# print(song.__dict__)

# song_repository.delete_all()
# print_songs()

# song_repository.delete(9)
# print_songs()

# guitar1 = Part("guitar1", 5, 1)
# part_repository.save(guitar1)
# guitar2 = Part("Guitar 2", 5, 1)
# part_repository.save(guitar2)
# guitar3 = Part("Guitar 3", 5, 2)
# part_repository.save(guitar3)

# got_guitar = song_repository.select(1)

# [print(part.__dict__) for part in part_repository.select_all_with_song(got_guitar.id)]

# print_parts()

# print(part_repository.select(2).__dict__)

# guitar1.name = "Egg"
# part_repository.update(guitar1)


# print()
# print_parts()

# part_repository.delete(3)

# print()
# print_parts()

# part_repository.delete_all()
# print()
# print_parts()
