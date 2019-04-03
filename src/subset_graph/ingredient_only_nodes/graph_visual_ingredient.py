#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("ingredient_subset_dict.pickle","rb")

#Getting the dictionary from the pickle
flavor_matrix_dict = pickle.load(pickle_in)

print(flavor_matrix_dict)



#Converting a dictionary of dictionaries to a graph
G = nx.from_dict_of_dicts(flavor_matrix_dict)

print(G.edges.data('shared_molecules', default=1))
print(G.number_of_edges())
print(G.number_of_nodes())

#Plotting the Graph 
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(G, ax=ax)
plt.show()