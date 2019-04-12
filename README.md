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

| Link                                          | O que faz?                                             |
|-----------------------------------------------|--------------------------------------------------------|
| http://127.0.0.1:8000/api/vagas/nova/         | Cria nova vaga de trabalho                             |
| http://127.0.0.1:8000/api/vagas/lista/        | Recebe JSON paginado com todas as vagas cadastradas    |
| http://127.0.0.1:8000/api/vagas/lista/(id)/   | Recebe JSON com os atributos da vaga consultrada       |
| http://127.0.0.1:8000/api/vagas/edita/(id)/   | Edita vaga de trabalho                                 |
| http://127.0.0.1:8000/api/vagas/apaga/(id)/   | Apaga vaga de trabalho                                 |
| http://127.0.0.1:8000/api/empresa/nova/       | Cria nova empresa                                      |
| http://127.0.0.1:8000/api/empresa/lista/      | Recebe JSON paginado com todas as empresas cadastradas |
| http://127.0.0.1:8000/api/empresa/lista/(id)/ | Recebe JSON com os atributos da empresa consultrada    |
