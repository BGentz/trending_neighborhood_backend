# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_submit(request):
    if request.method == "POST":  # if it's a post request
        json = request.POST['json']
        print(type(json))
        print(json)

    else:
        print('Get request')
