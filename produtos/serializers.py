from rest_framework import serializers
from .models import Produto, ProdutoFornecedor

from fornecedores.serializers import FornecedorSerializer

class ProdutoFornecedorSerializer():
    class Meta:
        model = ProdutoFornecedor
        fields = ['nome_fantasia', ]

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField()
    fornecedores = ProdutoFornecedorSerializer()
    class Meta:
        model = Produto
        fields = '__all__'
