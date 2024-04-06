from django.shortcuts import render
from .views import *

def index(request):
    return render(request, 'estabelecimentos/index.html')