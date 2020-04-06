import pandas as pd
import json

with open('./filtered.txt') as f:
  data = json.load(f)

arts = []
for index, value in enumerate(data):
    if('Arts & Entertainment' in str(data[index]['categories'])):
        arts.append(data[index])
    elif('arts & entertainment' in str(data[index]['categories'])):
        arts.append(data[index])


with open('arts.json','w') as arts_file:
    json.dump(arts, arts_file)