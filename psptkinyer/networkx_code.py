# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:25:29 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""

import networkx as nx
#import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)
# (2, 3, {'weight': 3.1415})
G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
print(G.number_of_nodes())
print(G.number_of_edges())



H = nx.DiGraph(G)  # create a DiGraph using the connections from G
list(H.edges())
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)  # create a graph from an edge list
print(list(H.edges()))
adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
G = nx.petersen_graph()
#subax1 = plt.subplot(121)
nx.draw_networkx(G, with_labels=True, font_weight='bold')



#subax2 = plt.subplot(122)
#nx.draw_networkx(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),])

H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from(H.edges)
# (2, 3, {'weight': 3.1415})
G.clear()

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')
print(G.number_of_nodes())
print(G.number_of_edges())

DG = nx.DiGraph()
DG.add_edge(2, 1)   # adds the nodes in order 2, 1
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)
assert list(DG.successors(2)) == [1, 4]
assert list(DG.edges) == [(2, 1), (2, 4), (1, 3), (1, 2)]
#The order of adjacency reporting (e.g., G.adj, G.successors, G.predecessors) 
##is the order of edge addition. However, the order of G.edges 
#is the order of the adjacencies which includes both the order of the nodes
# and each node’s adjacencies. See example below:

print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))
print(G.degree[1])
print(G.edges([2, 'm']))
#EdgeDataView([(2, 1), ('m', 3)])
print(G.degree([2, 3]))
G.remove_node(2)
#print(G.nodes("spam"))

G.remove_nodes_from("spam")
#print(G.nodes("spam"))
print(list(G.nodes))


G.add_edge(1, 2)
H = nx.DiGraph(G)  # create a DiGraph using the connections from G
list(H.edges())
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)  # create a graph from an edge list
print(list(H.edges()))
adjacency_dict = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
H = nx.Graph(adjacency_dict)  # create a Graph dict mapping nodes to nbrs
print(list(H.edges()))
    
G = nx.Graph([(1, 2, {"color": "yellow"})])

#G.add_edge(1, 3)
#G[1][3]['color'] = "blue"
#G.edges[1, 2]['color'] = "red"
#G.edges[1, 2]
FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, nbrs in FG.adj.items():
   for nbr, eattr in nbrs.items():
       wt = eattr['weight']
       if wt < 0.5: print(f"({n}, {nbr}, {wt:.3})")

for (u, v, wt) in FG.edges.data('weight'):
    if wt < 0.5:
        print(f"({u}, {v}, {wt:.3})")
G = nx.Graph(day="Friday")
G.graph
#{'day': 'Friday'}
G.graph['day'] = "Monday"

G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.nodes[1]
#G.nodes[1]['room'] 
G.nodes.data()

G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edges[3, 4]['weight'] = 4.2

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
DG.out_degree(1, weight='weight')
DG.degree(1, weight='weight')
print(list(DG.successors(1)))
print(list(DG.neighbors(1)))
H = nx.Graph(G)  # create an undirected graph H from a directed graph G
nx.draw(G, with_labels=True, font_weight='bold')
