from django.db import models
from categorias.models import Categoria
from fornecedores.models import Fornecedor


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedores = models.ManyToManyField(Fornecedor, through='ProdutoFornecedor')
    date_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    data_atualizacao = models.DateTimeField(auto_now=True, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class ProdutoFornecedor(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto} com {self.fornecedor} por R$ {self.preco_custo}'