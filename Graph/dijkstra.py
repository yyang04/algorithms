from typing import Dict, Tuple
from queue import PriorityQueue


def dijkstra(g: Dict[str, Dict[str, float]], start_point: str) -> Dict[str, float]:
    pq = PriorityQueue()
    pq.put((start_point, 0))
    visited = set()
    result = {}
    for neighbors in g.values():
        for neighbor in neighbors.keys():
            if neighbor not in result:
                result[neighbor] = float('inf')
    result[start_point] = 0.0

    while not pq.empty():
        p, d = pq.get()
        if p not in visited:
            visited.add(p)
            neighbors = g.get(p, {})
            for n, dist in neighbors.items():
                print(n, dist)
                pq.put((n, min(result[n], dist + d)))
                result.update({n: min(result[n], dist + d)})

    return result



