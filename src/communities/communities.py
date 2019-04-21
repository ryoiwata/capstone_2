import networkx as nx
from collections import Counter
import _pickle as pickle
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def most_central_edge(G):
    centrality = nx.edge_betweenness_centrality(G, weight= "pmi")
    return max(centrality, key=centrality.get)

def heaviest(G):
    u, v, w = max(G.edges(data='weight'), key=itemgetter(2))
    return (u, v)

def girvan_newman_step(G):
    """Run one step of the Girvan-Newman community detection algorithm.
    Afterwards, the graph will have one more connected component.
    Parameters
    ----------
    G: networkx Graph object
    Returns
    -------
    None
    """
    init_ncomp = nx.number_connected_components(G)
    ncomp = init_ncomp
    x = 0
    while ncomp == init_ncomp:
        # bw = Counter(nx.edge_betweenness_centrality(G)) #girvan newman for just edge between centrality
        # a, b = bw.most_common(1)[0][0]
        # edge_to_cut = heaviest(G) # Girvan Newman for heaviest edge
        # a = edge_to_cut[0] 
        # b = edge_to_cut[1]
        bw = most_central_edge(G) 
        a, b = bw[0], bw[1]

        G.remove_edge(a, b)
        ncomp = nx.number_connected_components(G)
        x += 1
        print("Cut of Girvan Newman: ", x)


def find_communities_n(G, n):
    """Return communites of G after running Girvan-Newman algorithm n steps.
    Parameters
    ----------
    G: networkx Graph object
    n: int
    Returns
    -------
    list of lists
    """
    G1 = G.copy()
    for i in range(n):
        girvan_newman_step(G1)
    return list(nx.connected_components(G1))


def find_communities_modularity(G, max_iter=None):
    """Return communities with the maximum modularity from G.
    Run Girvan-Newman algorithm on G and find communities with max modularity.
    Parameters
    ----------
    G: networkx Graph object
    max_iter: int, (optional, default=None)
        Maximum number of iterations
    Returns
    -------
    list of lists of strings
        Strings are node names
    """
    degrees = G.degree()
    num_edges = G.number_of_edges()
    G1 = G.copy()
    best_modularity = -1.0
    best_comps = nx.connected_components(G1)
    i = 0
    while G1.number_of_edges() > 0:
        subgraphs = nx.connected_component_subgraphs(G1)
        modularity = get_modularity(subgraphs, degrees, num_edges)
        if modularity > best_modularity:
            best_modularity = modularity
            best_comps = list(nx.connected_components(G1))
        girvan_newman_step(G1)
        i += 1
        if max_iter and i >= max_iter:
            break
    return best_comps


def get_modularity(subgraphs, degrees, num_edges):
    """Return the value of the modularity for the graph G.
    Parameters
    ----------
    subgraphs: generator
        Graph broken in subgraphs
    degrees: dictionary
        Node: degree key-value pairs from original graph
    num_edges: float
        Number of edges in original graph
    Returns
    -------
    float
        Modularity value, between -0.5 and 1
    """
    mod = 0
    for g in subgraphs:
        for node1 in g:
            for node2 in g:
                mod += int(g.has_edge(node1, node2))
                mod -= degrees[node1] * degrees[node2] / (2. * num_edges)
    return mod / (2. * num_edges)

def find_communities_modularities(G, max_iter=None):
    """Return communities and modularities.
    Run Girvan-Newman algorithm on G and return communities & modularity at for each step.
    Parameters
    ----------
    G: networkx Graph object
    max_iter: int, (optional, default=None)
        Maximum number of iterations
    Returns
    -------
    partitions: list of partitions
        (each partition is a list of sets (communities))
        (each set contains node labels (strings))
    modularities: corresponding modularities for each partition
    """
    degrees = G.degree()
    num_edges = G.number_of_edges()
    G1 = G.copy()
    modularities = []
    partitions = []
    i = 0
    while G1.number_of_edges() > 0:
        subgraphs = nx.connected_component_subgraphs(G1)
        modularity = get_modularity(subgraphs, degrees, num_edges)
        modularities.append(modularity)
        partitions.append(list(nx.connected_components(G1)))
        girvan_newman_step(G1)
        i += 1
        if max_iter and i >= max_iter:
            break
    return partitions, modularities

# def find_communities_modularities(G, max_iter=None):
#     """Return communities and modularities.
#     Run Girvan-Newman algorithm on G and return communities & modularity at for each step.
#     Parameters
#     ----------
#     G: networkx Graph object
#     max_iter: int, (optional, default=None)
#         Maximum number of iterations
#     Returns
#     -------
#     partitions: list of partitions
#         (each partition is a list of sets (communities))
#         (each set contains node labels (strings))
#     modularities: corresponding modularities for each partition
#     """
#     degrees = G.degree()
#     num_edges = G.number_of_edges()
#     G1 = G.copy()
#     modularities = []
#     partitions = []
#     i = 0
#     my_bool = True
#     while nx.number_connected_components(G1) < 4:
#         if nx.number_connected_components(G1) == 2 and my_bool:
#             with open('./data/graph/community_girvan_newman.graph', 'wb') as file:
#                 file.write(pickle.dumps(G1))
#                 file.close()
#             my_bool = False    
#         i += 1
#         print("Iteration: ", i)
#         subgraphs = nx.connected_component_subgraphs(G1)
#         modularity = get_modularity(subgraphs, degrees, num_edges)
#         modularities.append(modularity)
#         partitions.append(list(nx.connected_components(G1)))
#         girvan_newman_step(G1)
#         if max_iter and i >= max_iter:
#             break
#     return partitions, modularities

if __name__ == '__main__':
    
    
    #Opening the pickled file
    pickle_in = open("./data/graph/recipe_graph.pickle", "rb")
    #Getting the dictionary from the pickle
    shared_molecule_graph = pickle.load(pickle_in)


    comms, mods = find_communities_modularities(shared_molecule_graph)
    plt.plot(list(range(1,len(mods)+1)), mods, ':o')
    plt.xlabel('number of communities')
    plt.ylabel('modularity')
    print("Optimal number of communities: {}".format(len(comms[np.argmax(mods)])))
    plt.savefig('girvan_newman_recipe_graph.png')

    with open('./data/partitions', 'wb') as file:
        file.write(pickle.dumps(comms))
        file.close()

    with open('./data/modularities', 'wb') as file:
        file.write(pickle.dumps(mods))
        file.close()
#   # Uncomment this once done
    # karateG = nx.karate_club_graph()
    # c = find_communities_modularity(karateG)
    # print("Optimal number of communities: {}".format(len(c)))
