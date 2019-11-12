## Coding Dojo de Python/Django

## Primeira sessão

Nessa primeira etapa do coding dojo, cobrimos:

- virtualenv
    - criando um virtualenv com o comando `python -m venv venv`
- pip
    - instalando o `django` e a biblioteca `requests`
    - definindo o arquivo `requirements.txt`
- comandos pip:
    - pip freeze
    - pip list
    - pip install
    - pip install -r requirements.txt
    - pip install --upgrade
- django cli, via `python manage.py`. Vimos os comandos:
    - startproject: cria um projeto django
    - startapp: cria um app dentro do projeto
    - makemigrations: cria os arquivos de migrações caso detectado mudança nos models
    - migrate: roda as migrações pendentes
    - runserver: roda o servidor local
    - showmigrations: mostra as migrações pendentes e as que já rodaram
- migrations:
    - criamos um model Joke
    - rodamos as migrações
    - discutimos o que triga uma migração e o que não triga
- urls
    - definindo as urls do nosso app no arquivo `urls.py`
    - importando as funções das views que lidam com a requisição naquela url
- views e django orm:
    - criamos funções que processam as requisições do cliente
    - retornarmos um hello world com HttpResponse
    - utilizamos a biblioteca `requests` para bater no endpoint da api de piadas aleatórias do chuck norris http://api.icndb.com/jokes/random
    - salvamos a piada no banco via django orm e retornamos
    - fizemos uma query com o django orm que retorna todas as piadas
    - mostramos como ver uma query do django orm em sql
    - exploramos o banco sqlite3 com o comando `sqlite3 db.sqlite3`
    - adicionamos uma variável no context de uma template e renderizamos a template mostrando a lista de piadas salvas no banco
    - discutimos o conceito do que é um `endpoint`
- template engine
    - utilizando o jinja (templete engine do django) para mostrar a lista de piadas com um for
    - herança com extends e block
    - colocamos bootstrap
- separamos em pastas backend/frontend para no futuro fazer um app em react que utiliza esse django como uma api

## Segunda sessão

### GraphQL e Graphene

- Instalamos o [graphene-django](https://github.com/graphql-python/graphene-django) e configuramos no app django criado na sessão 1
- Criamos uma Query GraphQL que retorna todas as piadas e uma Mutation e pra criar uma piada nova no arquivo [`schema.py`](https://github.com/caiolopes/django-dojo/blob/master/projeto-1/backend/dojo/dojo/schema.py)
- Abordamos conceitos de GraphQL e do código, com diversos exemplos, e exploramos a interface do graphiql

### Celery

- Instalamos e configuramos o celery
- Fizemos uma task periódica que pega uma piada nova a cada 15 segundos no arquivo [`tasks.py`](https://github.com/caiolopes/django-dojo/blob/master/projeto-1/backend/dojo/core/tasks.py)


## Terceira sessão: testes e pytest

Slides: https://hackmd.io/@caiolopes/B1ZOfQvjH

- Criamos um novo projeto do zero, pra reforçar os conceitos, que tinha um model apenas: `Product`
- Criamos uma view e um endpoint para esse novo app
- Instalamos as bibliotecas `pytest pytest-django pytest-cov mixer`
- Fizemos testes pra verificar o endpoint criado nas URLs e pro model utilizando pytest
- Abordamos conceitos `fixture` e `parametrize`
