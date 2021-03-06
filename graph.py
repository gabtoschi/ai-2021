import random, math
from graph_printer import GraphPrinter

def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def getPathByParents(parent, end):
    foundPath = []
    pathCurrent = end

    if end in parent:
        while pathCurrent != None:
            foundPath.append(pathCurrent)
            pathCurrent = parent[pathCurrent]

    foundPath.reverse()

    return foundPath

class Graph:
    def __init__(self):
        self.graphDict = {}
        self.gPrinter = GraphPrinter()

    def vertices(self):
        return list(self.graphDict.keys())

    def edges(self):
        edges = []

        for source in self.graphDict:
            for target in self.graphDict[source]:
                edges.append((source, target))

        return edges

    def neighbors(self, vertex):
        return self.graphDict[vertex]

    def addVertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

    def addEdge(self, source, target):
        if source in self.graphDict and target in self.graphDict:
            self.graphDict[source].append(target)

    def print(self):
        self.gPrinter.print(self.edges())

    def printWithPath(self, path, filename):
        self.gPrinter.printWay(self.edges(), path, filename)

class KNNGraph(Graph):
    def __init__(self, v, k):
        super().__init__()

        vertices = []

        while len(vertices) < v:
            vertex = (random.randint(0, v), random.randint(0, v))

            if vertex not in vertices:
                self.addVertex(vertex)
                vertices.append(vertex)

        for v in vertices:
            distances = []

            for v2 in vertices:
                if v != v2:
                    distances.append((v2, distance(v, v2)))

            distances.sort(key = lambda x: x[1])

            for i in range(k):
                self.addEdge(v, distances[i][0])

