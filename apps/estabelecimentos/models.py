from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Produto(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    preco = models.FloatField(default=0.0, max_length=120, null=False, blank=False)
    serve = models.IntegerField(null=True, blank=False)
    imagem_produto = models.ImageField(upload_to="fotos/produtos/%Y/%m/%d/", blank=True)
    disponivel = models.BooleanField(default=True)
    usuario_business_prod = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_business_prod",
    )

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):

    OPCOES_CATEGORIAO = [
        ("Árabe", "ARABE"),
        ("Brasileira", "BRASILEIRA" ),
        ("Chinesa", "CHINESA" ),
        ("Italiana", "ITALIANA" ),
        ("Fast Food", "FASTFOOD" ),
        ("Gourmet", "GOURMET" ),
        ("Japonesa", "JAPONESA" ),
        ("Mexicana", "MEXICANA" ),
        ("Vegetariana", "VEGETARIANA" ),
        ("Vegana", "VEGANA" ),
        ("Pizza", "PIZZA" ),
        ("Sushi", "SUSHI" ),
        ("Frutos do mar", "FRUTOSMAR" ),
        ("Hambúrguer", "HAMBURGUER" ),
        ("Massa", "MASSA" ),
        ("Carne", "CARNE" ),
        ("Peixe", "PEIXE" ),
        ("Sopa", "SOPA" ),
        ("Salada", "SALADA" ),
        ("Sobremesa", "SOBREMESSA" ),
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
    produtos = models.ManyToManyField(Produto, related_name='produtos_adicionados', blank=True, null=True)
    visualizacoes = models.IntegerField(default=0.0,null=True, blank=True)
    usuario_business = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user_business",
    )

    def __str__(self):
        return self.nome

