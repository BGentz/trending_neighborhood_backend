import geopandas as gpd
import json
import random

from shapely.geometry import Point

def check(point, shape_data):
    """
    point should be in the format of [lon, lat]
    """
    pt = Point(point[0],point[1])
    for i in range(len(shape_data)):
        shape = shape_data.loc[i,"geometry"]
        hood = shape_data.loc[i,"name"]
        if shape.contains(pt):
            return hood

    return "None"


def predict():

    neighborhoods_path = './zillow-neighborhoods.geojson'
    shape_data = gpd.read_file(neighborhoods_path)

    data = [
        [       {
                    "Neighborhood": check([-87.89185685316146, 41.986793817732305], shape_data),
                    "Overall Score": 79,
                    "breakdown": {
                                    "Walkability": 5,
                                    "Groceries": 0,
                                    "Parks": 0,
                                    "Errands": 0,
                                    "Restaurants and Bars": 24,
                                    "Shopping": 0,
                                    "Entertainment": 0,
                                    "Schools": 0,
                                    "Public Transit": 34,
                                    "Biking": 27
                                }
                }
        ]
    ]
    choice = random.randint(0,len(data)-1)
    return json.dumps(data[choice])




print(predict())