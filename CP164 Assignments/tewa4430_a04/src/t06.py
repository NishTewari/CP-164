'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2020-02-07"
-----------------------------------------------

'''
# Imports

from Graph import Edge, Graph
from functions import prims

data = (
    (['A', 'B'], 2), (['A', 'C'], 3), (['A', 'D'], 7), (['B', 'C'], 6),
    (['B', 'G'], 4), (['C', 'E'], 1), (['C', 'F'], 8), (['D', 'E'], 5),
    (['E', 'F'], 4), (['F', 'G'], 2)
)

print(data)

edges = []

for d in data:
    edges.append(Edge(d[0], d[1]))

g = Graph(edges)
edges, total = prims(g, "A")

for k in edges:
    print(k)
print("Total Distance: {}".format(total))
