from dataclasses import dataclass


@dataclass
class Song:
    title: str
    artist: str
    album: str
    notes: str = ""
