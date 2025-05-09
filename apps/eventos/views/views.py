from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from apps.eventos.models import Evento
# from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
# from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .views import *
from apps.usuarios.models import Profile



@cache_page(60 * 2)
@login_required(login_url='login')
def index_eventos(request):
    ''' função responsavél por entregar os objetos do banco de dados: Evento'''
    
    eventos = Evento.objects.order_by("data_publicada").reverse().filter(publicada=True)

    return render(request, 'eventos/index.html', {'eventos': eventos})

@cache_page(60 * 2)
@login_required(login_url='login')
def evento(request, evento_id):
    ''' função responsavél por entregar os dados de um determinado objeto filtradao por id do banco de dados: Evento'''

    user = request.user

    try:
        profile = get_list_or_404(Profile, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')

    try:
        eventos = get_object_or_404(Evento, pk=evento_id)
        return render(request, 'eventos/evento.html', {'eventos': eventos})

    except:
        return render(request, 'eventos/evento.html')

