# estudos-django
Repositório de estudos para o projeto do Tabelionato

## Pré-requisitos
> Sempre utilize um um ambiente virtual isolado ([`venv`](https://pypi.org/project/virtualenv/)) para garantir a compatibilidade de versão em projetos distintos.

Todas as bibliotecas necessárias estão listadas no arquivo _requirementes.txt_, e podem ser instaladas utilizando o [`pip`](https://pip.pypa.io/):
```bash
python3 -m pip install -r requirementes.txt
```
ou
```bash
pip3 install -r requirementes.txt
```

## Começando com o Django
Crie o superusuário do servidor Django
```bash
python3 manage.py createsuperuser
```

Faça a migração do projeto, para identificar as alterações e criar e aplicar o banco de dados
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Inicie o servidor django
```bash
python3 manage.py runserver
```
O servidor roda por padrão em `127.0.0.1:8000`

