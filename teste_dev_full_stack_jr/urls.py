
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('produtos/', include('produtos.urls')),
    path('categorias/', include('categorias.urls')),
    path('fornecedores/', include('fornecedores.urls')),
]
