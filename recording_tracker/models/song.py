from models.part import Part


class Song:
    def __init__(self, title, artist, album, notes="", parts=[]):
        self.title = title
        self.artist = artist
        self.album = album
        self.notes = notes
        self.parts = parts
