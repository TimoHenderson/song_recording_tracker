from models.part import Part


class Song:
    def __init__(self, title, artist, album, parts=[], notes="", id=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.notes = notes
        self.parts = parts
        self.id = id

    def add_part(self, part):
        self.parts.append(part)

    def __repr__(self):
        return f"{self.title}, {self.artist}"
