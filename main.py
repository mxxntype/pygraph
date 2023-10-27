#!/usr/bin/env python3

from graph import Vertex, show_scc
from util import first_graph, second_graph

def main():
    scss_1: list[list[Vertex]] = first_graph().tarjan()
    print(f"Graph 1 SCC count: {len(scss_1)}")
    for scc in scss_1:
        show_scc(scc)
    
    # scss_2 = second_graph().tarjan()
    # print(f"Graph 2 SCC count: {len(scss_2)}")
    # for scc in scss_2:
    #     show_scc(scc)

if __name__ == "__main__":
    main()
