# Teste realizado para a empresa AWTech

- Instalar dependências e Utilizar com Poetry


- Referências:

[Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/#objectives)

[FastAPI do Zero - Dunossauro](https://fastapidozero.dunossauro.com/)

- Comandos:

```
[tool.taskipy.tasks]
lint = 'ruff check .; ruff check . --diff'
format = 'ruff check . --fix; ruff format .'
run = 'fastapi dev fast_zero/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
```
