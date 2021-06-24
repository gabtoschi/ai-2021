import graph as Graph

def BFS(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    parent[start] = None

    queue = []
    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.pop(0)

        if current == end:
            break

        for v in graph.neighbors(current):
            if v not in visited:
                queue.append(v)
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

# test = Graph.KNNGraph(800, 5)
# print('BFS =========', BFS(test, test.vertices()[0], test.vertices()[1]))