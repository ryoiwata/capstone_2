#Python Library for Dataframe usage
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Libraries for Graph
import networkx as nx

#Serializing to a file
import _pickle as pickle

#PandaDF of ingredients and their associated flavor molecules
#Opening the pickled file
pickle_in = open("./data/ingredients/ingredient_only_pd.pickle", "rb")

#Getting the dictionary from the pickle
ingredient_only_pd = pickle.load(pickle_in)


def common_pair_analysis(ing1, ing2):
    demo_G=nx.Graph()
    mol_list = []
    #iterate through each row of flavorDB based on if index is in random sample
    for index, row in ingredient_only_pd.iterrows():
        #set of the ingredient from the "rows"
        set_mol= row["set_molecules"]
        #name of the ingredient from the "rows" 
        ingredient_1 = row["ingredient"]

        if ingredient_1 in [ing1, ing2]:
            mol_list.append(set_mol)
            for molecule in set_mol:
                # flavor_matrix_df[ingredient_1][molecule] = {'weight': 1}
                demo_G.add_node(ingredient_1)
                demo_G.node[ingredient_1]["ingredient_node"] = True
                demo_G.add_node(molecule)
                demo_G.node[molecule]["molecule_node"] = True
                demo_G.add_edge(ingredient_1, molecule)
    ingredient_nodes = nx.get_node_attributes(demo_G, 'ingredient_node').keys()
    molecule_nodes = nx.get_node_attributes(demo_G, 'molecule_node').keys()
    pos=nx.spring_layout(demo_G)
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
    print("number of shared molecules: ", len(shared_molecules))
    print("number of unique molecules to {}: ".format(ing1), len(mol_for_ing_1))
    print("number of unique molecules to {}: ".format(ing2), len(mol_for_ing_2))
    print("ratio of shared to total: ", len(shared_molecules) / len(mol_list[1].union(mol_list[0])))