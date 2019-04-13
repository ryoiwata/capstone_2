#Serializing to a file
import _pickle as pickle

#Python Library for Dataframe usage
import pandas as pd
#text processing
from collections import Counter
#for graph creation
import networkx as nx
from itertools import combinations, product

###Pandas Dataframe of Recipes with associated ingredients from Recipe Puppy API

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./data/pandas/cleaned_up_recipes_pandas.pickle","rb")
#Getting the dictionary from the pickle
recipe_puppy_pandas = pickle.load(pickle_in)


###Pandas Dataframe of ingredients with associated flavor molecules from FlavorDB

#Opening the pickled file
pickle_in = open("./data/pandas/flavorDB_pandas.pickle","rb")

#Getting the dictionary from the pickle
flavorDB_pandas = pickle.load(pickle_in)
#makes the ingredient database lowercase
flavorDB_pandas["ingredient"] = flavorDB_pandas["ingredient"].str.lower()

###Making a graph that will iterate through each recipe
###Then iterate through each ingredient
###Then iterate through each flavor molecule of the ingredient, making a node for the flavor molecule
###Get a count of each molecule
###And then make edges based off of the total number of times each molecules has appeared in the recipe 
### (i.e. L-arginine appears 2 times in the recipe, methanethiol appears 1 time in the recipe, then the edge will have a weight of 3 due to this recipe)
###Edge weights will continue to be added on with subsequent recipes


#Initializing the Graph
G=nx.Graph()

#to keep track of which recipe we are on 
recipe_num = 0

#iterate through each recipe
for index, row in recipe_puppy_pandas.iterrows():
    recipe_num += 1
    print("currently on: ", recipe_num/ len(recipe_puppy_pandas["recipe_name"]))

    ingredient_set = set(row["recipe_ingredients"])
    if len(ingredient_set) <= 1:
        continue 
    
    ingredient_combo = combinations(ingredient_set, 2)
    for ing_combo in ingredient_combo:
        molecules_1 = flavorDB_pandas.loc[flavorDB_pandas['ingredient'] == ing_combo[0], 'molecules'].iloc[0] 
        molecules_2 = flavorDB_pandas.loc[flavorDB_pandas['ingredient'] == ing_combo[1], 'molecules'].iloc[0] 

        for mol_combo in product(molecules_1, molecules_2):
            molecule_1 = mol_combo[0]
            molecule_2 = mol_combo[1]
            G.add_node(molecule_1)
            G.add_node(molecule_2)
            G.node[molecule_1]["ingredient_node"] = False
            G.node[molecule_1]["molecule_node"] = True
            G.node[molecule_2]["ingredient_node"] = False
            G.node[molecule_2]["molecule_node"] = True

            if G.get_edge_data(molecule_1, molecule_2) == None:
                G.add_edge(molecule_1, molecule_2, weight = 1)
            else:
                G[molecule_1][molecule_2]["weight"] += 1
            


#writes the pickle into the data file
#makes it so that needs to be called in src folder
with open('./data/graph/recipe_molecule_flavordb_puppy_graph.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()