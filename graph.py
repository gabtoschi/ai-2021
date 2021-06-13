class Graph:
    def __init__(self):
        self.graphDict = {}

    def vertices(self):
        return list(self.graphDict.keys())

    def edges(self):
        edges = []

        for source in self.graphDict:
            for target in self.graphDict[source]:
                edges.append((source, target))

        return edges

    def addVertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

    def addEdge(self, source, target):
        if source in self.graphDict and target in self.graphDict:
            self.graphDict[source].append(target)

graph1 = Graph()

for i in range(4):
    graph1.addVertex(i)

graph1.addEdge(0, 1)
graph1.addEdge(0, 2)
graph1.addEdge(2, 1)
graph1.addEdge(2, 3)
graph1.addEdge(3, 2)

print(graph1.graphDict)
print(graph1.edges())
