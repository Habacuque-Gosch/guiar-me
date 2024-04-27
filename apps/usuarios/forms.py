from django import forms
# from apps.usuarios.models import Resumo



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user-login",
                "placeholder" : "Entre com seu usuário"
            }
        )
    )
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user-login",
                "placeholder" : "Digite sua senha",
                "id":'input-senha'
            }
        )
    )



class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite seu nome de usuário"
            }
        )
    )
    
    email = forms.CharField(
        label="Digite seu email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite seu email"
            }
        )
    )

    senha_cadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua senha",
                "id":'input-senha'
            }
        )
    )

    senha_confirma = forms.CharField(
        label="Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Confirme sua senha",
                "id":'input-senha-confirma'

            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            