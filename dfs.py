import graph as Graph
from graph_printer import GraphPrinter

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

test = Graph.KNNGraph(10, 5)
# test.print()
print('DFS =========', DFS(test, test.vertices()[0], test.vertices()[1]))
gPrinter = GraphPrinter()
gPrinter.printWay(test.edges(), DFS(test, test.vertices()[0], test.vertices()[1]), 'dirr/est.png')