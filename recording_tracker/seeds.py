import repositories.song_repository as song_repository
from models.song import Song


def print_songs():
    songs = song_repository.select_all()
    if songs:
        [print(song.__dict__) for song in songs]
    else:
        print("No songs")


song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")
song_repository.save(song3)


print_songs()

song = song_repository.select(1)
print(song.__dict__)

song_repository.delete_all()
print_songs()
