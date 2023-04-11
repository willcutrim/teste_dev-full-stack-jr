from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}'

class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_fantasia