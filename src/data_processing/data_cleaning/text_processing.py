#Python Library for Dataframe usage
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import numpy as np

#Serializing to a file
import _pickle as pickle

#PandaDF of recipes and associated ingredients
#Opening the pickled file
pickle_in = open("./data/pandas/recipe_puppy_pandas.pickle", "rb")

#Getting the dictionary from the pickle
recipe_df = pickle.load(pickle_in)

print(recipe_df.head())