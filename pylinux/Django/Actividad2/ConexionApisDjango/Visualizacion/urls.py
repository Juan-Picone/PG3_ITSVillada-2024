from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.get_first_20_pokemon, name='get_first_20_pokemon'),
]
