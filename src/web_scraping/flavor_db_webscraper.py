import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# Create instance of the MongoClient class
client = MongoClient()
database = client['food_map']   # Database name (to connect to)
collections = database['flavor_molecules'] # Collection name (to use)

#list of entries to redo if webscraping takes too long
redo_entries_list = []

#Loops through each ingredient page of FlavorDB
for num in range(0,973):
    print("Currently on page: {}".format(num))
    
    try:
        pg_num = num
        #Request each ingredient page using pg_num variable
        flavor_db_webpage =requests.get('https://cosylab.iiitd.edu.in/flavordb/entity_details?id={}'.format(pg_num))
        
        #Soup object accesses the HTML of the Request object
        soup = BeautifulSoup(flavor_db_webpage.text, 'html.parser')
        
        #Scrape the ingredient name
        ingredient_name = str(soup.find('h1', class_='text-primary text-capitalize').text).strip()

        #Scrape the category name
        category_name = str(soup.find('span', class_='text-capitalize').text).strip()
        
        #Acess the table (https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table)
        molecule_table = soup.find('table', id= 'molecules')
        table_body = molecule_table.find('tbody')

        #initiating a list for each molecule variable    
        list_molecule_names = []
        list_molecule_id = []
        list_molecule_flavor = []

        #Access every row in the table 
        for row in table_body.find_all('tr'):
            #Access molecule name, id, and flavor in each row
            molecule_name = row.findAll('td')[0].text.strip()
            molecule_id = row.findAll('td')[1].text.strip()
            molecule_flavor = row.findAll('td')[2].text.strip().split(",")
            list_molecule_names.append(molecule_name)
            list_molecule_id.append(molecule_id)
            list_molecule_flavor.append(molecule_flavor)
   
        # Insert everything into MondoDB
        collections.insert_one({"ingredient": ingredient_name, "catgeory": category_name, "molecules": list_molecule_names, "molecule_IDs": list_molecule_id, "flavor_of_molecules": list_molecule_flavor})
        
        # #Print Statement to Check What's Going On
        data = collections.find_one({"ingredient": ingredient_name}, {"ingredient": ingredient_name, "catgeory": category_name, "molecules": list_molecule_names})
        print(data)
    except:
        print("something's not right")
        redo_entries_list.append(num)
        
       
        


