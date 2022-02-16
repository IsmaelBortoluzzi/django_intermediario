from django.contrib import admin
from core.models import Produto, Contato


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contato)