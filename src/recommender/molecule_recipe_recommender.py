#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#For random walk
import random 
from collections import Counter
import numpy as np
import operator


#Opening the pickled file
pickle_in = open("./data/ingredients/ingredient_only_pd.pickle","rb")
#Getting the graph from the pickle
ingredient_only_pd = pickle.load(pickle_in)
ingredient_only_pd = ingredient_only_pd.drop_duplicates(subset='ingredient', keep="last")

#Opening the pickled file
pickle_in = open("./data/graph/recipe_molecule_flavordb_puppy_graph.pickle","rb")
#Getting the graph from the pickle
recipe_molecule_graph = pickle.load(pickle_in)

def recipe_molecule_recommender(ingredient_1):
    scores = {}
    molecule_list_1 = ingredient_only_pd[ingredient_only_pd["ingredient"] == ingredient_1].molecules.item()
    
    #iterate through each new ingredient
    for ingredient_2 in ingredient_only_pd["ingredient"]:
        
        score = 0
        print("ingredient: ", ingredient_2)
        molecule_list_2 = ingredient_only_pd[ingredient_only_pd["ingredient"] == ingredient_2].molecules.item()
        for molecule_1 in molecule_list_1: 
            for molecule_2 in molecule_list_2:
                try:
                    score += recipe_molecule_graph[molecule_1][molecule_2]['weight']
                except:
                    pass
        score /= len(molecule_list_2) ** 0.5
        scores[ingredient_2] = score
        print(scores[ingredient_2])
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1),  reverse=True)
    print(sorted_scores)
        
    

if __name__ == "__main__":
    ingredient_1 = "parsley"
    print(recipe_molecule_recommender(ingredient_1))