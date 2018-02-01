# Felix Nunez
# References: 
# https://www.tutorialspoint.com/python/index.htm
# https://networkx.github.io/documentation/latest/index.html
# http://www.mhenderson.net/graph-drawing/2014/05/02/networkx-01.html

import matplotlib.pyplot as plt
import networkx as nx

options = {
    'with_labels': False,
    'node_size': 20,
    'linewidths': .5,
    'width': .1,
    'cmap': 'plt.cm.plasma',
}
Sent = input("Which Graph would you like to use? For Barabasi-Albert press 1, \
 for Watts-Strogatz press 2, for Random Graph press 3, for Regular Graph press 4\n")
if int(Sent) == 1:
    N = input("How many Nodes are there?\n")
    M = input("How many edges are there?\n")
    BA = nx.barabasi_albert_graph(int(N), int(M), seed=None)
    A = nx.adjacency_matrix(BA)  
    nx.draw(BA, **options)
    plt.show(block=True)
elif int(Sent) == 2:
    N = input("How many Nodes are there?\n")
    K = input("How many Nodes are connected in a ring topology?\n")
    P = input("What's the probability of rewiring each edge\n")
    WS = nx.watts_strogatz_graph(int(N), int(K), float(P), seed=None)
    A = nx.adjacency_matrix(WS)
    nx.draw_circular(WS, **options)
    plt.show(block=True)
elif int(Sent) == 3:
    N = input("How many Nodes are there?\n")
    M = input("How many edges are there?\n")
    Rando = nx.gnm_random_graph(int(N), int(M), seed=None, directed=False)
    A = nx.adjacency_matrix(Rando)
    nx.draw(Rando, **options)
    plt.show(block=True)
elif int(Sent) == 4:
    D = input("What's the degree of each Node?\n")
    N = input("How many Nodes are there?\n")
    Reg = nx.random_regular_graph(int(D), int(N), seed=None)
    A = nx.adjacency_matrix(Reg)
    nx.draw(Reg, **options)
    plt.show(block=True)
else:
    print("Error: Graph not chosen\n")
