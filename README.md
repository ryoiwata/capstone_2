# Ingredient Analysis in Recipes with Graph Theory

## Summary 

Through webscraped cooking recipes from Recipe Puppy API, I found ingredients pairs that can act as substitutes for each other in recipes that contain either ingredient. 

## Data Sources

### Flavor DB
For food ingredients and their associated flavor molecules, I will refer to Dr. Ganesh Bagler’s FlavorDB (https://cosylab.iiitd.edu.in/flavordb/). From FlavorDB, I have collected information in the format of food ingredients as indexes to a list of its flavor molecules.  

### Recipe Puppy API
For cooking recipes and ingredients, I will refer to Recipe Lab’s Recipe Puppy API (http://www.recipepuppy.com/about/api/) From Recipe Puppy API, I have collected information in the form of a list of ingredients for each recipe. 

- I have collected information from both these sites using Python’s web scraping library, BeautifulSoup. Summing up to approximately 400 ingredients, 1,000 flavor compounds, and 100,000 recipes. The information was stored in a MongoDB database.

## What if graph theory?

Graphs are a way to represent relationships between subjects of interest. In this project, each subject or node is an ingredient. The relationship between each node or edge, would be the number of times the two ingredients share a recipe. 

## Repo layout

For an step by step overview of the project, checkout the Jupyter Notebook file titled:  recipe_graph_demonstration_nb.ipynb

## References

- https://www.nature.com/articles/srep00196
- https://cosylab.iiitd.edu.in/flavordb/
- http://www.recipepuppy.com/about/api/ 
- http://snap.stanford.edu/class/cs224w-2017/projects/cs224w-34-final.pdf 

## Contact Info

Linkedin: https://www.linkedin.com/in/riwata