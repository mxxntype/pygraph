from dataclasses import dataclass
from typing import Union

@dataclass
class Vertex:
    weight: Union[int, str] = 0
    index: int = 0
    depth: int = -1
    lowlink: int = -1
    on_stack: bool = False

    def __init__(self, index: int = 0) -> None:
        self.index = index

    # Required to be hashable.
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        return self.index == other.index

    # Required to be hashable.
    def __hash__(self) -> int:
        return hash(self.index)
