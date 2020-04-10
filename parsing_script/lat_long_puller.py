import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict
import math
from IPython import embed


filename = 'parsed'

with open(f'./{filename}.json') as f:
  data = json.load(f)
  district = []
  subdistrict = []
  lat = []
  lon = []
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


for line in data:
  lat.append(line['lat'])
  lon.append(line['lon'])
  walkscore.append(line['walkscore'])
  grocery.append(line['grocery'])
  parks.append(line['parks'])
  errands.append(line['errands'])
  drink.append(line['drink'])
  shopping.append(line['shopping'])
  culture.append(line['culture'])
  schools.append(line['schools'])
  transit.append(line['transit'])
  bike.append(line['bike'])

loc = []


for index in range(0, len(lat)):
  loc.append([float(lat[index]), float(lon[index]), float(walkscore[index]), float(grocery[index]), float(parks[index]), float(errands[index]), float(drink[index]), float(shopping[index]), float(culture[index]), float(schools[index]), float(transit[index]), float(bike[index])])
clustered_data = np.array(loc)
total_clusters = 10
clusters = KMeans(n_clusters=total_clusters).fit_predict(clustered_data[2:,:])

data = [i for i in zip(clusters, clustered_data)]

output = []

for index in range(0, len(data)):
    print(index)
    output.append({'Neighborhood': 'Neighborhood goes here',
                   'Overall Score': 'Overall score goes here',
                   'breakdown': {
                     'Walkability': math.floor(float(data[index][1][2])),
                     'Groceries': math.floor(float(data[index][1][3])),
                     'Parks': math.floor(float(data[index][1][4])),
                     'Errands': math.floor(float(data[index][1][5])),
                     'Restaurants and Bars': math.floor(float(data[index][1][6])),
                     'Shopping': math.floor(float(data[index][1][7])),
                     'Entertainment': math.floor(float(data[index][1][8])),
                     'Schools': math.floor(float(data[index][1][9])),
                     'Public Transit': math.floor(float(data[index][1][10])),
                     'Biking': math.floor(float(data[index][1][11]))
                   }
                   })

with open(f'./{filename}_output.json', 'w') as outfile:
    json.dump(output, outfile)
