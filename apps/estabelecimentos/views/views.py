from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from apps.resumo.forms import ResumoForms
from apps.estabelecimentos.models import Estabelecimento
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import pycep_correios
import folium
from folium.plugins import LocateControl
from .views import *
from apps.resumo.models import Resumo



@cache_page(60 * 2)
def index(request):
    ''' função responsavél por entregar os objetos do banco de dados: Estabelecimento'''

    user = request.user

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})


# @cache_page(60 * 2)
def estabelecimento(request, estabelecimento_id):
    ''' função responsavél por entregar os dados de um determinado objeto filtradao por id do banco de dados: Estabelecimento'''

    user = request.user

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    try:
        estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)
        return render(request, 'estabelecimentos/estabelecimento.html', {'estabelecimentos': estabelecimentos})

    except:
        return render(request, 'estabelecimentos/estabelecimento.html')


def maps(request):
   
    coordenadas = [-27.6307035,-48.6840267]

    map = folium.Map(location=coordenadas, zoom_start=16, zoom_control=False)
    folium.TileLayer('cartodbdark_matter').add_to(map)

    folium.Marker(
        location=coordenadas,
        popup="<i>O lugar que você procura</i>",
        icon= folium.Icon(icon="glyphicon glyphicon-record", prefix="glyphicon", icon_color="white", color="green"),
        tooltip="Estabelecimento"
    ).add_to(map)

    LocateControl(auto_start= False,KeepCurrentZoomLevel = False).add_to(map)

    map = map._repr_html_()
    context = {
        'map': map,
    }

    return render(request, 'estabelecimentos/map.html', context)



