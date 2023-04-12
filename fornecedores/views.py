from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Fornecedor, Endereco
from .serializers import FornecedorSerializer

class FornecedoresList(APIView):
    def get(self, request):
        produtos = Fornecedor.objects.all()
        serializer = FornecedorSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FornecedorDetail(APIView):
    def get_fornecedor(self, id):
        try:
            return Fornecedor.objects.get(id=id)
        except Fornecedor.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        fornecedor_id = self.get_fornecedor(id)
        serializer = FornecedorSerializer(fornecedor_id)
        return Response(serializer.data)
    
    def delete(self, request, id):
        fornecedor = self.get_fornecedor(id)
        fornecedor.delete()
        message = {'message': 'fornecedor deletado com sucesso!'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)
