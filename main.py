#!/usr/bin/env python3

from graph import Vertex
import util

def main():
    # scss: list[list[Vertex]] = util.first_graph().tarjan()
    # print(f"Graph 1 SCC count: {len(scss)}")
    # for scc in scss:
    #     show_scc(scc)
    
    scss_2 = util.second_graph().tarjan()
    print(f"Graph 2 SCC count: {len(scss_2)}")
    for scc in scss_2:
        show_scc(scc)

# Show SCC's vertices by their index..
def show_scc(scc: list[Vertex]) -> None:
    indices: list[int] = [v.index for v in scc]
    indices.sort()
    print(indices)

if __name__ == "__main__":
    main()
