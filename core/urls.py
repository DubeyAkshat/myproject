from django.urls import path
from .views import ListCarsView

urlpatterns = [
    path('listcars/', ListCarsView.as_view(), name='ListCars')
]