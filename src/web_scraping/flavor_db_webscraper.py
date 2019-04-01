import requests
from bs4 import BeautifulSoup


#Loops through each ingredient page of FlavorDB
for num in range(0,973):
    print("Currently on page: {}".format(num))
    pg_num = num
    #Request each ingredient page using pg_num variable
    flavor_db_webpage =requests.get('https://cosylab.iiitd.edu.in/flavordb/entity_details?id={}'.format(pg_num))
    
    #Soup object accesses the HTML of the Request object
    soup = BeautifulSoup(flavor_db_webpage.text, 'html.parser')
    
    #Scrape the ingredient name
    ingredient_name = str(soup.find('h1', class_='text-primary text-capitalize').text).strip()
    
    break


