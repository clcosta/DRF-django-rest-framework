# Bem vindo ao projeto **Django Rest Framework**
<p><img height="20" src="https://img.shields.io/badge/Project-TestFramework-green"/></p>

Esse projeto tem o intuito de criar uma API REST simples, com JWT como método de segurança.
Sendo assim ela não tem o objetivo de ser um projeto ou sistema complexo, apenas uma experiência com o framework, toda a construição do banco de dados/modelos está com uma fácil visualização no painel Admin do django.

## Redes Sociais
* [Site](https://portfolio-claudio.herokuapp.com)
* [Instagram](https://www.instagram.com/claudiogfez/)
* [Linkedin](https://www.linkedin.com/in/clcostaf/)

## Instalação

- Primeiramente você pode clonar este repositório.

```
$ git clone https://github.com/clcosta/DRF-django-rest-framework.git
```

- Agora a instalação das bibliotecas

```
pip install -r requirements.txt
```

## Como utilizar

- Com tudo já instalado precisamos iniciar o banco de dados !

```
python manage.py makemigrations

python manage.py migrate
```
- Agora precisamos de um usuario ou superuser !
```
python manage.py createsuperuser
```
- Agora só iniciar o servidor!
```
python manage.py runserver
```

### Token e Auth

O sistema de Autenticação da API funciona através de tokens, no modelo _JWT_. Para as requisições serem executadas com exito é necessário passar um token na requisição no formato de [_Bearer Token_](jwtumtokenseguro).    

#### Pegando o Token
```py linenums="1"
import requests

url = "http://localhost:8000/token/"

payload = {
    "username":"SEU USERNAME",
    "password":"SUA PASSWORD"
}

response = requests.post(url, data=payload)

```

**OUTPUT**
```json
{
  "refresh": "REFRESH TOKEN",
  "access": "ACCESS TOKEN"
}
```

**Token Expired**
O Token obtido na requisição acima tem um limite de tempo que pode ser alterado nas configurações do projeto ___DRF/settings.py___, seguindo todas as instruções da [__documentação__](https://github.com/jpadilla/django-rest-framework-jwt/blob/master/docs/index.md#additional-settings) e suas variáveis.

Caso seu token tenha expirado é so fazer um POST no end-point **`/token/refresh/`** passando o payload **`{"refresh":REFRESH TOKEN}`**, a resposta será um novo access token.

### End-Points

| Modelo      | End Point        | Token | Método                     |
| ---------   | ---------------- | ----- | -------------------------- |
| Alunos      | /api/alunos      | SIM   | GET - POST - PUT - DELETE  |
| Professores | /api/professores | SIM   | GET - POST - PUT - DELETE  |
| Turmas      | /api/turmas      | SIM   | GET - PUT - DELETE         |

### Modelos da API

1. #### Modelo _Alunos_

    `class escola.models.Aluno`

    **Fields**    

    - Nome (nome)

        Required, max_length = 30.

    - CPF (cpf)

        Required, max_length = 14, unique = True, validators = #Sem validação de cpf.

    - Ano Escola (ano_escolar)

        Required, default = ANO_1, choices = Aluno.ano_escolar_choices.

2. #### Modelo _Professor_

    `class escola.models.Professor`

    **Fields**    

    - Nome (nome)

        Required, max_length = 40.

    - CPF (cpf)

        Required, max_length = 14, unique = True, validators = #Sem validação de cpf.

    - Matéria (materia)

        Required, max_length=50, choices = Aluno.materias_choices.

3. #### Modelo _Turma_

    `class escola.models.Turma`

    **Fields**    

    - _Nome_ (nome)

        Required, max_length = 25, default = "3° Ano A - Manhã", unique = True.

    - _Professores_ (professor) [ManyToManyField]

        Required, model = Professor

    - _Alunos_ (alunos) [ManyToManyField]

        Required, model = Aluno

    **Propertys**

    - _qtd_alunos_ -> **int**

        *return* Quantidade de alunos dentro da turma

    - _qtd_professores_ -> **int**

        *return* Quantidade de professores dentro da turma

    - _lista_materias_ -> **list**

        *return* Lista de materias correspondente aos professores já cadastrados na turma

    - _lista_alunos_ -> **list**

        *return* Lista os alunos pelo nome

    - _lista_professores_ -> **list**

        *return* Lista os professores pelo nome



## Exemplos

1. Alunos
    ```py linenums="1"
    import requests

    url = "http://localhost:8000/api/alunos/"

    header_token =  {
        "Accept": "YOUR ACCEPT",
        "User-Agent": "YOUR USER AGENT",
        "Authorization": "Bearer YOUR TOKEN ACCESS HERE"
    }
    response = requests.get(url, header=header_token)

    print(response)

    ```
    **OUTPUT**
    ```json
    [
        {
            "id": 1,
            "nome": "aluno 0",
            "cpf": "000.000.000-00",
            "ano_escolar": "1° Ano"
        },
        {
            "id": 2,
            "nome": "aluno 1",
            "cpf": "111.111.111-11",
            "ano_escolar": "1° Ano"
        },
        ...
    ]
    ```

    Detalhes de um único item (funciona para todos os modelos):

    ```py linenums="1"
    import requests

    url = "http://localhost:8000/api/alunos/1/"

    header_token =  {
        "Accept": "YOUR ACCEPT",
        "User-Agent": "YOUR USER AGENT",
        "Authorization": "Bearer YOUR TOKEN ACCESS HERE"
    }
    response = requests.get(url, header=header_token)

    print(response)

    ```
    **OUTPUT**
    ```json
    {
        "id": 1,
        "nome": "aluno 0",
        "cpf": "000.000.000-00",
        "ano_escolar": "1° Ano"
    }
    ```

2. Professores
    ```py linenums="1"
    import requests

    url = "http://localhost:8000/api/professores/"

    header_token =  {
        "Accept": "YOUR ACCEPT",
        "User-Agent": "YOUR USER AGENT",
        "Authorization": "Bearer YOUR TOKEN ACCESS HERE"
    }
    response = requests.get(url, header=header_token)

    print(response)

    ```
    **OUTPUT**
    ```json
    [
        {
            "id": 1,
            "nome": "professor 1",
            "cpf": "333.333.333-33",
            "materia": "Matemática"
        },
        {
            "id": 2,
            "nome": "professor 2",
            "cpf": "444.444.444-44",
            "materia": "Português"
        },
        ...
    ]
    ```

3. Turma
    ```py linenums="1"
    import requests

    url = "http://localhost:8000/api/turmas/"

    header_token =  {
        "Accept": "YOUR ACCEPT",
        "User-Agent": "YOUR USER AGENT",
        "Authorization": "Bearer YOUR TOKEN ACCESS HERE"
    }
    response = requests.get(url, header=header_token)

    print(response)

    ```
    **OUTPUT**
    ```json
    [
        {
            "id": 1,
            "nome": "1° Ano A - Tarde",
            "qtd_alunos": 3,
            "qtd_professores": 2,
            "lista_materias": [
                "Matemática",
                "Português"
            ],
            "alunos": [
                {
                    "id": 1,
                    "nome": "aluno 0",
                    "cpf": "000.000.000-00",
                    "ano_escolar": "1° Ano"
                },
                {
                    "id": 2,
                    "nome": "aluno 1",
                    "cpf": "111.111.111-11",
                    "ano_escolar": "1° Ano"
                },
                {
                    "id": 3,
                    "nome": "aluno 3",
                    "cpf": "555.555.555-55",
                    "ano_escolar": "1° Ano"
                }
                ],
                "professores": [
                {
                    "id": 1,
                    "nome": "professor 1",
                    "cpf": "333.333.333-33",
                    "materia": "Matemática"
                },
                {
                    "id": 2,
                    "nome": "professor 2",
                    "cpf": "444.444.444-44",
                    "materia": "Português"
                }
            ]
        },
        ...
    ]
    ```

## Autor
| [<img src="https://avatars.githubusercontent.com/u/83929403?v=4" width=120><br><sub>@clcostaf</sub>](https://github.com/clcosta) |
| :---: |
