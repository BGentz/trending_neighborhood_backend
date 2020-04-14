import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter, defaultdict
import math
import copy
from IPython import embed


def cluster_and_rank(loc_data, preferences_dict):
  """
  if no preferences are given, then the results are the same methodology as the original
  """
  # consider changing file manipulation to django query if this is incorporated in the backend
  # filename = 'zillow_city_scrapes_converted'

  # with open(f'./{filename}.json') as f:
    # django query for data (add filter if cities are added):
    # data = Neighborhoods.all()
  data = [item for item in loc_data]
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

  # preferences should be in list form in this order:
  # [walkscore, grocery, parks, errands, drink, shopping, culture, schools, transit, bike]
  # unpack preferences_dict
  if preferences_dict == {}:
    preferences = [100]*10
  else:  
    preferences = []
    preferences.append(preferences_dict['Walkability'])
    preferences.append(preferences_dict['Groceries'])
    preferences.append(preferences_dict['Parks'])
    preferences.append(preferences_dict['Errands'])
    preferences.append(preferences_dict['Restaurants and Bars'])
    preferences.append(preferences_dict['Shopping'])
    preferences.append(preferences_dict['Entertainment'])
    preferences.append(preferences_dict['Schools'])
    preferences.append(preferences_dict['Public Transit'])
    preferences.append(preferences_dict['Biking'])

  # Rescale data for reproducing results:
  def rescale_data(num):
    max = 100
    min = 0
    n_new = (num - min) / (max - min)
    return n_new

  # compute vector norm for clustering
  def compute_distance(array):
    n = 0
    for num in array:
      n += (num**2)
    return math.sqrt(n)


  for value in data:
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
    loc.append(([walkscore[index], grocery[index], parks[index], errands[index], drink[index], shopping[index], culture[index], schools[index], transit[index], bike[index]]))

  # take input preferences and adjust the loc scores
  for entry_index in range(len(loc)):
    for pref_index in range(len(preferences)):
      if preferences[pref_index] == 99:
        loc[entry_index][pref_index] *= (preferences[pref_index] + 1) 
      else:
        loc[entry_index][pref_index] *= preferences[pref_index] 
      loc[entry_index][pref_index] = rescale_data(loc[entry_index][pref_index])

  pre_clustered_data = np.array(loc)
  clustered_data = np.array([])
  for row in pre_clustered_data:
    clustered_data = np.append(clustered_data,compute_distance(row))
  clustered_data = clustered_data.reshape(-1,1)
  

  total_clusters = 21
  clusters = KMeans(n_clusters=total_clusters, random_state = 42).fit(clustered_data)
  cluster_centers = clusters.cluster_centers_
  cluster_labels=clusters.predict(clustered_data)

  # reshape to 1d array
  cluster_distances = cluster_centers.reshape(21)


  distance_label_zip = list(zip(range(total_clusters),cluster_distances))
  distance_label_zip_sorted = sorted(distance_label_zip, key = lambda entry: entry[1])
  sorted_labels = [item[0] for item in distance_label_zip_sorted]

  for index in range(len(data)):
    data[index]['Overall Score'] = sorted_labels.index(cluster_labels[index])*5
  
  return data