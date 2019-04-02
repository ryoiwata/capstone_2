#Python Libraries for Mongos Database
import pymongo
from pymongo import MongoClient

#Python Library for Dataframe usage
import pandas as pd

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
flavor_matrix_df = {}

#iterate through each row of flavorDB
for index, row in flavorDB_pandas.iterrows():

    #might incorporate this might not
    list_of_shared_molecules = []
    list_of_number_of_shared_molecules = []
    
    #set of the ingredient from the "rows"
    set1= row["set_molecules"]
    #name of the ingredient from the "rows" 
    ingredient_1 = row["ingredient"]
    
    #starting a dictionary entry with a value of an empty dict
    flavor_matrix_df[ingredient_1] = {}  
    
    #iterate through the "columns" of ingredients
    for index, row in flavorDB_pandas.iterrows():
        
        #set of the ingredient from the "columns" of ingredients
        set2 = row["set_molecules"]
        #nome of the ingredient from the "columns" of ingredients
        ingredient_2 = row["ingredient"]
        
        #The molecules that are shared between the two sets
        shared_molecules = set1.intersection(set2)       
        
        #access the dictionary of a dictionary from 1st ingredient 
        #set the value as the number of shared molecules
        flavor_matrix_df[ingredient_1][ingredient_2] = len(shared_molecules)       

with open('flavor_matrix_dict.pickle', 'wb') as file:
    file.write(pickle.dumps(flavor_matrix_df))
    file.close()

#Celebratory print statement
print("we did it!")