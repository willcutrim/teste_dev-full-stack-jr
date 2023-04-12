from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriaList(APIView):
    def get(self, request):
        produtos = Categoria.objects.all()
        serializer = CategoriaSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoriaInfo(APIView):
    def get_categoria(self, id):
        try:
            return Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, id):
        categoria_id = self.get_categoria(id)
        serializer = CategoriaSerializer(categoria_id)
        return Response(serializer.data)
    
    def delete(self, request, id):
        categoria = self.get_categoria(id)
        categoria.delete()
        message = {'message': 'cattegoria deletado com sucesso!'}
        return Response(message, status=status.HTTP_204_NO_CONTENT)
