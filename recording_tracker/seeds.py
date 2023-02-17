import repositories.song_repository as song_repository
from models.song import Song


def print_songs():
    [print(song.__dict__) for song in songs]


song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")
song_repository.save(song3)

songs = song_repository.select_all()
print_songs()

song = song_repository.select(2)
print(song.__dict__)
