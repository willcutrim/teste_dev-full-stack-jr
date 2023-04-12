from django.urls import path
from .views import ProdutoList

urlpatterns = [
    path('', ProdutoList.as_view()),
]