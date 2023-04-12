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