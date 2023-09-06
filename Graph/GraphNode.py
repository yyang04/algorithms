
from graphviz import Digraph
from typing import Dict, Optional, Set, Tuple
from dijkstra import dijkstra

GraphA = """
v1:v2_2_v4_1
v2:v5_10_v4_3
v3:v1_4_v6_5
v4:v3_2_v5_2_v7_4_v6_8
v5:v7_1
v7:v6_1
"""


def strToGraph(s: str) -> Dict[str, Dict[str, float]]:
    result = {}
    for line in s.strip().split("\n"):
        neighborsDict = {}
        src_node = line.split(":")[0]
        neighbors = line.split(":")[1].split("_")
        for i in range(len(neighbors) // 2):
            neighborsDict[neighbors[2 * i]] = float(neighbors[2 * i + 1])
        result[src_node] = neighborsDict
    return result


def plotGraph(g: Dict[str, Dict[str, float]], name: str, path: str = None, pathSet: Optional[Set[Tuple[str, str]]] = None) -> None:
    dot = Digraph()
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='circle', color='lightblue2', style='filled')
    if path:
        pathSet = set()
        pathArr = path.split(',')
        for i in range(len(pathArr)-1):
            pathSet.add((pathArr[i], pathArr[i+1]))

    for src, neighbors in g.items():
        for dst, weight in neighbors.items():
            color = 'red' if pathSet and (src, dst) in pathSet else None
            dot.edge(src, dst, label=str(weight), color=color)
    dot.render(f'{name}.gv', view=True)


if __name__ == '__main__':
    # plotGraph(strToGraph(GraphA), 'GraphA', path='v3,v1,v4,v6')
    result = dijkstra(strToGraph(GraphA), 'v3')
    print(result)

