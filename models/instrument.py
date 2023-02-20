from dataclasses import dataclass


@dataclass
class Instrument:
    name: str
    icon: str
    id: int = None
