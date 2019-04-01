import requests
from bs4 import BeautifulSoup

x = 0
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

    #Scrape the category name
    category_name = str(soup.find('span', class_='text-capitalize').text).strip()
    
    #Acess the table (https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table)
    molecule_table = soup.find('table', id= 'molecules')
    table_body = molecule_table.find('tbody')

    #Access every row in the table 
    
    for row in table_body.find_all('tr'):
        #Access molecule name, id, and flavor in each row
        molecule_name = row.findAll('td')[0]
        molecule_id = row.findAll('td')[1]
        molecule_flavor = row.findAll('td')[2]


        # print(molecule_name.text)
        # print("hello")
        # print(molecule_id.text)
        # print("hello")
        # print(molecule_flavor.text)
        
    break
       
        


