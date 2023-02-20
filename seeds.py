import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
import repositories.instrument_repository as instrument_repository
from models.song import Song
from models.part import Part
from models.instrument import Instrument


instrument1 = Instrument("Guitar", "e900")
instrument_repository.save(instrument1)

instrument2 = Instrument("Drums", "e92c")
instrument_repository.save(instrument2)


song1 = Song("SDKMN", "The Purple Felts", "The Jester's Game", "Total Rubbish")
song_repository.save(song1)

song2 = Song("The Jester", "The Purple Felts", "The Jester's Game", "Really Good")
song_repository.save(song1)

part1 = Part("Verse Chords", 3, song1.id, instrument1, "Needs to be better")
part_repository.save(part1)
part2 = Part("End Shred", 3, song1.id, instrument2, "Needs to be better")
part_repository.save(part2)
