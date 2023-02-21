from dataclasses import dataclass, field
from models.artist import Artist


@dataclass
class Album:
    name: str
    artist: Artist
    songs_completion: list[int] = field(default_factory=list)
    id: int = None

    def get_completion(self):
        completion = 0
        if self.songs_completion:
            total = sum(song for song in self.songs_completion)
            completion = int(total / len(self.songs_completion))
        return completion

    def get_num_songs(self):
        return len(self.songs_completion)
