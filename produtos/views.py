from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class TestClass(APIView):
    def get(self, request):
        return Response({'status': '200'})