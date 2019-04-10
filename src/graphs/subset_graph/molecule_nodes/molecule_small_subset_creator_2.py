
"""
Takes entire data, and then makes a graph based off of nodes of ingredients and molecules
"""
#Python Library for Dataframe usage
import pandas as pd
import numpy as np

#Serializing to a file
import _pickle as pickle

#Libraries for Graph
import networkx as nx
import random 

#PandaDF of ingredients and their associated flavor molecules (with ingredients that are not cooked and have recipes)
#Opening the pickled file
pickle_in = open("./data/ingredients/ingredient_only_pd.pickle", "rb")

#Getting the dictionary from the pickle
ingredient_only_pd = pickle.load(pickle_in)
sample_pd = ingredient_only_pd.sample(n= 5, random_state = 30)

#Initializing Graph
G=nx.Graph()

#iterate through each row of flavorDB 
for index, row1 in sample_pd.iterrows():
    #ingredient name
    ingredient_1 = row1["ingredient"]
    #ingredient category
    category = row1["category"]
    molecules = row1["set_molecules"]

    G.add_node(ingredient_1)
    G.node[ingredient_1]["ingredient_node"] = True
    G.node[ingredient_1]["molecule_node"] = False
    G.node[ingredient_1]["category"] = category

    for molecule in molecules:
        G.add_node(molecule)
        G.node[molecule]["molecule_node"] = True
        G.node[molecule]["ingredient_node"] = False
        G.add_edge(ingredient_1, molecule)

with open('./data/graph/molecule_subset_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()