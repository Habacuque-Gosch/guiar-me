from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from apps.resumo.forms import ResumoForms
from apps.resumo.models import Resumo



@login_required(login_url='login')
def novo_perfil(request):
    ''' função responsável por exibir a página de criação de perfil '''
    current_user = request.user

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

        else:
            return redirect('novo_perfil')

    return render(request, 'usuarios/cadastro/idade_e_nome.html', {'form': form})

def splash_home(request, foto_user_id):
    ''' '''

    resumo = Resumo.objects.get(id=foto_user_id)

    return render(request, 'usuarios/cadastro/splash_agradecimento.html', {'resumo': resumo})

def config_user(request):
    ''' função responsável por renderizar a página de usuário '''

    user = request.user

    try:
        resumo = Resumo.objects.get(usuario=user)
    except:
        # messages.error(request, "Preencha seu perfil")
        return redirect('novo_perfil')

    resumo = Resumo.objects.get(usuario=user)

    return render(request, 'usuarios/configuracoes/config.html', {'resumo': resumo})

@login_required(login_url='login')
def editar_perfil(request, resumo_id):
    user = request.user
    
    resumo = Resumo.objects.get(id=resumo_id)
    form = ResumoForms(instance=resumo)

    if request.method == 'POST':
        form = ResumoForms(request.POST, request.FILES, instance=resumo)
        if form.is_valid():
            form.save()
            # messages.success(request, "Resumo editado com sucesso")
            return redirect('configuracoes_user')

    return render(request, 'usuarios/configuracoes/editar_resumo.html', {"form": form, "resumo_id": resumo_id, "resumo":resumo})


@login_required(login_url='login')
def favoritos(request):

    current_user = request.user

    resumo = Resumo.objects.get(usuario=current_user)

    return render(request, 'usuarios/configuracoes/favoritos.html', {'resumo': resumo})