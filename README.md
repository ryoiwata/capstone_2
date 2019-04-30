# Map of the Food World Based on Flavor Molecule Associations in Recipes

## Currently being edited and cleaned up. Thank you for your patience and reach out if you have any questions! (4/30/2019)

I will make a “map” of food ingredients that will have paths with other ingredients. These paths will be scaled by the the association between the food molecules of the two ingredients. The association will be calculated by the occurrence of two different food molecules from two different ingredients within any given cooking recipe. With such a map, I can find “communities” within ingredients that have closer associations than compared to those outside of it. Similar research has been done by Dr. Yong-Yeol Ahn et al.  (https://www.nature.com/articles/srep00196) In their studies, they have created graphs models that show the relationship between ingredients determined by the number of shared flavor molecules. I will build off of their work, by considering flavor molecules that are not necessarily the same between different ingredients. This will explore relationships of different flavor molecules that can then be extended to the ingredients themselves. The relationship can be calculated because patterns in cooking recipes can begin to display what goes into the synergy of flavor molecular combination.  

# Other Information 

For food ingredients and their associated flavor molecules, I will refer to Dr. Ganesh Bagler’s FlavorDB (https://cosylab.iiitd.edu.in/flavordb/). From FlavorDB, I have collected information in the format of food ingredients as indexes to a list of its flavor molecules.  For cooking recipes and ingredients, I will refer to Recipe Lab’s Recipe Puppy API (http://www.recipepuppy.com/about/api/) From Recipe Puppy API, I have collected information in the form of a list of ingredients for each recipe. I have collected information from both these sites using Python’s web scraping library, BeautifulSoup. Summing up to approximately 400 ingredients, 1,000 flavor compounds, and 100,000 recipes. The information was stored in a MongoDB database. The project will be presented with visualisations of the map of food ingredients in powerpoint slides accompanied by explanations. Due to the number of ingredients, significant time will have to be put into making all the ingredients and their associations visible. As well representing the ingredients according to the number and strength of associations. 

# Background and Motivation 

Findings and models from the proposed study can be used to discover novel food pairings that can not be reasonably uncovered from the countless possible combinations of ingredients. In addition, relationships of flavor molecules can provide the basis for generating new molecules if further analyzed with biochemical properties. 

# Potential Problems

Potential problems arise from ingredient names having similar names such as onion and onion powder. These ingredients can be the same as in the case of pluralization or different in the case of different ingredients. This problem will be addressed by using approximate string matching that will help take into account different grammatical tenses of words while separating out different ingredients. 
Other problems include how several flavor molecules are shared by a large number of ingredients and will result in an overly dense map that will be difficult to visually represent. Such considerations will be addressed similarly to that done by Yong-Yeol Ahn et al by utilizing the backbone extraction method to find statistically significant links. 

# Looking Ahead

The next few parts of the project consist of cleaning up the data by standardizing the names of ingredients between the different databases along with additional webscraping as needed. To begin modeling, I will start off by mapping the ingredients based on simple numerical occurrences of two different ingredient within a recipe. This will allow for a framework to scale up while being able to choose what considerations to apply based on domain research. 

# References

https://www.nature.com/articles/srep00196
https://cosylab.iiitd.edu.in/flavordb/
http://www.recipepuppy.com/about/api/
