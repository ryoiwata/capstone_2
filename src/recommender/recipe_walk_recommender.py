#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#For random walk
import random 
from collections import Counter
import numpy as np

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./data/graph/recipe_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

def recipe_random_walk(ingredient, iterations = 10000, steps = 10, return_prob = 0.001):
    #Where the nodes of the random walk will be placed into
    random_nodes = []

    #random walk for inputted iterations
    for num in range(iterations):
    
        #current node always restarts to the original ingredient
        current_node = ingredient

        #walk a inputted number of steps
        for num in range(steps):
            
            #return back to the original node at a inputted probability 
            if G.nodes[current_node]["molecule_node"] == True:
                
                #states if something should return of not given the probability 
                return_bool = np.random.choice(np.array([0,1]), p=[1 - return_prob, return_prob])
                
                #returns back to the original node
                if return_bool == 1:
                    current_node = ingredient  

                #continues exploring other nodes    
                elif return_bool == 0:
                    number_of_edges = len(G[current_node])
                    random_number = random.randint(0, number_of_edges - 1)
                    current_node = list(G[current_node])[random_number]           
            
            #does not return to the original node if the current node is also an ingredient
            else:
                number_of_edges = len(G[current_node])
                random_number = random.randint(0, number_of_edges - 1)
                current_node = list(G[current_node])[random_number]
        
        #adds to the list once done
        random_nodes.append(current_node)

    return Counter(random_nodes)


if __name__ == "__main__":
    ingredient_1 = "celery"
    iterations = 10000
    steps = 3
    return_prob = 0.001
    print(recipe_random_walk(ingredient_1, iterations, steps, return_prob))