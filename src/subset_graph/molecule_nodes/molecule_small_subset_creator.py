"""
Takes a small subset of the data, and then makes a graph based off of nodes of ingredients and molecules
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

#Lists of ingredients to keep from redundant ingredient cleaner notebook
keep_these_list = ["Animal Product", "Beverage Caffeinated", "Dairy", "Berry", "Seafood", "Fish", "Fruit", "Fruit Citrus", "Fruit Essence", "Fungus", "Herb", "Meat", "Nut", "Seed", "Legume", "Plant Derivative", "Spice", "Vegetable", "Cabbage", "Vegetable Root", "Vegetable Fruit", "Gourd",  "Vegetable Stem", "Vegetable Tuber", "Additive"]
consider_this_list = ["Beverage Alcoholic", "Cereal", "Maize", "Essential Oil", "Flower", "Fruit-Berry", "Plant","Additive"]
list_to_use = keep_these_list + consider_this_list

flavorDB_pandas = flavorDB_pandas[flavorDB_pandas["catgeory"].isin(list_to_use)]

#Making a list of random numbers with a certain seed
random.seed(10)
random_samples_to_812 = random.sample(range(812), 100)
random_samples_to_812.sort()

G=nx.Graph()

#iterate through each row of flavorDB based on if index is in random sample
for index, row in flavorDB_pandas.iterrows():
    #to see if it is in the random sample
    if index in random_samples_to_812:
        #might incorporate this might not
        list_of_shared_molecules = []
        list_of_number_of_shared_molecules = []
        
        #set of the ingredient from the "rows"
        set1= row["set_molecules"]
        #name of the ingredient from the "rows" 
        ingredient_1 = row["ingredient"]
        
        if True: #Can change the nodes you decide to have, such as: len(set1) < 5:
            for molecule in set1:
                # flavor_matrix_df[ingredient_1][molecule] = {'weight': 1}
                G.add_node(ingredient_1)
                G.node[ingredient_1]["ingredient_node"] = True
                G.add_node(molecule)
                G.node[molecule]["molecule_node"] = True
                G.add_edge(ingredient_1, molecule)

with open('molecule_subset_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()

#Celebratory print statement
print("we did it!")