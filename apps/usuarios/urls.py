from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('', home, name = 'home'),
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
]
