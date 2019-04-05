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
pickle_in = open("./../../data/graph/molecule_full_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

def random_walk_jacaard_lists(ingredient_1, iterations = 1000, steps = 2, return_prob = 0.9):
    print(G.nodes[ingredient_1])
    # random_nodes = []
    # #random walk for ingredient 1
    # for num in range(iterations):
    #     current_node = ingredient_1
    #     for num in range(steps):
    #         # if G[ingredient_1]["molecule_node"] == True:
    #         #     return_bool = np.random.choice(np.arange(0,1), p=[1 - return_prob, return_prob])
    #         #     print(return_bool)
    #         #     if return_bool == 1:
    #         #         current_node = ingredient_1  
    #         #     elif return_bool == 0:
    #         #         number_of_edges = len(G[current_node])
    #         #         random_number = random.randint(0, number_of_edges - 1)
    #         #         current_node = list(G[current_node])[random_number]           
    #         # else:
    #         number_of_edges = len(G[current_node])
    #         random_number = random.randint(0, number_of_edges - 1)
    #         current_node = list(G[current_node])[random_number]
    #     random_nodes.append(current_node)
    #     # print(current_node)
    # # print(random_nodes)
    # return Counter(random_nodes)




if __name__ == "__main__":
    ingredient_1 = "Mozzarella Cheese"
    # ingredient_2 = "Chocolate"
    iterations = 10000
    steps = 10
    print(random_walk_jacaard_lists(ingredient_1, iterations, steps))


