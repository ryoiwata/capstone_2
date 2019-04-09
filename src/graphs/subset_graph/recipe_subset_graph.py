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

#To get sample of pandas graph
recipe_puppy_pandas = recipe_puppy_pandas.sample(n= 2, random_state = 1)
num_recipes = len(recipe_puppy_pandas["recipe_name"])

#Initializing the Graph
G=nx.Graph()

#to keep track of which recipe we are on 
recipe_num = 0

#iterate through each recipe
for index, row in recipe_puppy_pandas.iterrows():
    recipe_num += 1
    print(row["recipe_name"])
    print("Recipe Progress: ", recipe_num / num_recipes)
    
    ingredient_list = row["recipe_ingredients"]
    
    # to keep track of the indexes
    x = 1
    
    #iterate through each ingredient of the recipe
    for ingredient_1 in ingredient_list:

        # print("first ingredient: ", ingredient_1)
        G.add_node(ingredient_1)
        G.node[ingredient_1]["ingredient_node"] = True
        G.node[ingredient_1]["molecule_node"] = False
        
        #make an edge to connect the two ingredients
        for ingredient_2 in ingredient_list[x:]:
            # print("second ingredient: ", ingredient_2)
            G.add_node(ingredient_2)
            G.node[ingredient_2]["ingredient_node"] = True
            G.node[ingredient_2]["molecule_node"] = False
            if G.get_edge_data(ingredient_1, ingredient_2) == None:
                G.add_edge(ingredient_1, ingredient_2, weight = 1)
            else:
                G[ingredient_1][ingredient_2]["weight"] += 1
        
        #change the index to match the new first ingredient
        x += 1
        
        #break if it's the last ingredient
        if x == len(ingredient_list):
            break


#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/graph/recipe_subset_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()
