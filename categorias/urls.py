from django.urls import path

from .views import CategoriaList

urlpatterns = [
    path('', CategoriaList.as_view())
]