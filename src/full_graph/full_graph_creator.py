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

#Lists of ingredients to keep from redundant ingredient cleaner notebook
keep_these_list = ["Animal Product", "Beverage Caffeinated", "Dairy", "Berry", "Seafood", "Fish", "Fruit", "Fruit Citrus", "Fruit Essence", "Fungus", "Herb", "Meat", "Nut", "Seed", "Legume", "Plant Derivative", "Spice", "Vegetable", "Cabbage", "Vegetable Root", "Vegetable Fruit", "Gourd",  "Vegetable Stem", "Vegetable Tuber", "Additive"]
consider_this_list = ["Beverage Alcoholic", "Cereal", "Maize", "Essential Oil", "Flower", "Fruit-Berry", "Plant","Additive"]
list_to_use = keep_these_list + consider_this_list

flavorDB_pandas = flavorDB_pandas[flavorDB_pandas["catgeory"].isin(list_to_use)]

#Importing a set that has all the ingredients with recipes
#Opening the pickled file
pickle_in = open("./data/ingredients_with_recipes.pickle","rb")
#Getting the dictionary from the pickle
set_of_ing_with_recipe = pickle.load(pickle_in)




G=nx.Graph()

x = 0
#iterate through each row of flavorDB based on if index is in random sample
for index, row in flavorDB_pandas.iterrows():
    x += 1
    #set of the ingredient from the "rows"
    set1= row["set_molecules"]
    #name of the ingredient from the "rows" 
    ingredient_1 = row["ingredient"]
    
    if ingredient_1.lower() in set_of_ing_with_recipe : #to filter out ingredients that only have recipes from Puppy Recipe API 
        print(ingredient_1)
        print(x) #to keep track of what's going on
        for molecule in set1:
            G.add_node(ingredient_1)
            G.node[ingredient_1]["ingredient_node"] = True
            G.node[ingredient_1]["molecule_node"] = False
            G.add_node(molecule)
            G.node[molecule]["molecule_node"] = True
            G.node[molecule]["ingredient_node"] = False
            G.add_edge(ingredient_1, molecule)

#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/molecule_full_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()

list_of_ingredients = list(flavorDB_pandas["ingredient"])
#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/ingredient_full_list.pickle', 'wb') as file:
    file.write(pickle.dumps(list_of_ingredients))
    file.close()

#Celebratory print statement
print("we did it!")

