# Felix Nunez
# References: 
# https://www.tutorialspoint.com/python/index.htm
# https://networkx.github.io/documentation/latest/index.html
# http://www.mhenderson.net/graph-drawing/2014/05/02/networkx-01.html
# https://media.readthedocs.org/pdf/networkx/latest/networkx.pdf

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import json
from networkx.readwrite import json_graph


Sent = input("Which Graph would you like to use? For Barabasi-Albert press 1, \
 for Watts-Strogatz press 2, for Random Graph press 3, for Regular Graph press 4\n")
if int(Sent) == 1:
    N = input("How many Nodes are there?\n")
    M = input("How many edges are there?\n")
    BA = nx.barabasi_albert_graph(int(N), int(M), seed=None)
    data = json_graph.adjacency_data(BA, attrs={'id':'Node', 'key': 'Edges'})
    degrees = BA.degree()
    nodes = BA.nodes()
    nodeclr = np.asarray([degrees[n] for n in nodes])
    options = {
    'with_labels': False,
    'node_size': nodeclr + 20,
    'node_color': nodeclr,
    'cmap': 'gist_heat_r',
    'linewidths': .5,
    'width': .1,
    }
    nx.draw(BA, **options)
    plt.title("Barabasi-Albert Graph")
    plt.show(block=True)
elif int(Sent) == 2:
    N = input("How many Nodes are there?\n")
    K = input("How many Nodes are connected in a ring topology?\n")
    P = input("What's the probability of rewiring each edge?\n")
    WS = nx.watts_strogatz_graph(int(N), int(K), float(P), seed=None)
    data = json_graph.adjacency_data(WS, attrs={'id':'Node', 'key': 'Edges'})
    degrees = WS.degree()
    nodes = WS.nodes()
    nodeclr = np.asarray([degrees[n] for n in nodes])
    options = {
    'with_labels': False,
    'node_size': nodeclr + 20,
    'node_color': nodeclr,
    'cmap': 'gist_heat_r',
    'linewidths': .5,
    'width': .1,
    }
    nx.draw_circular(WS, **options)
    plt.title("Watts-Strogatz Graph")
    plt.show(block=True)
elif int(Sent) == 3:
    N = input("How many Nodes are there?\n")
    M = input("How many edges are there?\n")
    Rando = nx.gnm_random_graph(int(N), int(M), seed=None, directed=False)
    data = json_graph.adjacency_data(Rando, attrs={'id':'Node', 'key': 'Edges'})
    degrees = Rando.degree()
    nodes = Rando.nodes()
    nodeclr = np.asarray([degrees[n] for n in nodes])
    options = {
    'with_labels': False,
    'node_size': nodeclr + 20,
    'node_color': nodeclr,
    'cmap': 'gist_heat_r',
    'linewidths': .5,
    'width': .1,
    }
    nx.draw(Rando, **options)
    plt.title("Random Graph")
    plt.show(block=True)
elif int(Sent) == 4:
    D = input("What's the degree of each Node?\n")
    N = input("How many Nodes are there?\n")
    Reg = nx.random_regular_graph(int(D), int(N), seed=None)
    data = json_graph.adjacency_data(Reg, attrs={'id':'Node', 'key': 'Edges'})
    degrees = Reg.degree()
    nodes = Reg.nodes()
    nodeclr = np.asarray([degrees[n] for n in nodes])
    options = {
    'with_labels': False,
    'node_size': nodeclr + 20,
    'node_color': nodeclr,
    'cmap': 'gist_heat_r',
    'linewidths': .5,
    'width': .1,
    }
    nx.draw(Reg, **options)
    plt.title("Regular Graph")
    plt.show(block=True)
else:
    print("Error: Graph not chosen\n")

with open('Graph_data.json', 'w') as outfile:
    json.dump(data, outfile)
