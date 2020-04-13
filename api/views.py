# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
# from .predictor import predict
from .models import Neighborhoods
from .serializer import NieghborhoodSerializer
from .helpers.kMeans_estimator import cluster_and_rank
from IPython import embed


@csrf_exempt
def user_submit(request):
    received = json.load(request)
    query = Neighborhoods.objects.filter(city__iexact=received['city']).all()
    serialized_hoods = NieghborhoodSerializer(query).all_neighborhoods
    
    category_scores = received['categories']
    
    # for key, value in enumerate(category_scores):
    #     category_scores[value] = category_scores[value][1]

    if sum(list(category_scores.values())) == 0:
        return JsonResponse(data=serialized_hoods['data'], safe=False, status=200)
    else:
        output = cluster_and_rank(serialized_hoods['data'],category_scores)
        return JsonResponse(data=output, safe=False, status=200)

def neighborhoods_data(request, city):
    query = Neighborhoods.objects.filter(city__iexact=city).all()
    serialized_hoods = NieghborhoodSerializer(query).all_neighborhoods
    return JsonResponse(data=serialized_hoods['data'], safe=False, status=200)

# def Neighborhoods_detail(request, name):
#     # add city into request if we have more cities
#     # add filter by city if expanded
#     query = Neighborhoods.get(neighborhood_name = name)
#     # needs serializer
#     return JsonResponse(data=query, status=200)