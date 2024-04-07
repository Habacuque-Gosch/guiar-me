from django.urls import path
from .views import *


urlpatterns = [
    # path('', loader, name = 'loader'),
    # path('home/', home, name = 'home'),
    path('index/', index, name = 'index'),
    path('buscar', buscar, name="buscar"),    
]
