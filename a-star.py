import graph as Graph
from queue import PriorityQueue

def aStar(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    partialCost = dict()

    parent[start] = None
    partialCost[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))
    visited.add(start)

    def heuristic(node):
        return Graph.distance(node, end)

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

    foundPath = []
    pathCurrent = end

    if end in parent:
        while pathCurrent != None:
            foundPath.append(pathCurrent)
            pathCurrent = parent[pathCurrent]

    foundPath.reverse()

    return foundPath

test = Graph.KNNGraph(800, 5)
print('A* =========', aStar(test, test.vertices()[0], test.vertices()[1]))