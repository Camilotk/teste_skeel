# API
Foi construido uma Web API utilizando o djangorestframewok para que os dados sejam enviados e trabalhados em JSON. Para utilizá-la por meio do **Postman** - _testado e funcionando_ - ou acesso do servidor basta enviar o post para o endereço da função desejada.

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

| Link                                           |Método | O que faz?                                            |
|------------------------------------------------|-------|-------------------------------------------------------|
| http://127.0.0.1:8000/api/vagas/nova/          | POST  |Cria nova vaga de trabalho                             |
| http://127.0.0.1:8000/api/vagas/lista/         | GET   |Recebe JSON paginado com todas as vagas cadastradas    |
| http://127.0.0.1:8000/api/vagas/lista/(id)/    | POST  |Recebe JSON com os atributos da vaga consultrada       |
| http://127.0.0.1:8000/api/vagas/edita/(id)/    | POST  |Edita vaga de trabalho                                 |
| http://127.0.0.1:8000/api/vagas/apaga/(id)/    | POST  |Apaga vaga de trabalho                                 |
| http://127.0.0.1:8000/api/empresas/nova/       | POST  |Cria nova empresa                                      |
| http://127.0.0.1:8000/api/empresas/lista/      | GET   |Recebe JSON paginado com todas as empresas cadastradas |
| http://127.0.0.1:8000/api/empresas/lista/(id)/ | POST  |Recebe JSON com os atributos da empresa consultrada    |
| http://127.0.0.1:8000/api/empresas/edita/(id)/ | POST  |Edita empresa                                          |
| http://127.0.0.1:8000/api/empresas/apaga/(id)/ | POST  |Apaga empresa                                          |

