from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from apps.usuarios.forms import LoginForms, CadastroForms, ChangePassForms
# from django.contrib.auth import update_session_auth_hash, login, authenticate





def home(request):
    ''' Função responsável pela tela inicial do App'''
    user = request.user
    if user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('index')
    
    return render(request, 'usuarios/home/home.html')

def home_plataforma(request):
    ''' Função responsável pela tela inicial do App'''
    user = request.user
    if user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('dashboard')
    
    return render(request, 'plataforma/home.html')

def login_plataforma(request):
    ''' Realiza o login do usuario na aplicação '''

    user = request.user

    if user.is_authenticated:
        # messages.error(request, "Usuário não logado")
        return redirect('dashboard')

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
                return redirect('dashboard')
            else:
                messages.error(request, "usuário ou senha inválido")
                return redirect('login_plataforma')

    return render(request, 'plataforma/usuarios/login/login.html', {"form": form})

def cadastro_plataforma(request):
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
            return redirect('dashboard')
        else:
            messages.error(request, "usuário ou senha inválido")
            return redirect('login_plataforma')
    

    return render(request, 'plataforma/usuarios/cadastro/cadastro.html', {"form": form})

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
            return redirect('novo_perfil')
        else:
            messages.error(request, "usuário ou senha inválido")
            return redirect('login')
    

    return render(request, 'usuarios/cadastro/cadastro.html', {"form": form})

def logout(request):
    ''' Realiza o logout do usuario na aplicação '''
    # messages.success(request, "Logout efetuado com sucesso")
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def trocar_senha(request):
    ''' Realiza a troca de senha do usuario no sistema '''

    user = request.user

    form = ChangePassForms()
    
    if request.method == 'POST':
        form = ChangePassForms(request.POST)
        
        if form.is_valid():
            if form["senha_nova"].value() != form["senha_nova_confirma"].value():
                messages.error(request, "senhas não são iguais")
                return redirect('trocar_senha')

            # senha_atual = request.POST['input_senha']
            
            # check_senha = user.check_password(senha_atual)

            # if check_senha == True:

            #     senha_nova = form["senha_nova"].value()

            #     usuario = form.save()
            #     update_session_auth_hash(request, usuario)  # Important!

            #     autenticate_user = auth.authenticate(request, username=user, password=senha_nova)

            #     if autenticate_user is not None:
            #         login(request, autenticate_user)

            #     return redirect('index')

            senha_atual = form["senha_atual"].value()
            
            check_senha = user.check_password(senha_atual)

            if check_senha == True:
                senha_nova = form["senha_nova"].value()

                usuario = User.objects.get(username=user)
                usuario.set_password(senha_nova)
                usuario.save()
                return redirect('/')

            
            else:
                return redirect('trocar_senha')

    return render(request, 'usuarios/configuracoes/trocar_senha.html', {"form": form})


