#!/usr/bin/env python3

from graph import Edge, Graph, Vertex

def main():
    graph = Graph()

    graph.add_vertex(
        vertex=Vertex(
            index=0,
        ),
        connected_vertices=[
            Vertex(index=1),
            Vertex(index=2),
            Vertex(index=3),
            Vertex(index=4),
        ]
    )

    graph.add_edge(
        edge=Edge(
            starting_vertex=Vertex(index=2),
            ending_vertex=Vertex(index=4),
        )
    )

    graph.edit_edge(
        old_edge=Edge(
            starting_vertex=Vertex(index=2),
            ending_vertex=Vertex(index=4),
        ),
        new_edge=Edge(
            starting_vertex=Vertex(index=4),
            ending_vertex=Vertex(index=5),
        )
    )

    graph.edit_vertex(
        old_vertex=Vertex(index=0),
        new_vertex=Vertex(index=6),
    )

    graph.print()

    graph.remove_vertex(
        vertex=Vertex(
            index=int(input(">> vertex.id: "))
        )
    )

    graph.print()
    print(graph.first(Vertex(index=6)))
    print(graph.next(Vertex(index=6), 4))
    print(graph.vertex(Vertex(index=6), 3))

if __name__ == "__main__":
    main()
