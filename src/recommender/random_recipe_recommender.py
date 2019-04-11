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
    
    all_recipe_comb = list(combinations(list_of_nodes, 2))
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

    # #Where the nodes of the random walk will be placed into
    # random_nodes = []

    # #random walk for inputted iterations
    # for num in range(iterations):
    
    #     #current node always restarts to the original ingredient
    #     current_node = ingredient

    #     #walk a inputted number of steps
    #     for num in range(steps):
            
    #         #return back to the original node at a inputted probability 
    #         if G.nodes[current_node]["molecule_node"] == True:
                
    #             #states if something should return of not given the probability 
    #             return_bool = np.random.choice(np.array([0,1]), p=[1 - return_prob, return_prob])
                
    #             #returns back to the original node
    #             if return_bool == 1:
    #                 current_node = ingredient  

    #             #continues exploring other nodes    
    #             elif return_bool == 0:
    #                 number_of_edges = len(G[current_node])
    #                 random_number = random.randint(0, number_of_edges - 1)
    #                 current_node = list(G[current_node])[random_number]           
            
    #         #does not return to the original node if the current node is also an ingredient
    #         else:
    #             number_of_edges = len(G[current_node])
    #             random_number = random.randint(0, number_of_edges - 1)
    #             current_node = list(G[current_node])[random_number]
        
    #     #adds to the list once done
    #     random_nodes.append(current_node)

    # return Counter(random_nodes)


if __name__ == "__main__":
    #Opening the pickled file
    #Needs to be opened in the recommender folder
    pickle_in = open("./data/graph/recipe_graph.pickle","rb")

    #Getting the dictionary from the pickle
    pickled_G = pickle.load(pickle_in)

    #Converting a dictionary of dictionaries to a graph
    G = pickled_G
    print(random_recipe_recommender(G))