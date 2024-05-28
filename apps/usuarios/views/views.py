from django.shortcuts import render, redirect, get_list_or_404
# from apps.usuarios.models import Resumo
# from apps.vagas.models import Vagas
from django.contrib.auth.models import User
from django.contrib import auth, messages
from apps.usuarios.forms import LoginForms, CadastroForms



def home(request):
    ''' Função responsável pela tela inicial do App'''
    user = request.user
    if user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('index')
    
    return render(request, 'usuarios/home/home.html')

def login(request):
    ''' Realiza o login do usuario na aplicação '''

    user = request.user

    if user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('index')

    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()
                
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                # messages.success(request, f"{nome} logado com sucesso")
                return redirect('index')
            else:
                messages.error(request, "usuário ou senha inválido")
                return redirect('login')

    return render(request, 'usuarios/login/login.html', {"form": form})

def cadastro(request):
    ''' Realiza o cadastro de um novo usuario no sistema '''
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_cadastro"].value() != form["senha_confirma"].value():
                messages.error(request, "senhas não são iguais")
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_cadastro"].value()
        if  User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já existente")
            return redirect('cadastro')
        
        usuario =  User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        usuario.save()

        nome = form["nome_cadastro"].value()
        senha = form["senha_cadastro"].value()
                
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        
        if usuario is not None:
            auth.login(request, usuario)
            # messages.success(request, f"{nome} logado com sucesso")
            return redirect('index')
        else:
            messages.error(request, "usuário ou senha inválido")
            return redirect('login')
    

    return render(request, 'usuarios/cadastro/cadastro.html', {"form": form})

def logout(request):
    ''' Realiza o logout do usuario na aplicação '''
    # messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('/')

def trocar_senha(request):
    return render(request, 'usuarios/configuracoes/trocar_senha.html')


