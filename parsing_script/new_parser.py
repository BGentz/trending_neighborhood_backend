import pandas as pd
import json
import math

with open('./city_scrapes.json') as f:
  data = json.load(f)

parsed = []


for index, value in enumerate(data):
    breakdown = []

    key = list(value.keys())
    key = str(key[0])

    neighborhood = list(value.keys())
    neighborhood = str(neighborhood[0])
    neighborhood = neighborhood.replace('_', ' ')

    for subindex in range (0, len(data[index][key])):
        breakdown_name = data[index][key][subindex]['name']
        breakdown_score = math.floor(float(data[index][key][subindex]['score']))

        if(breakdown_name == 'Dining & Drinking'):
            breakdown_name = 'Restaurants and Bars'

        if(breakdown_name == 'Culture & Entertainment'):
            breakdown_name = 'Entertainment'

        if(breakdown_name == 'Walk'):
            breakdown_name = 'Walkability'

        if(breakdown_name == 'Transit'):
            breakdown_name = 'Public Transit'

        if(breakdown_name == 'Bike'):
            breakdown_name = 'Biking'

        breakdown.append([breakdown_name, breakdown_score])


    parsed.append({'Neighborhood': neighborhood,
                   'Overall Score': 'Score here',
                   'breakdown': {
                       'Walkability': breakdown[7][1],
                       'Groceries': breakdown[1][1],
                       'Parks': breakdown[4][1],
                       'Errands': breakdown[3][1],
                       'Restaurants and Bars': breakdown[0][1],
                       'Shopping': breakdown[2][1],
                       'Entertainment': breakdown[6][1],
                       'Schools': breakdown[5][1],
                       'Public Transit': breakdown[8][1],
                       'Biking': breakdown[9][1]

                                }
                    }
                  )

with open(f'./city_scrapes_converted.json', 'w') as outfile:
    json.dump(parsed, outfile)
