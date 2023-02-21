from dataclasses import dataclass, field


@dataclass
class Artist:
    name: str
    albums_completion: list[int] = field(default_factory=list)
    id: int = None

    def get_completion(self):
        completion = 0
        if self.albums_completion:
            total = sum(album for album in self.albums_completion)
            completion = int(total / len(self.albums_completion))
        return completion

    def get_num_albums(self):
        return len(self.albums_completion)
