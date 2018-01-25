from django.urls import path
from .views import Main, get_coords, get_intent

urlpatterns = [
    path('', Main.as_view(), name='index'),
    path(r'ajax/get_coords/', get_coords, name='get_coords'),
    path(r'ajax/get_intent/', get_intent, name='get_intent'),
]
