from django.shortcuts import render, redirect, get_list_or_404
from apps.resumo.forms import ResumoForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .views import *
from apps.resumo.models import Resumo




@login_required(login_url='login')
def index(request):

    user = request.user

    try:
        resumo = get_list_or_404(Resumo, usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')

    return render(request, 'estabelecimentos/index.html')