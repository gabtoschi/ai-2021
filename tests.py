import sys, time, random

from graph import KNNGraph
from dfs import DFS
from bfs import BFS
from bestfirst import bestFirst
from astar import aStar

EXECUTIONS = 5

args = sys.argv[1:]
if (len(args) < 2):
    print('Need arguments for v and k')
    exit()

algorithms = {
    # 'DFS': DFS,
    'BFS': BFS,
    'Best-First': bestFirst,
    'A*': aStar,
}

v = int(args[0])
k = int(args[1])
graph = KNNGraph(v, k)

verticesAmount = len(graph.vertices())
startNode = graph.vertices()[random.randrange(verticesAmount)]

endNode = startNode
while (startNode == endNode):
    endNode = graph.vertices()[random.randrange(verticesAmount)]

file = open('results/v' + str(v) + '-k' + str(k) + '.dat', 'w')

print('| Graph | V =', v, '| K =', k, '|', file = file)
print('| Start:', startNode, '| End:', endNode, '|', file = file)
print(file = file)

for algName in algorithms:
    executionTime = 0.0
    lastPath = None

    for exec in range(EXECUTIONS):
        start = time.time()
        lastPath = algorithms[algName](graph, startNode, endNode)
        end = time.time()

        executionTime = executionTime + (end - start)

    executionTime = executionTime / EXECUTIONS

    print('|', algName, '| Average Time:', executionTime, '|', file = file)
    print(lastPath, file = file)
    print(file = file)