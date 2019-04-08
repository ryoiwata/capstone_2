import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from communities import find_communities_modularities
from communities import find_communities_n, find_communities_modularity



karateG = nx.karate_club_graph()

comms, mods = find_communities_modularities(karateG)

plt.plot(list(range(1,len(mods)+1)), mods, ':o')
plt.xlabel('number of communities')
plt.ylabel('modularity')
plt.savefig('modularities_community.png')

plt.show()