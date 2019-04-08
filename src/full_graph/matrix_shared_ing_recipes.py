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


#accessing mongoDB for flavor molecules
client = MongoClient()
database = client['food_map']   # Database name (to connect to)
collections_molecule = database['flavor_molecules']
collections_recipe = database['recipes']

#Getting the dataset from MongoDB into Pandas for recipes
recipe_puppy_pandas = pd.DataFrame(list(collections_recipe.find()))
#dropping duplicates
recipe_puppy_pandas = recipe_puppy_pandas.drop_duplicates(subset= "recipe_name", keep="last")

all_ingredient_list = []

#iterate through each recipe
for index, row in recipe_puppy_pandas.iterrows():
    ingredient_list = row["recipe_ingredients"]
    
    # to keep track of the indexes
    x = 1

    #iterate through each ingredient of the recipe
    for ingredient_1 in ingredient_list:
        print("first ingredient: ", ingredient_1)
        for ingredient_2 in ingredient_list[x:]:
            print("second ingredient: ", ingredient_2)
        x += 1
        if x == len(ingredient_list):
            break

    
    # print(ingredient_list)
    break




"""
#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('recipe_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()
"""