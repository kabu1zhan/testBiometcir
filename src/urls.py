from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="MoveOn API",
      default_version='v1',
      description="This is a swagger api for MoveOn app",
      contact=openapi.Contact(email="kabiljanz0301@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name='schema-swagger-ui '),
    path('people/', include('person.urls'))
]
