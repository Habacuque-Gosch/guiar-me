from django.shortcuts import render, redirect, get_list_or_404
from apps.resumo.forms import ResumoForms
from apps.resumo.models import Resumo
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def novo_perfil(request):
    ''' '''
    current_user = request.user
    print(current_user.id)

    form = ResumoForms

    if request.method == 'POST':

        form = ResumoForms(request.POST, request.FILES)

        if form.is_valid:
            resumo = form.save(commit=False)
            resumo.usuario = current_user
            resumo.save()
            # messages.success(request, "salvo com sucesso")
            resumo = Resumo.objects.get(id=resumo.id)
            return render(request, 'usuarios/cadastro/splash_agradecimento.html', {'resumo': resumo})
            # return redirect('splash_home')

    return render(request, 'usuarios/cadastro/idade_e_nome.html', {'form': form})

def splash_home(request, foto_user_id):
    ''' '''

    current_user = request.user

    # try:
    # resumo = get_list_or_404(Resumo, foto=current_user.foto)
    resumo = Resumo.objects.get(id=foto_user_id)
    #     return render(request, 'usuarios/cadastro/splash_agradecimento.html', {'resumo': resumo})


    # except:
    return render(request, 'usuarios/cadastro/splash_agradecimento.html', {'resumo': resumo})

def config_user(request):
    ''' '''
    current_user = request.user

    # try:
    # resumo = get_list_or_404(Resumo, foto=current_user.foto)
    resumo = Resumo.objects.get(usuario=current_user)

    return render(request, 'usuarios/configuracoes/config.html', {'resumo': resumo})


