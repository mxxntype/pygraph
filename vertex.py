from dataclasses import dataclass
from typing import Union

@dataclass
class Vertex:
    weight: Union[int, str]
    index: int = 0

    def __init__(self, index: int = 0) -> None:
        self.index = index