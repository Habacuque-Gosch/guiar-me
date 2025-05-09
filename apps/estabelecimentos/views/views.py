from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from .views import *
from apps.estabelecimentos.models import Estabelecimento
from apps.usuarios.models import Profile
import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import pycep_correios
import folium
from folium.plugins import LocateControl




@login_required(login_url='login')
@cache_page(60 * 2)
def index(request):
    ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
    estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})


@cache_page(60 * 2)
def estabelecimento(request, estabelecimento_id):
    ''' função responsavél por entregar os dados de um determinado estabelecimendo filtrado por id do banco de dados: Estabelecimento'''

    user = request.user

    try:
        profile = get_list_or_404(Profile, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)

    estabelecimentos.visualizacoes = estabelecimentos.visualizacoes + 1
    estabelecimentos.save()

    produtos_adicionados = estabelecimentos.produtos.all().filter(disponivel=True)
    
    try:
        estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)
        return render(request, 'estabelecimentos/estabelecimento.html', {'estabelecimentos': estabelecimentos, 'produtos_adicionados': produtos_adicionados})

    except:
        return render(request, 'estabelecimentos/estabelecimento.html')


@login_required(login_url='login')
def maps_estabelecimentos(request, estabelecimento_id):
    ''' Funcionalidade responsável por processar os dados de lat e long e renderizar o componente mapa'''

    estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)

    cep_estabelecimento = str(estabelecimentos.cep)

    endereco_estabelecimento = pycep_correios.get_address_from_cep(cep_estabelecimento)

    geolocator = Nominatim(user_agent="GuiarMe")
    location = geolocator.geocode(endereco_estabelecimento['logradouro'] + ", " + endereco_estabelecimento['bairro'] + ", ")

    #LATIDUDE E LOGITUDE COLETA
    lat_estabelecimento, long_estabelecimento = location.latitude, location.longitude
    #COORDENADAS DA COLETA
    coordenadas_estabelecimento = lat_estabelecimento, long_estabelecimento

    map = folium.Map(location=coordenadas_estabelecimento, zoom_start=16, zoom_control=False)
    folium.TileLayer('cartodbdark_matter').add_to(map)

    folium.Marker(
        location=coordenadas_estabelecimento,
        popup=f"<b>{estabelecimentos.nome}</b>",
        icon= folium.Icon(icon="glyphicon glyphicon-record", prefix="glyphicon", icon_color="white", color="blue"),
        tooltip="Estabelecimento"
    ).add_to(map)

    LocateControl(auto_start= False,KeepCurrentZoomLevel = False).add_to(map)

    map = map._repr_html_()
    context = {
        'map': map,
    }

    return render(request, 'estabelecimentos/map.html', context)


@login_required(login_url='login')
# @cache_page(60 * 2)
def dashboard(request):
    ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
    # estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    # return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})

    user = User.objects.get(id=request.user.id)
    
    profile_user = Profile.get_profile(usuario_id=request.user.id)

    estabelecimento = Estabelecimento.objects.get(usuario_business_id=request.user.id)

    print(estabelecimento)

    return render(request, 'plataforma/dashboard/index.html', {'profile_business':profile_user,'estabelecimento_business': estabelecimento})

@login_required(login_url='login')
# @cache_page(60 * 2)
def menu(request):
    ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
    # estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    # return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})
    return render(request, 'plataforma/cardapio/index.html')


@login_required(login_url='login')
# @cache_page(60 * 2)
def my_events(request):
    ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
    # estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    # return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})
    return render(request, 'plataforma/eventos/index.html')


@login_required(login_url='login')
# @cache_page(60 * 2)
def my_reviews(request):
    ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
    # estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    # return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})
    return render(request, 'plataforma/avaliacoes/index.html')


# @login_required(login_url='login-plataforma')
# # @cache_page(60 * 2)
# def menu(request):
#     ''' função responsável por entregar os objetos do banco de dados: Estabelecimento '''
    
#     # estabelecimentos = Estabelecimento.objects.order_by("data_publicada").reverse().filter(publicada=True)

#     # return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})
#     return render(request, 'plataforma/cardapio/index.html')
