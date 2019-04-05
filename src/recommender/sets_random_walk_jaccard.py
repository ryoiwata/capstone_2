#For graphing
import matplotlib.pyplot as plt
import networkx as nx

#For using a pickled dictionary
import pickle

#For random walk
import random 

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./../../data/graph/molecule_full_graph.pickle","rb")

#Getting the dictionary from the pickle
pickled_G = pickle.load(pickle_in)

#Converting a dictionary of dictionaries to a graph
G = pickled_G

def random_walk_jacaard_sets(ingredient_1, ingredient_2, iterations = 1000, steps = 2):

    random_nodes, random_nodes_2 = set([]), set([])
    #random walk for ingredient 1
    for num in range(iterations):
        current_node = ingredient_1
        for num in range(steps):
            number_of_edges = len(G[current_node])
            random_number = random.randint(0, number_of_edges - 1)
            current_node = list(G[current_node])[random_number]
        random_nodes.add(current_node)

    #random walk for ingredient 2
    for num in range(iterations):
        current_node = ingredient_2
        for num in range(steps):
            number_of_edges = len(G[current_node])
            random_number = random.randint(0, number_of_edges - 1)
            current_node = list(G[current_node])[random_number]
        random_nodes_2.add(current_node)

    #jaccard similarity 
    intersection = random_nodes.intersection(random_nodes_2)
    union = random_nodes.union(random_nodes_2)
    if len(intersection) >= 1:
        jaccard_similarity = len(intersection) / len(union)
        # print("intersecting molecules: ", intersection)
        print("occurances of item 1 in intersection: ", list(intersection).count(ingredient_1))
        print("occurances of item 2 in intersection: ", list(intersection).count(ingredient_2))
        print("number of intersections: ", len(intersection))
        print("jacaard similarity: ", jaccard_similarity)
        return(jaccard_similarity)

    else:
        print("nothing in common!")



if __name__ == "__main__":
    ingredient_1 = "Mozzarella Cheese"
    ingredient_2 = "Chocolate"
    iterations = 1000
    steps = 100
    random_walk_jacaard_sets(ingredient_1, ingredient_2, iterations, steps)


