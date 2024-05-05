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

    user = request.user

    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login')

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    estabelecimentos = Estabelecimento.objects.filter(publicada=True)

    return render(request, 'estabelecimentos/index.html', {'estabelecimentos': estabelecimentos})

def estabelecimento(request, estabelecimento_id):

    user = request.user

    if not user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('login')

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')
    
    try:
        estabelecimentos = get_object_or_404(Estabelecimento, pk=estabelecimento_id)

    except:
        return render(request, 'estabelecimentos/estabelecimento.html')


    return render(request, 'estabelecimentos/estabelecimento.html', {'estabelecimentos': estabelecimentos})


