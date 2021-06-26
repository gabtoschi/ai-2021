import graph as Graph

def DFS(graph: Graph.Graph, start, end):
    visited = set()

    parent = dict()
    parent[start] = None

    def DFSRec(graph: Graph.Graph, current):
        visited.add(current)

        for v in graph.neighbors(current):
            if v not in visited:
                parent[v] = current
                DFSRec(graph, v)

    DFSRec(graph, start)

    foundPath = []
    pathCurrent = end

    if end in parent:
        while pathCurrent != None:
            foundPath.append(pathCurrent)
            pathCurrent = parent[pathCurrent]

    foundPath.reverse()

    return foundPath

def DFSIterative(graph: Graph.Graph, start, end):
    visited = set()
    visited.add(start)

    parent = dict()
    parent[start] = None

    stack = [start]

    while stack:
        current = stack.pop()

        if current == end:
            break

        for v in graph.neighbors(current):
            if v not in visited:
                stack.append(v)
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
