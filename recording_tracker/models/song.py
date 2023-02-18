from models.part import Part


class Song:
    def __init__(self, title, artist, album, notes="", id=None, parts=[]):
        self.title = title
        self.artist = artist
        self.album = album
        self.notes = notes
        self.parts = parts
        self.id = id

    def get_completion(self):
        completion = 0
        if self.parts:
            total = sum(part.status for part in self.parts)
            possible = len(self.parts) * 5
            completion = total / possible * 100
        return int(completion)

    def __repr__(self):
        return f"{self.title}, {self.artist}"
