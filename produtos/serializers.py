from rest_framework import serializers
from .models import Produto, ProdutoFornecedor


class ProdutoFornecedorSerializer():
    
    class Meta:
        model = ProdutoFornecedor
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField()
    fornecedores = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Produto
        fields = '__all__'
