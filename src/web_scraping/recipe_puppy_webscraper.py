#for webscraping
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time

#for access to databases
from pymongo import MongoClient

#For using a pickled list
import pickle

# Create instance of the MongoClient class
client = MongoClient()
database = client['food_map']   # Database name (to connect to)
collections = database['recipies'] # Collection name (to use)

#Opening the pickled file
#Needs to be opened in the recommender folder
pickle_in = open("./ingredient_full_list.pickle","rb")

#Getting the dictionary from the pickle
pickled_list = pickle.load(pickle_in)

x = 0
#looping through each ingredient from the list
for ingredient in pickled_list[:5]:
    #name of the ingredient to query, formating for website query
    #lowercasing, replacing the spaces for pluses
    ing_name = "+".join(ingredient.split()).lower()
    
    #for testing purposes, remove afterwards
    # ing_name = "gfdfj"

    # to check progress of scraper
    x += 1
    print(x)
    print(ing_name)
    
    url = "http://www.recipepuppy.com/?i={}&q={}".format(ing_name, ing_name)
    recipe_puppy_page = requests.get(url)
    soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')

    try:
        #See if the query exists, we are looking for the word "sorry" in text
        query_result = soup.find('div', style='padding:5px').text.split()
        
        #Conditional to see if there are any queries, if not then the scraper will go to the next
        #If the text contains "sorry, then we'll move on to the next ingredient"
        if query_result[0].strip() == "Sorry":
            print("No results here")
            continue
    except: #if query exists we'll loop through each page of the ingredients
        num_result = soup.find('div', class_='searchStats')
        """
        MAKE SURE TO BE ABLE TO GET THE NUMBER OF RESULTS
        """
        for num in range(1,5): # will need to incorporate looping through each page
                # to check progress of scraper
                print("page: {}".format(num))
                url = "http://www.recipepuppy.com/?i={}&q={}&p={}".format(ing_name, ing_name, num)
                print(url)

                #access the page
                recipe_puppy_page = requests.get(url)
                soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')
    


