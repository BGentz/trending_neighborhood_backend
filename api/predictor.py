import random
import json

def predict():

    data = [
        [       {
                    "Neighborhood": "Lincoln Park",
                    "Overall Score": 79,
                    "lat": 41.986793817732305,
                    "lon": -87.89185685316146,
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
        ],

        [       {
                    "Neighborhood": "Test Neighborhood 2",
                    "Overall Score": 45,
                    "lat": 41.952543817732305,
                    "lon": -87.84360685316146,
                    "breakdown": {
                                    "Walkability": 28,
                                    "Groceries": 58,
                                    "Parks": 61,
                                    "Errands": 43,
                                    "Restaurants and Bars": 44,
                                    "Shopping": 8,
                                    "Entertainment": 12,
                                    "Schools": 7,
                                    "Public Transit": 41,
                                    "Biking": 27
                                }
                },
                {
                    "Neighborhood": 'Test Neighborhood 3',
                    "Overall Score": 45,
                    "lat": 41.986793817732305,
                    "lon": -87.84360685316146,
                    "breakdown": {
                                    "Walkability": 62,
                                    "Groceries": 75,
                                    "Parks": 68,
                                    "Errands": 86,
                                    "Restaurants and Bars": 68,
                                    "Shopping": 80,
                                    "Entertainment": 4,
                                    "Schools": 12,
                                    "Public Transit": 62,
                                    "Biking": 53
                                }
                }
        ],

        [
                {
                    "Neighborhood": 'Test Neighborhood 4',
                    "Overall Score": 17,
                    "lat": 41.781293817732305,
                    "lon": -87.79535685316146,
                    "breakdown": {
                                    "Walkability": 45,
                                    "Groceries": 15,
                                    "Parks": 29,
                                    "Errands": 58,
                                    "Restaurants and Bars": 45,
                                    "Shopping": 76,
                                    "Entertainment": 8,
                                    "Schools": 77,
                                    "Public Transit": 46,
                                    "Biking": 46
                                }
                },
                {
                    "Neighborhood": 'Test Neighborhood 5',
                    "Overall Score": 28,
                    "lat": 41.781293817732305,
                    "lon": -87.74710685316147,
                    "breakdown": {
                                    "Walkability": 39,
                                    "Groceries": 5,
                                    "Parks": 78,
                                    "Errands": 67,
                                    "Restaurants and Bars": 53,
                                    "Shopping": 55,
                                    "Entertainment": 31,
                                    "Schools": 9,
                                    "Public Transit": 67,
                                    "Biking": 40
                    }
                },
                {
                    "Neighborhood": 'Test Neighborhood 6',
                    "Overall Score": 99,
                    "lat": 41.918293817732305,
                    "lon": -87.79535685316146,
                    "breakdown": {
                                    "Walkability": 66,
                                    "Groceries": 71,
                                    "Parks": 100,
                                    "Errands": 61,
                                    "Restaurants and Bars": 56,
                                    "Shopping": 75,
                                    "Entertainment": 86,
                                    "Schools": 44,
                                    "Public Transit": 56,
                                    "Biking": 64
                                }
                }
        ],


        [
            {
                "Neighborhood": 'Test Neighborhood 7',
                "Overall Score": 43,
                "lat": 41.952543817732305,
                "lon": -87.79535685316146,
                "breakdown": {
                                "Walkability": 75,
                                "Groceries": 96,
                                "Parks": 66,
                                "Errands": 82,
                                "Restaurants and Bars": 67,
                                "Shopping": 88,
                                "Entertainment": 63,
                                "Schools": 51,
                                "Public Transit": 48,
                                "Biking": 73
                            }
            },
            {
                "Neighborhood": 'Test Neighborhood 8',
                "Overall Score": 38,
                "lat": 41.986793817732305,
                "lon": -87.79535685316146,
                "breakdown": {
                                "Walkability": 59,
                                "Groceries": 5,
                                "Parks": 92,
                                "Errands": 82,
                                "Restaurants and Bars": 63,
                                "Shopping": 72,
                                "Entertainment": 49,
                                "Schools": 83,
                                "Public Transit": 57,
                                "Biking": 67
                            }
            }
        ],

        [
            {
                "Neighborhood": 'Test Neighborhood 9',
                "Overall Score": 34,
                "lat": 41.952543817732305,
                "lon": -87.74710685316147,
                "breakdown": {
                                "Walkability": 89,
                                "Groceries": 83,
                                "Parks": 94,
                                "Errands": 94,
                                "Restaurants and Bars": 87,
                                "Shopping": 96,
                                "Entertainment": 99,
                                "Schools": 66,
                                "Public Transit": 66,
                                "Biking": 67
                            }
            },
            {
                "Neighborhood": 'Test Neighborhood 10',
                "Overall Score": 89,
                "lat": 41.986793817732305,
                "lon": -87.74710685316147,
                "breakdown": {
                                "Walkability": 59,
                                "Groceries": 71,
                                "Parks": 89,
                                "Errands": 81,
                                "Restaurants and Bars": 56,
                                "Shopping": 35,
                                "Entertainment": 9,
                                "Schools": 77,
                                "Public Transit": 35,
                                "Biking": 72
                            }
            }
        ]
    ]
    choice = random.randint(0,len(data)-1)
    return json.dumps(data[choice])