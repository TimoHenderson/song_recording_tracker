from models.part import Part


class Song:
    def __init__(self, title, artist, album, parts=[], notes="", id=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.notes = notes
        self.parts = parts
        self.id = id

    def get_completion(self):
        if self.parts == []:
            completion = 0
        else:
            total = 0
            for part in self.parts:
                total += part.status
            num_parts = len(self.parts)
            possible = num_parts * 5
            completion = total / possible * 100

        return completion

    def __repr__(self):
        return f"{self.title}, {self.artist}"
