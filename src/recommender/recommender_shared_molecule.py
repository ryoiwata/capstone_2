"""
https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3
Look at 'Putting it all together section'
"""

#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#For random walk
import random 

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./../../data/graph/molecule_full_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G
# print(G.nodes())

#random walk algorithm
current_node = "Egg"
for num in range(10):
    number_of_edges = len(G[current_node])
    random_number = random.randint(1, number_of_edges)
    current_node = list(G[current_node])[random_number]
    print(current_node)



# print(G["Egg"])


print(G.number_of_edges())
print(G.number_of_nodes())


