#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("small_flavor_matrix_graph_ingredient_node.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)




#Converting a dictionary of dictionaries to a graph
G = pickled_G

print(G.edges.data('shared_molecules', default=1))
print(G.number_of_edges())
print(G.number_of_nodes())

ingredient_nodes = nx.get_node_attributes(G, 'ingredient_node').keys()
molecule_nodes = nx.get_node_attributes(G, 'molecule_node').keys()

print('Shape node ids: {}'.format(ingredient_nodes))
print('Color node ids: {}'.format(molecule_nodese))

# #getting all the weights of each edge
# all_weights = []
# for (node1,node2,data) in G.edges(data=True):
#     all_weights.append(data['shared_molecules'])

# #getting the unique weights of all the edges
# unique_weights = list(set(all_weights))

# for weight in unique_weights:
#         #4 d. Form a filtered list with just the weight you want to draw
#         weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['shared_molecules']==weight]
#         width = weight*G.number_of_nodes()/sum(all_weights)
#         nx.draw_networkx_edges(G,pos=nx.spring_layout(G), edgelist=weighted_edges,width=width)
# # plt.axis('off')
# # plt.show() 


#Plotting the Graph 
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(G, ax=ax)
plt.show()