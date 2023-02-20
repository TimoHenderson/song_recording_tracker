from dataclasses import dataclass
from models.artist import Artist


@dataclass
class Album:
    name: str
    artist: Artist
    id: int = None
