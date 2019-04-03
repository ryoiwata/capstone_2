#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#Opening the pickled file
pickle_in = open("small_flavor_matrix_dict.pickle","rb")

#Getting the dictionary from the pickle
flavor_matrix_dict = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = nx.from_dict_of_dicts(flavor_matrix_dict)

