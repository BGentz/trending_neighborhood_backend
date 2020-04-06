import pandas as pd
import json

with open('./filtered.txt') as f:
  data = json.load(f)

restaurants = []

for index, value in enumerate(data):
    if('Food' in str(data[index]['categories'])):
        restaurants.append(data[index])
    elif('food' in str(data[index]['categories'])):
        restaurants.append(data[index])
    elif('Restaurant' in str(data[index]['categories'])):
        restaurants.append(data[index])
    elif('restaurant' in str(data[index]['categories'])):
        restaurants.append(data[index])

with open('restaurants.json','w') as restaurant_file:
    json.dump(restaurants, restaurant_file)
