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

#Making a list of random numbers with a certain seed
random.seed(10)
random_samples_to_972 = random.sample(range(973), 50)
random_samples_to_972.sort()



G=nx.Graph()

#iterate through each row of flavorDB based on if index is in random sample
for index, row in flavorDB_pandas.iterrows():
    #to see if it is in the random sample
    if index in random_samples_to_972:
        #might incorporate this might not
        list_of_shared_molecules = []
        list_of_number_of_shared_molecules = []
        
        #set of the ingredient from the "rows"
        set1= row["set_molecules"]
        #name of the ingredient from the "rows" 
        ingredient_1 = row["ingredient"]
        
        if len(set1) < 5:
            for molecule in set1:
                # flavor_matrix_df[ingredient_1][molecule] = {'weight': 1}
                G.add_node(ingredient_1)
                G.node[ingredient_1]["ingredient_node"] = True
                G.add_node(molecule)
                G.node[molecule]["molecule_node"] = True
                G.add_edge(ingredient_1, molecule)



    #     #Going to replace this with a default dict
    #     """
    #     #starting a dictionary entry with a value of an empty dict
    #     flavor_matrix_df[ingredient_1] = {}  
    #     """

    #     #iterate through the "columns" of ingredients
    #     for index, row in flavorDB_pandas.iterrows():
    #         #to see if it is in the random sample
    #         if index in random_samples_to_972:
                
    #             #set of the ingredient from the "columns" of ingredients
    #             set2 = row["set_molecules"]
    #             #nome of the ingredient from the "columns" of ingredients
    #             ingredient_2 = row["ingredient"]
                
    #             #checking to see if ingredients are different
    #             if ingredient_1 != ingredient_2:
    #                 #The molecules that are shared between the two sets
    #                 shared_molecules = set1.intersection(set2)       
                    
    #                 #access the dictionary of a dictionary from 1st ingredient 
    #                 #set the value as the number of shared molecules
    #                 #Below code is for non networkx use    
    #                 # flavor_matrix_df[ingredient_1][ingredient_2] = len(shared_molecules)

    #                 #Below is for networkX use
    #                 #Only includes edges that have at least one shared molecule
    #                 if len(shared_molecules) > 0:
    #                     for 
    #                     flavor_matrix_df[ingredient_1][ingredient_2] = {'shared_molecules': len(shared_molecules)}       
                
                
    #             else: 
    #                 pass   
    #         else:
    #             pass
    # else:
    #     pass



with open('small_flavor_matrix_graph_ingredient_node.pickle', 'wb') as file:
    file.write(pickle.dumps(G))
    file.close()

#Celebratory print statement
print("we did it!")