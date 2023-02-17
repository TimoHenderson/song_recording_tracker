import repositories.song_repository as song_repository
from models.song import Song

song3 = Song("SDKMN", "The Purple Felts", "The Jester's Game")
song_repository.save(song3)
