import pickle
import pandas as pd


#Opening the pickled file
pickle_in = open("flavor_matrix_dict.pickle","rb")

#Getting the dictionary from the pickle
flavor_matrix_dict = pickle.load(pickle_in)

#Making a dataframe out of the dictionary of dictionaries
flavor_matrix_df = pd.DataFrame(flavor_matrix_dict)

print(flavor_matrix_df.head())