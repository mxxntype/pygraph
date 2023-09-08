from dataclasses import dataclass

from vertex import Vertex
from edge import Edge

class Graph:
    node_count: int = 0
    edge_count: int = 0
    edges: list[Edge] = []
    
    def __init__(self, edges: list[Edge] = []) -> None:
        self.edges = edges

    def first(self, v: int) -> int:
        return 0

    def next(self, v: int, i: int) -> int:
        return 0

    def vertex(self, v: int, i: int):
        pass

    def add_vertex(self, id: int, connected_vertices: list[int] = []):
        # TODO: Check that all connected vertices exist
        for connected_vertex in connected_vertices:
            self.edges.append(
                Edge(
                    starting_vertex=Vertex(index=id),
                    ending_vertex=Vertex(index=connected_vertex)
                )
            )

    def add_edge(self, id_1: int, id_2: int) -> None:
        # TODO: Check that both vertices exist
        self.edges.append(
            Edge(
                starting_vertex=Vertex(index=id_1),
                ending_vertex=Vertex(index=id_2)
            )
        )

    def remove_vertex(self, vertex: int):
        tmp = self.edges.copy()
        for edge in self.edges:
            if vertex in [edge.starting_vertex, edge.ending_vertex]:
                tmp.remove(edge)
        self.edges = tmp.copy();

    def remove_edge(self, edge: Edge) -> None:
        self.edges.remove(edge)

    def edit_vertex(self):
        pass

    def edit_edge(self):
        pass

    def print(self) -> None:
        for edge in self.edges:
            print(f"Vertex {edge.starting_vertex.index} -> Vertex {edge.ending_vertex.index}")
