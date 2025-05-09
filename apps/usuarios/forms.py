from django import forms
# from apps.usuarios.models import Resumo
from django import forms
from .models import Profile



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "campo-user",
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
                "class": "campo-user",
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
        label="Confirme sua senha",
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

class ChangePassForms(forms.Form):
    senha_atual = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua senha atual",
                "id":'input-senha'
            }
        )
    )

    senha_nova = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Digite sua nova senha",
                "id":'input-senha-confirma'
            }
        )
    )

    senha_nova_confirma = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "campo-user",
                "placeholder" : "Confirme sua nova senha",
                "id":'input-senha-confirma-nova'

            }
        )
    )


class ResumoForms(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['usuario', 'estabelecimentos_fav']

        labels = {
            'foto' : ' ',
            'orientacao_sexual' : ' ',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo','placeholder':'Digite seu nome'}),
            'idade': forms.TextInput(attrs={'class': 'campo-user', 'id': 'campo-age', 'placeholder':'Digite sua idade'}),
            'orientacao_sexual': forms.Select(attrs={'class': 'select-user', 'id': 'sexo', 'placeholder':'Selecione seu sexo'}),
            'foto': forms.FileInput(attrs={'class': 'upload-img', 'id': 'upload-img'}),
            'tags_filtro': forms.SelectMultiple(attrs={'class': 'tags_filtro', 'id': 'tags_filtro'}),
        }


