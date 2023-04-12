from django.urls import path

from .views import FornecedoresList, FornecedorDetail

urlpatterns = [
    path('', FornecedoresList.as_view()),
    path('<int:id>', FornecedorDetail.as_view())   
]