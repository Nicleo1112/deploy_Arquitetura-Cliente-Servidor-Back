# API Livraria - Back-end (Exercício 8.4)

Este repositório contém a API Back-end do sistema de livraria, desenvolvida em Python com Flask.
O projeto implementa a Arquitetura Cliente-Servidor, separando completamente as responsabilidades
da Interface (Front-end) das regras de negócio e persistência de dados (Back-end).

> **Aviso:** Este é apenas o repositório do Back-end. O Cliente (Front-end independente construído
> com HTML/JS) está em um repositório separado e deve ser acessado pelo link abaixo.

---

## Links

| | URL |
|---|---|
| 🌐 Front-end | https://nicleo1112.github.io/Arquitetura-Cliente-Servidor-Front-end |
| ⚙️ Back-end | https://livraria-api-btc4e6eucreuctae.eastus-01.azurewebsites.net |

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask:** Microframework para criação da API REST.
- **Flask-CORS:** Permite requisições Cross-Origin vindas do Front-end independente.
- **Manipulação de TXT:** Persistência de dados utilizando arquivos de texto para simular um banco de dados.
- A API retorna exclusivamente dados em formato **JSON**.

---

## Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está online |
| GET | `/api/livros` | Retorna a lista de livros (suporta filtros por query params) |
| POST | `/api/livros` | Adiciona um novo livro ao catálogo |
| DELETE | `/api/livros/<titulo>` | Remove um livro pelo título |

### Filtros disponíveis em `GET /api/livros`

| Parâmetro | Tipo | Descrição |
|---|---|---|
| `titulo` | string | Filtra livros que contenham o valor no título |
| `autor` | string | Filtra livros que contenham o valor no autor |
| `ano_min` | int | Ano mínimo de publicação |
| `ano_max` | int | Ano máximo de publicação |

Exemplo: `GET /api/livros?titulo=Harry&ano_min=1990&ano_max=2000`

### Body esperado em `POST /api/livros`

```json
{
  "titulo": "Nome do Livro",
  "autor": "Nome do Autor",
  "ano": 2024
}
```

---

## Função de Teste

O arquivo `test_api.py` testa todas as rotas da API em produção. Para executar:

```bash
python test_api.py
```

Resultado esperado:

```
🔍 Testando API...

✅ Status: API Livraria online ✅
✅ Listar: 30 livros retornados
✅ Filtro por título: 2 livros encontrados
✅ Adicionar: Livro adicionado com sucesso.
✅ Remover: Livro removido com sucesso.

✅ Todos os testes passaram!
```

---

## Estrutura do Projeto

```
deploy_Arquitetura-Cliente-Servidor-Back/
├── .github/
│   └── workflows/
│       └── main_livraria-api.yml   # CI/CD para Azure App Service
├── entities/
│   ├── livro.py                    # Entidade pura
│   └── livro_repository_interface.py  # Interface abstrata (DIP)
├── infra/
│   └── txt_livro_repository.py     # Persistência em TXT
├── interface/
│   └── livro_controller.py         # Rotas da API
├── use_cases/
│   └── livro_use_cases.py          # Regras de negócio
├── .gitignore
├── README.md
├── app.py                          # Inicialização do Flask
├── livros.txt                      # Arquivo de dados
├── requirements.txt                # Dependências
└── test_api.py                     # Testes da API em produção
```

---

## Deploy (Azure App Service)

O deploy é feito automaticamente via GitHub Actions a cada push na branch `main`.

Startup command configurado:
```
gunicorn --bind=0.0.0.0:8000 app:app
```
