from django.urls import path

from .views import FornecedoresList

urlpatterns = [
    path('', FornecedoresList.as_view())    
]