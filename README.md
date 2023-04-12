<h1>Teste para à vaga de dev</h1>

## Instalação do projeto.
Para utilizar voce precisa primeiro, executar o comando:
```
pip install -r requirements.txt
```
execute os comandos:
```
python manage.py makemigrations / python manage.py migrate
```

Depois execute o projeto:
```
python manage.py runserver
```

# Utilize o Postman ou insomnia para fazer requisição a API.
## Links da API endpoint PRODUTOs:

#### adicionar e buscar todos os produtos: method [POST] - [GET]
```
http://127.0.0.1:8000/produtos
```

#### buscar produto específicos: [GET]
```
http://127.0.0.1:8000/produtos/[id]
```

#### adicionar e buscar todas as categorias: method [POST] - [GET]
```
http://127.0.0.1:8000/categorias/
```

#### adicionar e buscar todos os fornecedores: method [POST] - [GET]
```
http://127.0.0.1:8000/fornecedores/
```

#### buscar fornecedor específico: [GET]
```
http://127.0.0.1:8000/fornecedores/[id]
```


*- Lembrando que a segurança não foi um ponto abordado nesse projeto.*
