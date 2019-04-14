# Skeel Teste Full Stack
Em abril de 2019 a empresa Skeel entrou em contato comigo para saber se eu gostaria de me candidatar a uma vaga na Startup deles.

O teste requeria que: fosse construido um CRUD com as tabelas Vagas, Empresas e Benefícios.

# Servidor Utilizado:
- Ubuntu 18.10 com os pacotes:
    - python-dev python3-dev
    - libmysqlclient-dev
- Anaconda Virtualenv 4.6 com:
    - Django 2.2
    - Python 3.7

# Dependencias:
- djangorestframework
- mysqlclient
- pycpfcnpj
- drf-writable-nested

# Configuração
- Criar um DB Mysql/Mariadb com qualquer nome e configurar o nome da DB, user e senha nas settings
- Criar um super usuário

# API
Foi construido uma Web API utilizando o djangorestframewok para que os dados sejam enviados e trabalhados em JSON. Para utilizá-la por meio do Postman ou acesso do servidor basta enviar o post para o endereço da função desejada.
* modelo de requisição para nova empresa
```
{
    "name": "Nome",
    "cnpj": "CNPJ válido com ou sem pontuação",
    "description": "Descrição",
    "location_city": "Cidade/UF",
    "email": "E-mail"
}
```

* modelo de requisição para nova vaga
```
{
    "title": "Nome",
    "description": "Descrição",
    "initial_salary": 0,
    "final_salary": 9999,
    "contract_type": "CLT ou PJ",
    "company": 0,
    "requirements_job": [
        {
            "description": "Requisito 1"
        },
        {
            "description": "Requisito 2"
        }
    ],
    "benefits_job": [
        {
            "description": "Beneficio 1"
        },
        {
            "description": "Beneficio 2"
        }
    ]
}
```
* para editar um beneficio da vaga é preciso usar id como em "Beneficio 2", toda a API está tratada contra valores 0

| Link                                          | O que faz?                                             |
|-----------------------------------------------|--------------------------------------------------------|
| http://127.0.0.1:8000/api/vagas/nova/         | Cria nova vaga de trabalho                             |
| http://127.0.0.1:8000/api/vagas/lista/        | Recebe JSON paginado com todas as vagas cadastradas    |
| http://127.0.0.1:8000/api/vagas/lista/(id)/   | Recebe JSON com os atributos da vaga consultrada       |
| http://127.0.0.1:8000/api/vagas/edita/(id)/   | Edita vaga de trabalho                                 |
| http://127.0.0.1:8000/api/vagas/apaga/(id)/   | Apaga vaga de trabalho                                 |
| http://127.0.0.1:8000/api/empresas/nova/       | Cria nova empresa                                      |
| http://127.0.0.1:8000/api/empresas/lista/      | Recebe JSON paginado com todas as empresas cadastradas |
| http://127.0.0.1:8000/api/empresas/lista/(id)/ | Recebe JSON com os atributos da empresa consultrada    |
| http://127.0.0.1:8000/api/empresas/edita/(id)/ | Edita empresa                                          |
| http://127.0.0.1:8000/api/empresas/apaga/(id)/ | Apaga empresa                                          |
