import pandas as pd
import json

old_file = open('./yelp_academic_dataset_business.json', 'r')
selector = '"state":"IL"'

new = open('./filtered.txt', 'w')
for line in old_file:
    if(selector in line):
        new_file = str(line + ',')
        new.write(new_file)
new.close()
