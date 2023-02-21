from dataclasses import dataclass, field
from models.artist import Artist


@dataclass
class Album:
    name: str
    artist: Artist
    songs_completion: list[int] = field(default_factory=list)
    id: int = None
