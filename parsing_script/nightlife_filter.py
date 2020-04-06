import pandas as pd
import json

with open('./filtered.txt') as f:
  data = json.load(f)

nightlife = []
for index, value in enumerate(data):
    if('Bars' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('bars' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Nightlife' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Nightlife' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Beer' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('beer' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Wine' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('wine' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Spirits' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('spirits' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Spirits' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('spirits' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('Pubs' in str(data[index]['categories'])):
        nightlife.append(data[index])
    elif('pubs' in str(data[index]['categories'])):
        nightlife.append(data[index])

with open('nightlife.json','w') as restaurant_file:
    json.dump(nightlife, restaurant_file)
