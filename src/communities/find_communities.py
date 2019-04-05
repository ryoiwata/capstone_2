#Python Library for Dataframe usage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Serializing to a file
import _pickle as pickle

#Libraries for Graph
import networkx as nx
from communities import find_communities_n, find_communities_modularity
from communities import find_communities_modularities

#etc. 
from collections import Counter

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./../../data/graph/molecule_subset_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

best_communities_set = find_communities_modularity(G)
print(len(best_communities_set))
print(best_communities_set)

comms, mods = find_communities_modularities(G)

plt.plot(list(range(1,len(mods)+1)), mods, ':o')
plt.xlabel('number of communities')
plt.ylabel('modularity')
plt.show()