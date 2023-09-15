from dataclasses import dataclass
from vertex import Vertex

@dataclass
class Edge:
    starting_vertex: Vertex
    ending_vertex: Vertex
    weight: int = 0

    def __init__(self,
        starting_vertex: Vertex,
        ending_vertex: Vertex,
        weight: int = 0
    ) -> None:
        self.starting_vertex = starting_vertex
        self.ending_vertex = ending_vertex
        self.weight = weight
        
    def invert(self) -> None:
        tmp = self.starting_vertex
        self.starting_vertex = self.ending_vertex
        self.ending_vertex = tmp
