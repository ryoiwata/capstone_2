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

x = 1
#looping through each ingredient from the list
for ingredient in pickled_list:
    #name of the ingredient to query, formating for website query
    #lowercasing, replacing the spaces for pluses
    ing_name = "+".join(ingredient.split()).lower()
    
    #for testing purposes, remove afterwards
    ing_name = "sadlfkj"

    # to check progress of scraper
    x += 1
    print(x)
    print(ing_name)

    
    for num in range(1,10): # will need to incorporate looping through each page
        # to check progress of scraper
        print("page: {}".format(num))
        url = "http://www.recipepuppy.com/?i={}&q={}&p={}".format(ing_name, ing_name, num)
        print(url)

        #access the page
        recipe_puppy_page = requests.get(url)
        soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')


        try:
            #See if the query exists, we are looking for the word "sorry" in text
            query_result = soup.find('div', style='padding:5px').text.split()
            
            #Conditional to see if there are any queries, if not then the scraper will go to the next
            #If the text contains "sorry, then we'll move on to the next ingredient"
            if query_result[0].strip() == "Sorry":
                print("I'm sorry")
                break
        except:
            pass


    break

"""

#see if there is anything on the page
url = "http://www.recipepuppy.com/?i=sdf&q="
recipe_puppy_page = requests.get(url)
soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')
text = soup.find("div", class_ = "right")
print(text)

"""

# recipe_puppy_page = requests.get('http://www.recipepuppy.com/?i={}&q='.format(name))

# x = 0 
# for name in pickled_list:


    
#     try:
#         #need to incorporate a for loop for each page num of ingredient 
        
#         if len(name.split()) >= 1:
#             joined_name = "+".join(name.split())
#             recipe_puppy_page = requests.get('http://www.recipepuppy.com/?i={}&q='.format(joined_name))

#         elif len(name.split()) == 0:
#             recipe_puppy_page = requests.get('http://www.recipepuppy.com/?i={}&q='.format(name))

#         #Soup object accesses the HTML of the Request object
#         soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')
        
#         #Goes through each recip in the page
#         for recipe in soup.findAll('div', class_='result'):
#             print("hello!")   

#         print("It worked!")
#     except:
#         print("Couldn't quite work!")
      
#     #to keep track of progress
#     x += 1
#     print(x)
#     break

