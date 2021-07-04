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

    return parent

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

    return parent

# test = Graph.KNNGraph(10, 5)
# test.print()
# print('DFS =========', DFS(test, test.vertices()[0], test.vertices()[1]))
# gPrinter = GraphPrinter()
# gPrinter.printWay(test.edges(), DFS(test, test.vertices()[0], test.vertices()[1]), 'dirr/est.png')

