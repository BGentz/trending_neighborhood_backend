import pandas as pd
import json

with open('./walkscore_subset.txt') as f:
  data = json.load(f)

parsed = []


for index, value in enumerate(data):
    for subindex in range(0, len(data[f'{value}'])):
        subdistrict_num = subindex
        lon = data[value][subindex]['point'][0]
        lat = data[value][subindex]['point'][1]
        walkscore = data[value][subindex]['score']['walkscore']
        grocery = data[value][subindex]['score']['categoryscores']['grocery_P']['score']
        parks = data[value][subindex]['score']['categoryscores']['parks_P']['score']
        errands = data[value][subindex]['score']['categoryscores']['errands_C']['score']
        drink = data[value][subindex]['score']['categoryscores']['dine_drink_C']['score']
        shopping = data[value][subindex]['score']['categoryscores']['shopping_C']['score']
        culture = data[value][subindex]['score']['categoryscores']['culture_C']['score']
        schools = data[value][subindex]['score']['categoryscores']['schools_P']['score']
        transit = data[value][subindex]['score']['transit']['score']
        bike = data[value][subindex]['score']['bike']['score']
        parsed.append({'district': value, 'subdistrict': subdistrict_num,
                            'lat': lat, 'lon': lon, 'walkscore': walkscore,
                            'grocery': grocery, 'parks': parks, 'errands': errands,
                            'drink': drink, 'shopping': shopping, 'culture': culture,
                            'schools': schools, 'transit': transit, 'bike': bike})

    # parsed.append(subdistrict)

with open('parsed.json','w') as parsed_file:
    json.dump(parsed, parsed_file)