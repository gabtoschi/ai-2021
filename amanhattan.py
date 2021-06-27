import graph as Graph
from queue import PriorityQueue

def aManhattan(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    partialCost = dict()

    parent[start] = None
    partialCost[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))
    visited.add(start)

    def heuristic(node):
        # Manhattan distance
        return abs(node[0] - end[0]) + abs(node[1] - end[1])

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
