from builtins import object

class NeighborhoodSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_neighborhoods(self):
        output = {'data':[]}

        for hood in self.body:
            hood_obj = {}
            hood_obj["Neighborhood"]= hood.neighborhood_name
            hood_obj["Overall Score"]= hood.overall_score
            hood_obj["breakdown"]= {
                "Walkability": float(hood.walkability_score),
                "Groceries": float(hood.groceries_score),
                "Parks": float(hood.parks_score),
                "Errands": float(hood.errands_score),
                "Restaurants and Bars":float (hood.restaurants_bars_score),
                "Shopping": float(hood.shopping_score),
                "Entertainment": float(hood.entertainment_scores),
                "Schools": float(hood.schools_scores),
                "Public Transit": float(hood.transit_scores),
                "Biking": float(hood.bike_scores)
            }
            output['data'].append(hood_obj)

        return output
