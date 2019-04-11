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
from communities import *

#etc. 
from collections import Counter

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("../../data/graph/molecule_full_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

comms, mods = find_communities_modularities(G, 30)
plt.plot(list(range(1,len(mods)+1)), mods, ':o')
plt.xlabel('number of communities')
plt.ylabel('modularity')
plt.savefig('modularities_community_molecules_graph.png')
plt.show()