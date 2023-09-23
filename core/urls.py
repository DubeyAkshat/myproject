from django.urls import path
from .views import AllCarsView, CarView

urlpatterns = [
    path('cars/', AllCarsView.as_view(), name='Create Car'),
    path('cars/<int:id>/', CarView, name='Car'),
]