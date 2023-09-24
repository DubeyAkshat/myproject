from django.urls import path
from .views import AllCarsView, CarView

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Cars API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('cars/', AllCarsView.as_view(), name='Create Car'),
    path('cars/<int:id>/', CarView, name='Car'),
]