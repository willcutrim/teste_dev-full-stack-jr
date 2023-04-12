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

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco_serializer = EnderecoSerializer(data=endereco_data)
        endereco_serializer.is_valid(raise_exception=True)
        endereco = endereco_serializer.save()

        fornecedor = Fornecedor.objects.create(endereco=endereco, **validated_data)

        return fornecedor