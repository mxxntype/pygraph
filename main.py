#!/usr/bin/env python3

from graph import Edge, Graph, Vertex

def main():
    graph = Graph()

    v1 = Vertex(index=1)
    v2 = Vertex(index=2)
    v3 = Vertex(index=3)
    v4 = Vertex(index=4)
    v5 = Vertex(index=5)
    v6 = Vertex(index=6)

    graph.add_edge(Edge(starting_vertex=v1, ending_vertex=v2))
    graph.add_edge(Edge(starting_vertex=v2, ending_vertex=v3))
    graph.add_edge(Edge(starting_vertex=v3, ending_vertex=v1))

    graph.add_edge(Edge(starting_vertex=v4, ending_vertex=v5))
    graph.add_edge(Edge(starting_vertex=v5, ending_vertex=v6))
    graph.add_edge(Edge(starting_vertex=v6, ending_vertex=v4))

    # graph.print()
    scss: list[list[Vertex]] = graph.tarjan()
    print(f"SCC count: {len(scss)}")
    for scc in scss:
        print(f"SCC: {scc}")

if __name__ == "__main__":
    main()
