import geopandas as gpd
from shapely.geometry import Point
import json

neighborhoods_path = './zillow-neighborhoods.geojson'
neighborhoods_data = gpd.read_file(neighborhoods_path)

def check_neighborhood(point, shape_data):
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