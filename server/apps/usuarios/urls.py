from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('', home, name = 'home'),  
    path('plataforma/', home_plataforma, name = 'home_plataforma'),  
    path('login-plataforma/', login_plataforma, name = 'login_plataforma'),
    path('cadastro-plataforma/', cadastro_plataforma, name = 'cadastro_plataforma'),
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
    path('change-pass/', trocar_senha, name = 'trocar_senha'),
]
