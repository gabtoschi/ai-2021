from aeuclidian import aEuclidian
import sys, time, random
from typing import DefaultDict

from graph import KNNGraph, getPathByParents
from dfs import DFSIterative
from bfs import BFS
from bestfirst import bestFirst
from astar import aStar
from amanhattan import aManhattan

EXECUTIONS = 5

args = sys.argv[1:]
if (len(args) < 2):
    print('Need arguments for v and k')
    exit()

algorithms = {
    'DFS': DFSIterative,
    'BFS': BFS,
    'Best-First': bestFirst,
    'A*': aStar,
    'A (Manhattan)': aManhattan,
    'A (10 * Euclidian)': aEuclidian,
}

v = int(args[0])
k = int(args[1])
graph = KNNGraph(v, k)

verticesAmount = len(graph.vertices())
startNode = graph.vertices()[random.randrange(verticesAmount)]

endNode = startNode
while (startNode == endNode):
    endNode = graph.vertices()[random.randrange(verticesAmount)]

filenameBase = 'results/v' + str(v) + '-k' + str(k)
file = open(filenameBase + '.dat', 'w')

print('| Graph | V =', v, '| K =', k, '|', file = file)
print('| Start:', startNode, '| End:', endNode, '|', file = file)
print(file = file)

for algName in algorithms:
    executionTime = 0.0
    lastParent = None

    print('Start:', algName, 'v =', v, 'k =', k)

    for exec in range(EXECUTIONS):
        start = time.time()
        lastParent = algorithms[algName](graph, startNode, endNode)
        end = time.time()

        executionTime = executionTime + (end - start)

    executionTime = executionTime / EXECUTIONS

    path = getPathByParents(lastParent, endNode)
    print(path)

    print('|', algName, '| Average Time:', executionTime, '| Path Length:', len(path), file = file)
    print(path, file = file)
    print(file = file)

    graph.printWithPath(path, filenameBase + '-' + algName + '.png')

    print('End:', algName, 'v =', v, '| k =', k)
