# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from .predictor import predict


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