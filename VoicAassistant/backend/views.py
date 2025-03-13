from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ApiView(APIView):
    def get(self, request):
        return Response({"message": "Hello from DRF API!"}, status=status.HTTP_200_OK)