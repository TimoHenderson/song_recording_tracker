from dataclasses import dataclass
from models.song import Song
from models.instrument import Instrument


@dataclass
class Part:
    name: str
    status: int
    song: Song = None
    instrument: Instrument = None
    notes: str = ""
    id: int = None

    def get_status_str(self):
        if self.status == 0:
            status_str = "Not Started"
        elif self.status == 1:
            status_str = "Tracking Guides"
        elif self.status == 2:
            status_str = "Tracking Part"
        elif self.status == 3:
            status_str = "Doing drop ins"
        elif self.status == 4:
            status_str = "Comping"
        elif self.status == 5:
            status_str = "Take!"
        return status_str
