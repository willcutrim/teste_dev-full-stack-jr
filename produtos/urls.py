from django.urls import path
from .views import ProdutoList

urlpatterns = [
    path('get-test/', ProdutoList.as_view())
]