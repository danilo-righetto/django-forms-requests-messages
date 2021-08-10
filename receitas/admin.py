from django.contrib import admin
from .models import Receitas


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_da_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_da_receita')
    search_fields = ('nome_da_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Receitas, ListandoReceitas)

# Register your models here.
