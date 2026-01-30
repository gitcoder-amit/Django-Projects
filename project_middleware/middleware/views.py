from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    data = {
        "message": "Welcome to the Middleware Demo!",
        "status": True
    }
    return JsonResponse(data)  # this will convert dictionary to JSON response
