import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict
import math
# from IPython import embed


filename = 'city_scrapes_converted'

with open(f'./{filename}.json') as f:
  data = json.load(f)
  walkscore = []
  grocery = []
  parks = []
  errands = []
  drink = []
  shopping = []
  culture = []
  schools = []
  transit = []
  bike = []


for key, value in enumerate(data):
  for index in range(0, len(value['breakdown'])):
    walkscore.append(value['breakdown']['Walkability'])
    grocery.append(value['breakdown']['Groceries'])
    parks.append(value['breakdown']['Parks'])
    errands.append(value['breakdown']['Errands'])
    drink.append(value['breakdown']['Restaurants and Bars'])
    shopping.append(value['breakdown']['Shopping'])
    culture.append(value['breakdown']['Entertainment'])
    schools.append(value['breakdown']['Schools'])
    transit.append(value['breakdown']['Public Transit'])
    bike.append(value['breakdown']['Biking'])

loc = []


for index in range(0, len(walkscore)):
  loc.append([walkscore[index], grocery[index], parks[index], errands[index], drink[index], shopping[index], culture[index], schools[index], transit[index], bike[index]])

clustered_data = np.array(loc)

total_clusters = 10
clusters = KMeans(n_clusters=total_clusters).fit_predict(clustered_data)

data = [i for i in zip(clusters, clustered_data)]

print(data)

output = []


with open(f'./{filename}_output.json', 'w') as outfile:
    json.dump(output, outfile)
