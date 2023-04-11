from django.contrib import admin

from .models import Fornecedor, Endereco

admin.site.register(Fornecedor)
admin.site.register(Endereco)

