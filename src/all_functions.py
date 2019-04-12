#Serializing to a file
import _pickle as pickle

#Libraries for Graph
import networkx as nx

#Python Library for Dataframe usage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import random
from collections import Counter

#PandaDF of ingredients and their associated flavor molecules
#Opening the pickled file
pickle_in = open("./data/ingredients/ingredient_only_pd.pickle", "rb")
#Getting the PandaDF from the pickle
ingredient_only_pd = pickle.load(pickle_in)

"""
GRAPH CREATION
"""

def graph_based_on_ingredient_with_associated_flavor_molecule_creator(pandas_df = ingredient_only_pd):
    #Initializing Graph
    G=nx.Graph()

    #iterate through each row of flavorDB based on if index is in random sample
    for index, row in pandas_df.iterrows():

        #name of the ingredient from the "rows" 
        ingredient_1 = row["ingredient"]
        #category of the ingredient from the "rows"
        category = row["category"]
        #set of the ingredient from the "rows"
        set_of_molecules= row["set_molecules"]

        #creating an ingredient node and adding attributes
        G.add_node(ingredient_1)
        G.node[ingredient_1]["ingredient_node"] = True
        G.node[ingredient_1]["molecule_node"] = False
        G.node[ingredient_1]["category"] = category

        # to keep track of what's going on
        for molecule in set_of_molecules:           
            #creating a molecule node and adding attribute
            G.add_node(molecule)
            G.node[molecule]["molecule_node"] = True
            G.node[molecule]["ingredient_node"] = False
            G.add_edge(ingredient_1, molecule)
    return G



def graph_based_on_shared_molecule_creator(pandas_df = ingredient_only_pd, intersection_ratio = 0.25):
    #Initializing Graph
    G=nx.Graph()

    #iterate through each row of flavorDB 
    for index, row1 in pandas_df.iterrows():
        #ingredient name
        ingredient_1 = row1["ingredient"]
        #ingredient category
        category_1 = row1["category"]
        molecules_1 = row1["set_molecules"]

        G.add_node(ingredient_1)
        G.node[ingredient_1]["ingredient_node"] = True
        G.node[ingredient_1]["molecule_node"] = False
        G.node[ingredient_1]["category"] = category_1

        for index, row2 in pandas_df.iterrows():
            ingredient_2 = row2["ingredient"]
            
            #checks to see if ingredients are different
            if ingredient_1 != ingredient_2:
                G.add_node(ingredient_1)
                category_2 = row2["category"]
                molecules_2 = row2["set_molecules"]

                G.node[ingredient_1]["ingredient_node"] = True
                G.node[ingredient_1]["molecule_node"] = False
                G.node[ingredient_1]["category"] = category_2
                
                num_intersection = len(molecules_1.intersection(molecules_2))
                total_molecules = len(molecules_1.union(molecules_2))
                intersection_ratio = num_intersection / total_molecules
                if intersection_ratio > intersection_ratio:
                    G.add_edge(ingredient_1, ingredient_2, weight=num_intersection)
    return G

"""
ANALYSIS
"""

def common_pair_analysis(ing1, ing2, pandas_df = ingredient_only_pd, graph_it = False, print_statements = False):
    demo_G=nx.Graph()
    mol_list = []
    #iterate through each row of flavorDB based on if index is in random sample
    for index, row in pandas_df.iterrows():
        #set of the ingredient from the "rows"
        set_mol= row["set_molecules"]
        #name of the ingredient from the "rows" 
        ingredient_1 = row["ingredient"]

        if ingredient_1 in [ing1, ing2]:
            mol_list.append(set_mol)
            for molecule in set_mol:
                demo_G.add_node(ingredient_1)
                demo_G.node[ingredient_1]["ingredient_node"] = True
                demo_G.add_node(molecule)
                demo_G.node[molecule]["molecule_node"] = True
                demo_G.add_edge(ingredient_1, molecule)
    ingredient_nodes = nx.get_node_attributes(demo_G, 'ingredient_node').keys()
    molecule_nodes = nx.get_node_attributes(demo_G, 'molecule_node').keys()
    pos=nx.spring_layout(demo_G)
    if graph_it == True:
        nx.draw_networkx_nodes(demo_G,pos,
                            nodelist=ingredient_nodes,
                            node_color='r',
                            node_size=500,
                        alpha=0.8)
        nx.draw_networkx_nodes(demo_G,pos,
                            nodelist=molecule_nodes,
                            node_color='b',
                            node_size=500,
                        alpha=0.8)
    
    shared_molecules = mol_list[0].intersection(mol_list[1])
    mol_for_ing_1 = mol_list[0].difference(mol_list[1])
    mol_for_ing_2 = mol_list[1].difference(mol_list[0])
    
    ratio_shared_to_total = len(shared_molecules) / len(mol_list[1].union(mol_list[0]))
    num_unique_molecules_1 = len(mol_for_ing_1)
    num_unique_molecules_2 = len(mol_for_ing_2)
    num_shared_molecules = len(shared_molecules)    
    if print_statements == True:
        print("number of shared molecules: ", num_shared_molecules)
        print("number of unique molecules to {}: ".format(ing1), len(mol_for_ing_1))
        print("number of unique molecules to {}: ".format(ing2), len(mol_for_ing_2))
        print("ratio of shared to total: ", ratio_shared_to_total)
    return ratio_shared_to_total, num_unique_molecules_1, num_unique_molecules_2, num_shared_molecules

if __name__ == "__main__":
    pass