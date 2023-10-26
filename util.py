from graph import Graph
from edge import Edge
from vertex import Vertex

def first_graph() -> Graph:
    graph: Graph = Graph()

    vertex_1: Vertex = Vertex(index=1)
    vertex_2: Vertex = Vertex(index=2)
    vertex_3: Vertex = Vertex(index=3)
    vertex_4: Vertex = Vertex(index=4)
    vertex_5: Vertex = Vertex(index=5)
    vertex_6: Vertex = Vertex(index=6)
    vertex_7: Vertex = Vertex(index=7)

    graph.add_edge(Edge(starting_vertex=vertex_5, ending_vertex=vertex_1))

    # SCC #1
    graph.add_edge(Edge(starting_vertex=vertex_1, ending_vertex=vertex_2))
    graph.add_edge(Edge(starting_vertex=vertex_2, ending_vertex=vertex_3))
    graph.add_edge(Edge(starting_vertex=vertex_3, ending_vertex=vertex_4))
    graph.add_edge(Edge(starting_vertex=vertex_4, ending_vertex=vertex_1))

    # SCC #2
    graph.add_edge(Edge(starting_vertex=vertex_5, ending_vertex=vertex_6))
    graph.add_edge(Edge(starting_vertex=vertex_6, ending_vertex=vertex_7))
    graph.add_edge(Edge(starting_vertex=vertex_7, ending_vertex=vertex_5))

    return graph

def second_graph() -> Graph:
    graph: Graph = Graph()
    vertex_1: Vertex = Vertex(index=1)
    vertex_2: Vertex = Vertex(index=2)
    vertex_3: Vertex = Vertex(index=3)
    vertex_4: Vertex = Vertex(index=4)
    vertex_5: Vertex = Vertex(index=5)
    vertex_6: Vertex = Vertex(index=6)
    vertex_7: Vertex = Vertex(index=7)
    vertex_8: Vertex = Vertex(index=8)
    vertex_9: Vertex = Vertex(index=9)

    graph.add_edge(Edge(starting_vertex=vertex_1, ending_vertex=vertex_4))
    graph.add_edge(Edge(starting_vertex=vertex_4, ending_vertex=vertex_7))

    # SCC #1
    graph.add_edge(Edge(starting_vertex=vertex_1, ending_vertex=vertex_2))
    graph.add_edge(Edge(starting_vertex=vertex_2, ending_vertex=vertex_3))
    graph.add_edge(Edge(starting_vertex=vertex_3, ending_vertex=vertex_1))

    # SCC #2
    graph.add_edge(Edge(starting_vertex=vertex_4, ending_vertex=vertex_5))
    graph.add_edge(Edge(starting_vertex=vertex_5, ending_vertex=vertex_6))
    graph.add_edge(Edge(starting_vertex=vertex_6, ending_vertex=vertex_4))

    # SCC #3
    graph.add_edge(Edge(starting_vertex=vertex_7, ending_vertex=vertex_8))
    graph.add_edge(Edge(starting_vertex=vertex_8, ending_vertex=vertex_9))
    graph.add_edge(Edge(starting_vertex=vertex_9, ending_vertex=vertex_7))
    
    return graph
