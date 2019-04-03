"""
Takes entire data, and then makes a graph based off of nodes of ingredients and molecules
"""
#Python Libraries for Mongos Database
import pymongo
from pymongo import MongoClient

#Python Library for Dataframe usage
import pandas as pd
import numpy as np
import random 
from collections import defaultdict

#Serializing to a file
import _pickle as pickle

#Libraries for Graph
import networkx as nx


#accessing mongoDB
client = MongoClient()
database = client['food_map']   # Database name (to connect to)
collections = database['flavor_molecules']

#Getting the dataset from MongoDB into Pandas
flavorDB_pandas = pd.DataFrame(list(collections.find()))
flavorDB_pandas = flavorDB_pandas[["_id", "ingredient", "catgeory", "molecules", "molecule_IDs"]]

#Making each list into a set
flavorDB_pandas["set_molecules"] = flavorDB_pandas["molecules"].apply(lambda row: set(row))
flavorDB_pandas["set_molecules_ID"] = flavorDB_pandas["molecule_IDs"].apply(lambda row: set(row))

#Creation of the Flavor Matrix
flavor_matrix_df = defaultdict(dict)

G=nx.Graph()

x = 0
#iterate through each row of flavorDB based on if index is in random sample
for index, row in flavorDB_pandas.iterrows():
    x += 1
    #set of the ingredient from the "rows"
    set1= row["set_molecules"]
    #name of the ingredient from the "rows" 
    ingredient_1 = row["ingredient"]
    
    print(ingredient_1)
    print(x) #to keep track of what's going on

    if True: # or len(set1) < 5: # To set if you want to consider all ingredients
        for molecule in set1:
            G.add_node(ingredient_1)
            G.node[ingredient_1]["ingredient_node"] = True
            G.add_node(molecule)
            G.node[molecule]["molecule_node"] = True
            G.add_edge(ingredient_1, molecule)

with open('molecule_full_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()

#Celebratory print statement
print("we did it!")