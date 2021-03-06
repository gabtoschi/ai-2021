import graph as Graph
from queue import PriorityQueue

def bestFirst(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    parent[start] = None

    queue = PriorityQueue()
    queue.put((0, start))
    visited.add(start)

    while not queue.empty():
        current = queue.get()[1]

        if current == end:
            break

        for v in graph.neighbors(current):
            if v not in visited:
                queue.put((Graph.distance(current, v), v))
                visited.add(v)
                parent[v] = current

    return parent
