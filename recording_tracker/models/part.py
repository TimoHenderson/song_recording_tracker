class Part:
    def __init__(self, name, status, instrument="", song=None, notes="", id=None):
        self.name = name
        self.status = status
        self.song = song
        self.instrument = instrument
        self.notes = notes
        self.id = None
