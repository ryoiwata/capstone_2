#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("molecule_subset_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

print(G.edges.data('shared_molecules', default=1))
print(G.number_of_edges())
print(G.number_of_nodes())

ingredient_nodes = nx.get_node_attributes(G, 'ingredient_node').keys()
molecule_nodes = nx.get_node_attributes(G, 'molecule_node').keys()

print('Ingredient nodes ids: {}'.format(ingredient_nodes))
print('Molecule nodes ids: {}'.format(molecule_nodes))

#Plotting the Graph 
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(G, ax=ax)
plt.show()