from django.shortcuts import render
from django.http import JsonResponse
from .models import Store

# Create your views here.


def index(request):
    print(request.headers.get('bmp_id'))
    store = Store.objects.get(bmp_id = request.headers.get('bmp'))
    data = {
        "message": "Welcome to the Middleware Demo!",
        "status": True,
        "data" : {
            "store_name": store.store_name,
            "bmp_id": store.bmp_id
            }
        }
    return JsonResponse(data)  # this will convert dictionary to JSON response
