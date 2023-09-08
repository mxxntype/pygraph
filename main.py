#!/usr/bin/env python3

from graph import Edge, Graph, Vertex

def main():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.print()
    pass

if __name__ == "__main__":
    main()
