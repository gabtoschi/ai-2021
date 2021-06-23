import networkx as nx
import matplotlib.pyplot as plt

class GraphPrinter:
    def __init__(self):
        self.G = nx.DiGraph(directed=True)
        self.options = {
            'node_color': 'blue',
            'node_size': 200,
            'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 18
        }

    def print(self, edges):
        edgesExtracted = []

        # ((6, 8), (8, 6))
        for item in edges:
            edgesExtracted.append(item[0])
            edgesExtracted.append(item[1])

        self.G.add_edges_from(edgesExtracted)
        nx.draw_networkx(self.G, arrows=True, **self.options)
        plt.show()
