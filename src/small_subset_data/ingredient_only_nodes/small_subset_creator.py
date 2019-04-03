"""
Takes a small subset of the data and turns it into a dictionary so that it can be used by NetworkX
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
random.seed(30)
random_samples_to_972 = random.sample(range(973), 20)
random_samples_to_972.sort()

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

        #iterate through the "columns" of ingredients
        for index, row in flavorDB_pandas.iterrows():
            #to see if it is in the random sample
            if index in random_samples_to_972:
                
                #set of the ingredient from the "columns" of ingredients
                set2 = row["set_molecules"]
                #nome of the ingredient from the "columns" of ingredients
                ingredient_2 = row["ingredient"]
                
                #checking to see if ingredients are different
                if ingredient_1 != ingredient_2:
                    #The molecules that are shared between the two sets
                    shared_molecules = set1.intersection(set2)       
                    
                    #access the dictionary of a dictionary from 1st ingredient 
                    #set the value as the number of shared molecules
                    #Below code is for non networkx use    
                    # flavor_matrix_df[ingredient_1][ingredient_2] = len(shared_molecules)

                    #Below is for networkX use
                    #Only includes edges that have at least one shared molecule
                    if len(shared_molecules) > 0:
                        flavor_matrix_df[ingredient_1][ingredient_2] = {'shared_molecules': len(shared_molecules)}       
                
#put it into a pickle
with open('small_flavor_matrix_dict.pickle', 'wb') as file:
    file.write(pickle.dumps(flavor_matrix_df))
    file.close()

#Celebratory print statement
print("we did it!")