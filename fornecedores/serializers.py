from rest_framework import serializers
from .models import Fornecedor, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class FornecedorSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Fornecedor
        fields = '__all__'
