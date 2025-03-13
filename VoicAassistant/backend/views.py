from django.shortcuts import render
from django.http import JsonResponse

def api_view(request):
    return JsonResponse({"message": "Hello from Api"})