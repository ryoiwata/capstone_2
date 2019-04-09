
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
sample_pd = ingredient_only_pd.sample(n= 50, random_state = 999)
# sample_pd = ingredient_only_pd.sample(n= 50, random_state = 10)


#Initializing Graph
G=nx.Graph()

#iterate through each row of flavorDB 
for index, row1 in sample_pd.iterrows():
    #ingredient name
    ingredient_1 = row1["ingredient"]
    #ingredient category
    category_1 = row1["category"]
    molecules_1 = row1["set_molecules"]
    if len(molecules_1) > 5:
        continue
    G.add_node(ingredient_1)
    G.node[ingredient_1]["ingredient_node"] = True
    G.node[ingredient_1]["molecule_node"] = False
    G.node[ingredient_1]["category"] = category_1

    for index, row2 in sample_pd.iterrows():
        ingredient_2 = row2["ingredient"]
        
        #checks to see if ingredients are different
        if ingredient_1 != ingredient_2:
            G.add_node(ingredient_1)
            category_2 = row2["category"]
            molecules_2 = row2["set_molecules"]
            if len(molecules_2) > 5:
                continue
            G.node[ingredient_1]["ingredient_node"] = True
            G.node[ingredient_1]["molecule_node"] = False
            G.node[ingredient_1]["category"] = category_2
            
            num_intersection = len(molecules_1.intersection(molecules_2))

            if num_intersection >= 1:
                G.add_edge(ingredient_1, ingredient_2, weight=num_intersection)

with open('./data/graph/ingredient_subset_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()