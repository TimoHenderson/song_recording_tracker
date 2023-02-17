class Part:
    def __init__(self, name, status, song_id, instrument="", notes="", id=None):
        self.name = name
        self.status = status
        self.song_id = song_id
        self.instrument = instrument
        self.notes = notes
        self.id = id

    def get_status_str(self):
        match self.status:
            case 0:
                status_str = "Not Started"
            case 1:
                status_str = "Tracking Guides"
            case 2:
                status_str = "Tracking Part"
            case 3:
                status_str = "Doing drop ins"
            case 4:
                status_str = "Comping"
            case 5:
                status_str = "Take!"
        return status_str

    def __repr__(self):
        return f"{self.name}, {self.status}"
