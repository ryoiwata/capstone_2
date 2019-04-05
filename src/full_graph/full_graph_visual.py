#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("molecule_full_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

print("Number of edges: ", G.number_of_edges())
print("Number of nodes: ", G.number_of_nodes())

#returns a dictionary based on attributes
ingredient_node_attribute = nx.get_node_attributes(G, 'ingredient_node')
molecule_node_attribute = nx.get_node_attributes(G, 'molecule_node')

#list of ingredients
ingredient_list = []
for node, boolean in ingredient_node_attribute.items():    
    if boolean == True:
        ingredient_list.append(node)

#list of non ingredients
molecule_list = []
for node, boolean in molecule_node_attribute.items():   
    if boolean == True:
        molecule_list.append(node)

# Print statemenets to verify lists
# print('Ingredient nodes ids: {}'.format(ingredient_list))
# print('Molecule nodes ids: {}'.format(molecule_list))

# #Plotting the Graph 
# fig, ax = plt.subplots(1, 1, figsize=(8, 6))
# nx.draw_networkx(G, ax=ax)
# plt.show()