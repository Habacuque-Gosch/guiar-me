from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Estabelecimento(models.Model):

    OPCOES_CATEGORIAO = [
        ("teste", "TESTE"),
        ("teste1", "TESTE1" ),
        ("teste2", "TESTE2" ),
    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    numero_telefone = models.CharField(max_length=20, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')
    descricao = models.TextField(null=False, blank=False)
    local = models.CharField(max_length=200, null=False, blank=False)
    publicada = models.BooleanField(default=True)
    data_publicada = models.DateTimeField(default=datetime.now, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    # usuario = models.ForeignKey(
    #     to=User,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=False,
    #     related_name="user",
    # )

    def __str__(self):
        return self.nome

