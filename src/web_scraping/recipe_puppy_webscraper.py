#for webscraping
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
import time
import re
import random

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
for ingredient in pickled_list:
    #name of the ingredient to query, formating for website query
    #lowercasing, replacing the spaces for pluses
    ing_for_url = "+".join(ingredient.split()).lower()
    ingredient_name = ingredient.strip().lower()

    # to check progress of scraper
    x += 1
    print("current ingredient number: ", x)
    print("current ingredient: ", ingredient_name)
    

    url = "http://www.recipepuppy.com/?i={}&q={}".format(ing_for_url, ing_for_url)
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
        try:
            #scrapes the number of results
            num_result = soup.find('div', class_='searchStats').find_all('b')[1].text

            #formats the number of results
            num_result = int("".join(num_result.split(",")))
            
            #only the first 1000 recipes can be queried
            if num_result > 1000:
                num_pages = 100
            else: #gets the number of pages to loop through
                num_pages = num_result // 10 + 1
            
            #loops through each page of the ingredient
        except:
            pass
        try:
            for page_num in range(1, num_pages + 1):
                print("page number: ", page_num)
                
                #accessing each page of the ingredient
                url = "http://www.recipepuppy.com/?i={}&q={}&p={}".format(ing_for_url, ing_for_url, page_num)
                recipe_puppy_page = requests.get(url)
                soup = BeautifulSoup(recipe_puppy_page.text, 'html.parser')

                #getting the name, link, and ingredient list of each recipe
                for result in soup.findAll('div', class_ = "result"):
                    result_h3 = result.find('h3')

                    #name of the result 
                    result_name = result_h3.text.strip()
                    # print(result_name)

                    #link of the result
                    result_link = re.findall(r'\"(.+?)\"', str(result_h3))[0].strip()
                    # print(result_link)

                    #a list of all the ingredients in a recipe
                    result_ing_list = [ingredient_name]
                    for recipe_ing in result.find('div', class_ = "ings").findAll('a'):
                        recipe_ing_name = recipe_ing.text.strip("+")
                        result_ing_list.append(recipe_ing_name)
                    result_ing_list.sort()
                    
                    print(ingredient_name)
                    print(result_name)
                    print(result_link)
                    print(result_ing_list)
                    
                    #put the recipes into mongoDB
                    collections.insert_one({"searched_ingredient" : ingredient_name,"recipe_name" : result_name, "recipe_ingredients" : result_ing_list, "recipe_link": result_link})

                    #stop breaker in between pages
                    random_num = random.randint(1,10)
                    time.sleep(random_num / 1000)  
        except:
            pass
        
            
print("all done!")

     


