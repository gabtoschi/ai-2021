import networkx as nx
import matplotlib.pyplot as plt

class GraphPrinter:
    def __init__(self):
        self.G = nx.DiGraph(directed=True)
        self.options = {
            # 'node_color': 'blue',
            'node_size': 200,
            # 'width': 1,
            'arrowstyle': '-|>',
            'arrowsize': 18,
            # 'edge_color': 'r'
        }

    def print(self, edges):
        self.G.add_edges_from(edges)
        nx.draw_networkx(self.G, arrows=False, **self.options)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show()

    def printWay(self, edges, way, path_to_save=None):
        wayAux = []

        localOptions = {
            'node_color': '#005e615c',
            'node_size': 10,
            'font_color': '#18054f',
            'font_weight': 'bold',
            'arrowstyle': '-|>',
            'arrowsize': 5,
            'font_size': 0,
        }

        index = 1
        for v in way:
            wayAux.append((v, way[index]))
            if (index < len(way) - 1):
                index = index + 1

        for edge in edges:
            color = '#005e615c'
            width = 1
            alpha = 0.5
            if edge in wayAux:
                color = 'red'
                width = 1
                alpha = 1
            self.G.add_edge(edge[0], edge[1], color=color, width=width, alpha=alpha)

        colors = [self.G[u][v]['color'] for u,v in self.G.edges()]
        widths = [self.G[u][v]['width'] for u,v in self.G.edges()]

        nx.draw_networkx(self.G, edge_color=colors, arrows=True, width=widths, with_labels=False, pos=nx.kamada_kawai_layout(self.G), **localOptions)

        figManager = plt.get_current_fig_manager()
        # figManager.window.showMaximized()
        ppp = plt.plot()
        plt.tight_layout(rect=[0, 0, 1, 0.95])

        figure = plt.gcf()
        figure.set_size_inches(8, 6)

        if path_to_save:
            plt.savefig(path_to_save, bbox_inches='tight', dpi=300)
        else:
            plt.show()

        plt.clf()
