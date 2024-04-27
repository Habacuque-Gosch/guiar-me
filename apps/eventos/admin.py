from django.contrib import admin
from apps.eventos.models import Evento



class ListandoEvento(admin.ModelAdmin):
    list_display = ("id", "nome", "local")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("local",)
    # list_editable = ("publicada",)
    list_per_page = 20

admin.site.register(Evento, ListandoEvento)