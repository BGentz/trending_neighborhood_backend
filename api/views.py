# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse


@csrf_exempt
def user_submit(request):
    received = request.body
    print(type(received))
    print(received)
    message_data = {'message': 'Test message'}
    print(message_data)


# b'{"city":"Chicago","categories":
# {"accessability":0,"artsAndEntertainment":0,"bars":0,
# "localEvents":3,"restaurants":0,"retail":2,"schools":0}}'

    return JsonResponse(data=message_data, status=200)
    # if request.method == "POST":
    #     print(request.body)
