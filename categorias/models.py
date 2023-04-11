from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    date_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome