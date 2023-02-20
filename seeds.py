import repositories.song_repository as song_repository
import repositories.part_repository as part_repository
import repositories.instrument_repository as instrument_repository
import repositories.artist_repository as artist_repository
from models.song import Song
from models.part import Part
from models.instrument import Instrument
from models.artist import Artist


instrument1 = Instrument("Guitar", "e900")
instrument_repository.save(instrument1)

instrument2 = Instrument("Drums", "e92c")
instrument_repository.save(instrument2)

artist1 = Artist("U2")
artist_repository.save(artist1)


# song1 = Song("SDKMN", artist1, "The Jester's Game", "Total Rubbish")
# song_repository.save(song1)

# song2 = Song("The Jester", artist1, "The Jester's Game", "Really Good")
# song_repository.save(song1)

# part1 = Part("Verse Chords", 3, song1.id, instrument1, "Needs to be better")
# part_repository.save(part1)
# part2 = Part("End Shred", 3, song1.id, instrument2, "Needs to be better")
# part_repository.save(part2)
