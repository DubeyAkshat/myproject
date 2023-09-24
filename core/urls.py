from django.urls import path
from .views import AllCarsView, CarView

# Swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Cars API')

urlpatterns = [
    path('swagger/', schema_view),
    path('cars/', AllCarsView.as_view(), name='Create Car'),
    path('cars/<int:id>/', CarView, name='Car'),
]