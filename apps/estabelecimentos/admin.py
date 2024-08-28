from django.contrib import admin
from apps.estabelecimentos.models import Estabelecimento
from apps.estabelecimentos.models import Produto


class ListandoEstabelecimentos(admin.ModelAdmin):
    list_display = ("id", "nome", "local", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 20

admin.site.register(Estabelecimento, ListandoEstabelecimentos)


class ListandoProdutos(admin.ModelAdmin):

    list_display = ("id", "nome", "disponivel")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_editable = ("disponivel",)
    list_per_page = 20

admin.site.register(Produto, ListandoProdutos)