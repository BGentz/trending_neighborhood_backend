import pandas as pd
import json

with open('./filtered.txt') as f:
  data = json.load(f)

retail = []
for index, value in enumerate(data):
    if('Shopping' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('shopping' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Fashion' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('fashion' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Shoe' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('shoe' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Clothing' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('clothing' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Book' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('book' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Store' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('store' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('Electronic' in str(data[index]['categories'])):
        retail.append(data[index])
    elif('electronic' in str(data[index]['categories'])):
        retail.append(data[index])

with open('retail.json','w') as restaurant_file:
    json.dump(retail, restaurant_file)
