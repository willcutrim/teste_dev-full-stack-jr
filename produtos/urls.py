from django.urls import path
from .views import ProdutoList, ProdutoInfo

urlpatterns = [
    path('', ProdutoList.as_view()),
    path('<int:id>', ProdutoInfo.as_view()),
]
