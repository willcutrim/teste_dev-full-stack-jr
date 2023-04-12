from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Produto, ProdutoFornecedor
from categorias.models import Categoria
from .serializers import ProdutoSerializer, ProdutoFornecedorSerializer


class ProdutoList(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        categoria_id = request.data.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)

        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['categoria'] = categoria
            produto = serializer.save()
            return Response(ProdutoSerializer(produto).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProdutoInfo(APIView):
    def get_produto(self, id):
        try:
            return Produto.objects.get(id=id)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, id):
        fornecedor_id = self.get_produto(id)
        serializer = ProdutoSerializer(fornecedor_id)
        return Response(serializer.data)
    
    def delete(self, request, id):
        produto = self.get_produto(id)
        produto.delete()
        message = {'message': 'Produto deletado com sucesso!'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        produto = self.get_produto(id)
        categoria_id = request.data.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['categoria'] = categoria
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
