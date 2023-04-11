from django.contrib import admin

from .models import Produto, ProdutoFornecedor

admin.site.register(Produto)
admin.site.register(ProdutoFornecedor)

