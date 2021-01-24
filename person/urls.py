from django.contrib import admin
from django.urls import path, include
from .views import PersonView


urlpatterns = [
    path('', PersonView.as_view({'post': 'create'})),
    path('<pk>/', PersonView.as_view({'get': 'retrieve'}))
]
