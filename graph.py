from typing import Union

from vertex import Vertex
from edge import Edge

class Graph:
    edges: list[Edge] = []
    
    def __init__(self, edges: list[Edge] = []) -> None:
        self.edges = edges

    # Return the index of the first vertex reachable from the given one
    # Returns `None` if the given vertex is not linked with any other
    def first(self, vertex: Vertex) -> Union[int, None]:
        __connected_edges: list[Edge] = filter(lambda e: e.starting_vertex == vertex, self.edges)
        __connected_vertices: list[Vertex] = map(lambda e: e.ending_vertex, __connected_edges)
        first_vertex: Vertex = min(__connected_vertices, key=lambda v: v.index, default=None)
        return first_vertex.index if first_vertex else None

    # Return the index of the first vertex reachable from the given one that has index greater than the given one
    # Returns `None` if the given vertex is not linked with any other or of i is the index of the last vertex reachable from the given one
    def next(self, vertex: Vertex, i: int) -> Union[int, None]:
        __connected_edges: list[Edge] = filter(lambda e: e.starting_vertex == vertex, self.edges)
        __connected_vertices: list[Vertex] = map(lambda e: e.ending_vertex, __connected_edges)
        __greater_vertices: list[Vertex] = filter(lambda v: v.index > i, __connected_vertices)
        next_vertex: Vertex = min(__greater_vertices, key=lambda v: v.index, default=None)
        return next_vertex.index if next_vertex else None

    # From vertices that are reachable from `vertex`, return the one with the give index
    # Returns `None` if such vertex could not be found
    def vertex(self, vertex: Vertex, index: int) -> Union[Vertex, None]:
        __connected_edges: list[Edge] = filter(lambda e: e.starting_vertex == vertex, self.edges)
        __connected_vertices: list[Vertex] = map(lambda e: e.ending_vertex, __connected_edges)
        matching_vertices: list[Vertex] = filter(lambda v: v.index == index, __connected_vertices)
        return next(matching_vertices, None)

    # Add a vertex to the graph and link it with other vertices, creating them if needed
    def add_vertex(self, vertex: Vertex, connected_vertices: list[Vertex]):
        for connected_vertex in connected_vertices:
            self.add_edge(
                Edge(
                    starting_vertex=vertex,
                    ending_vertex=connected_vertex,
                )
            )

    # Link two vertices, creating them if needed
    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)

    # Remove the given vertex and all edges connected to it
    def remove_vertex(self, vertex: Vertex):
        __tmp_edges = self.edges.copy()
        for edge in self.edges:
            if vertex in [edge.starting_vertex, edge.ending_vertex]:
                __tmp_edges.remove(edge)
        self.edges = __tmp_edges.copy()

    # Unlink two vertices
    def remove_edge(self, edge: Edge) -> None:
        if (edge not in self.edges):
            raise Exception("Cannot remove non-existent edge")
        self.edges.remove(edge)

    # In all edges that have `old_vertex`, replace it with `new_vertex`
    def edit_vertex(self, old_vertex: Vertex, new_vertex: Vertex):
        for edge in self.edges:
            if (edge.starting_vertex == old_vertex):
                edge.starting_vertex = new_vertex
            if (edge.ending_vertex == old_vertex):
                edge.ending_vertex = new_vertex

    # Replace `old_edge` with `new_edge`
    def edit_edge(self, old_edge: Edge, new_edge: Edge):
        self.remove_edge(old_edge)
        self.add_edge(new_edge)

    # Print relations between vertices
    def print(self) -> None:
        for edge in self.edges:
            print(f"Vertex {edge.starting_vertex.index} -> Vertex {edge.ending_vertex.index}")
