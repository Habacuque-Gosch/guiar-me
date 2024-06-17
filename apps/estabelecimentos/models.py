from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Estabelecimento(models.Model):

    OPCOES_CATEGORIAO = [
        ("Árabe", "TESTE"),
        ("Brasileira", "TESTE1" ),
        ("Chinesa", "TESTE2" ),
        ("Italiana", "TESTE2" ),
        ("Fast Food", "TESTE2" ),
        ("Gourmet", "TESTE2" ),
        ("Japonesa", "TESTE2" ),
        ("Mexicana", "TESTE2" ),
        ("Vegetariana", "TESTE2" ),
        ("Vegana", "TESTE2" ),
        ("Pizza", "TESTE2" ),
        ("Sushi", "TESTE2" ),
        ("Frutos do mar", "TESTE2" ),
        ("Hambúrguer", "TESTE2" ),
        ("Massa", "TESTE2" ),
        ("Carne", "TESTE2" ),
        ("Peixe", "TESTE2" ),
        ("Sopa", "TESTE2" ),
        ("Salada", "TESTE2" ),
        ("Sobremesa", "TESTE2" ),
    ]

    nome = models.CharField(max_length=150, null=False, blank=False)
    preco_medio = models.FloatField(default=0.0, max_length=120, null=False, blank=False)
    avaliacao = models.FloatField(max_length=150, null=True, blank=False)
    # numero_telefone = models.CharField(max_length=20, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAO, default='')
    descricao = models.TextField(null=False, blank=False)
    local = models.CharField(max_length=200, null=False, blank=False)
    cep = models.IntegerField(default=0.0,null=False, blank=False)
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

