from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import CarSerializer
from .models import Car

class ListCarsView(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse({'cars': serializer.data})