class Part:
    def __init__(self, name, status, song_id, instrument="", notes="", id=None):
        self.name = name
        self.status = status
        self.song_id = song_id
        self.instrument = instrument
        self.notes = notes
        self.id = id

    def __repr__(self):
        return f"{self.name}, {self.status}"
