from dataclasses import dataclass, field

from models.album import Album


@dataclass
class Song:

    title: str
    album: Album
    parts_status: list[int] = field(default_factory=list)
    notes: str = ""
    id: int = None

    def get_completion(self):
        completion = 0
        if self.parts_status:
            total = sum(status for status in self.parts_status)
            possible = len(self.parts_status) * 5
            completion = total / possible * 100
        return int(completion)

    def get_num_parts(self):
        return len(self.parts_status)

    def get_parts_status_percent(self):
        return [status * 20 for status in self.parts_status]
