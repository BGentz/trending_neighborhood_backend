# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
# from .predictor import predict
from .models import Neighborhoods
from .serializer import NieghborhoodSerializer
from .helpers.kMeans_estimator import cluster_and_rank
import requests
# from IPython import embed



@csrf_exempt
def user_submit(request):
    received = json.load(request)
    query = Neighborhoods.objects.filter(city__iexact=received['city']).all()
    serialized_hoods = NieghborhoodSerializer(query).all_neighborhoods

    category_scores = received['categories']

    # for key, value in enumerate(category_scores):
    #     category_scores[value] = category_scores[value][1]

    if sum(list(category_scores.values())) == 0:
        output = cluster_and_rank(serialized_hoods['data'], {})
        return JsonResponse(data=output, safe=False, status=200)
    else:
        output = cluster_and_rank(serialized_hoods['data'],category_scores)
        return JsonResponse(data=output, safe=False, status=200)

def neighborhoods_data(request, city):
    query = Neighborhoods.objects.filter(city__iexact=city).all()
    serialized_hoods = NieghborhoodSerializer(query).all_neighborhoods
    output = cluster_and_rank(serialized_hoods['data'], {})
    return JsonResponse(data=output, safe=False, status=200)


def events(request, city):
    api = 'PDPGOtbKM8m0PSczgsJmwG85AMd2XiTh'
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?city={city}&apikey={api}"
    results = requests.get(url)
    results = results.json()

    event_list = []

    for event in results['_embedded']['events']:
        event_list.append(
            {
                'eventUrl': event['url'],
                'eventType': event['type'],
                'images': event['images'],
                'date': event['dates']['start']['localDate'],
                'time': event['dates']['start']['localTime'][0:5],
                'address': event['_embedded']['venues'][0]['address']['line1'],
                'city': event['_embedded']['venues'][0]['city']['name'],
                'state': event['_embedded']['venues'][0]['state']['name'],
                'zip': event['_embedded']['venues'][0]['postalCode'],
            }
            )

    return JsonResponse(data=event_list, safe=False, status=200)


# def Neighborhoods_detail(request, name):
#     # add city into request if we have more cities
#     # add filter by city if expanded
#     query = Neighborhoods.get(neighborhood_name = name)
#     # needs serializer
#     return JsonResponse(data=query, status=200)