from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from apps.resumo.forms import ResumoForms
from apps.estabelecimentos.models import Estabelecimento
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .views import *
from apps.resumo.models import Resumo




# @login_required(login_url='login')
def index(request):
    ''' função responsavél por entregar os objetos do banco de dados: Estabelecimento'''

    user = request.user

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    estabelecimentos = Estabelecimento.objects.filter(publicada=True)

    return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})


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



