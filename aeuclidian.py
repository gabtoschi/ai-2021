import graph as Graph
from queue import PriorityQueue

def aEuclidian(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    partialCost = dict()

    parent[start] = None
    partialCost[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))
    visited.add(start)

    def heuristic(node):
        # 10 * Euclidian distance
        return 10 * Graph.distance(node, end)

    while not queue.empty():
        current = queue.get()[1]

        if current == end:
            break

        for v in graph.neighbors(current):
            newPartialCost = partialCost[current] + Graph.distance(current, v)

            if v not in visited or newPartialCost < partialCost[current]:
                partialCost[v] = newPartialCost
                queue.put((newPartialCost + heuristic(v), v))
                visited.add(v)
                parent[v] = current

    return parent
