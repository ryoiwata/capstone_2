#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("./data/graph/molecule_subset_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

print("Number of edges: ", G.number_of_edges())
print("Number of nodes: ", G.number_of_nodes())


ingredient_nodes = nx.get_node_attributes(G, 'ingredient_node').keys()
molecule_nodes = nx.get_node_attributes(G, 'molecule_node').keys()

print("Number of ingredients: ", len(ingredient_nodes))
print("Number of molecules: ", len(molecule_nodes))