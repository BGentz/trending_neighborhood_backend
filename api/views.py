# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from .predictor import predict
from .models import Neighborhoods


@csrf_exempt
def user_submit(request):
    received = request.body
    print(type(received))
    print(received)
    message_data = predict()
    print(message_data)
    return JsonResponse(data=message_data, safe=False, status=200)
    # if request.method == "POST":
    #     print(request.body)

def neighborhoods_data(request):
    query = Neighborhoods.all()
    # needs serializer
    return JsonResponse(data=query, status=200)

def Neighborhoods_detail(request, name):
    # add city into request if we have more cities
    # add filter by city if expanded
    query = Neighborhoods.get(neighborhood_name = name)
    # needs serializer
    return JsonResponse(data=query, status=200)