#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#For random walk
import random 
from collections import Counter
import numpy as np
from itertools import combinations 
import operator




def random_recipe_recommender(recipe_graph):
    result = {}
    list_of_nodes = recipe_graph.nodes()
    num_ing_per_recipe = int(input("How many ingredients in your recipe: "))

    all_recipe_comb = list(combinations(list_of_nodes, num_ing_per_recipe))
    for recipe in all_recipe_comb:
        key = tuple(recipe)
        result[key] = 0
        ingredient_pairs = list(combinations(recipe, 2))
        for pair in ingredient_pairs:
            score = 0
            first_ingredient = pair[0]
            second_ingredient = pair[1]
            edge_data = recipe_graph.get_edge_data(first_ingredient,second_ingredient)
            if edge_data != None:
                score = recipe_graph[first_ingredient][second_ingredient]['weight']
            else:
                pass
            result[key] += score
        
        # for ingredient_1 in key:
        #     print(recipe_graph[ingredient_1])
        #     break
    result = sorted(result.items(), key=operator.itemgetter(1))

    return result



if __name__ == "__main__":
    #Opening the pickled file
    #Needs to be opened in the recommender folder
    pickle_in = open("./data/graph/recipe_graph.pickle","rb")

    #Getting the dictionary from the pickle
    pickled_G = pickle.load(pickle_in)

    #Converting a dictionary of dictionaries to a graph
    G = pickled_G
    
    stop_ingredients = ['salt', 'butter', 'sugar', 'black pepper', 'garlic', 'olive oil', 'flour', 'water', 'onions', 'eggs', 'vegetable oil', 'lemon juice', 'milk', 'heavy cream', 'baking powder', 'baking soda', 'bread crumbs', 'cream', 'egg yolks', 'sea salt', 'bread', 'nonstick cooking spray', 'sauce']
    for stop_ing in stop_ingredients:
        G.remove_node(stop_ing)
    
    print(random_recipe_recommender(G))