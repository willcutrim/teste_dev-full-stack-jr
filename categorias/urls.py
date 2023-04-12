from django.urls import path

from .views import CategoriaList, CategoriaInfo

urlpatterns = [
    path('', CategoriaList.as_view()),
    path('<int:id>', CategoriaInfo.as_view())
]
