import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict
import math
from IPython import embed


filename = 'zillow_city_scrapes_converted'

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
  # for index in range(0, len(value['breakdown'])):
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

total_clusters = 11
clusters = KMeans(n_clusters=total_clusters).fit(clustered_data)
cluster_centers = clusters.cluster_centers_
cluster_labels=clusters.predict(clustered_data)

# Compute cluster distances
cluster_distances = []
for center in cluster_centers:
  sum = 0
  for point in center:
    sum += (point ** 2)
  cluster_distances.append(math.sqrt(sum))

distance_label_zip = list(zip(range(total_clusters),cluster_distances))
distance_label_zip_sorted = sorted(distance_label_zip, key = lambda entry: entry[1])
sorted_labels = [item[0] for item in distance_label_zip_sorted]

for index in range(len(data)):
  data[index]['Overall Score'] = sorted_labels.index(cluster_labels[index])*10

# data = [i for i in zip(cluster_labels, clustered_data)]

# print(data)

output = []

# embed()
with open(f'./{filename}_output.json', 'w') as outfile:
    json.dump(data, outfile)
