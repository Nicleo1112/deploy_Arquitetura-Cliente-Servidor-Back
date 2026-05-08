# API Livraria - Back-end (Exercício 8.3)

Este repositório contém a API Back-end do sistema de livraria, desenvolvida em Python com Flask.
O projeto foi refatorado para implementar a Arquitetura Cliente-Servidor, separando completamente
as responsabilidades da Interface (Front-end) das regras de negócio e persistência de dados (Back-end).

> **Aviso:** Este é apenas o repositório do Back-end. O Cliente (Front-end independente construído
> com HTML/JS) deve ser executado separadamente para consumir esta API.

---

## Tecnologias Utilizadas

- **Python 3.11**
- **Flask:** Microframework para criação da API REST.
- **Flask-CORS:** Biblioteca utilizada para permitir as requisições (Cross-Origin) vindas do Front-end independente.
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

## Como executar localmente

### Pré-requisitos

- Python 3.11+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/livraria-api.git
cd livraria-api

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```

### Rodando localmente

```bash
python app.py
```

API disponível em: `http://127.0.0.1:5000`

> Na primeira execução, o arquivo `livros.txt` é criado automaticamente com 30 livros pré-cadastrados.

---

## Persistência de Dados

Os dados são armazenados em `livros.txt` na raiz do projeto no formato:

```
Titulo|Autor|Ano
Harry Potter e a Pedra Filosofal|J.K Rowling|1997
O Hobbit|Tolkien|1937
```

---

## Deploy na Azure (App Service)

O deploy é feito automaticamente via GitHub Actions a cada push na branch `main`.

Para configurar manualmente:

```bash
az login
az webapp up --name livraria-api --runtime "PYTHON:3.11" --sku B1
az webapp config set --name livraria-api --startup-file "gunicorn --bind=0.0.0.0:8000 app:app"
az webapp config appsettings set --name livraria-api --settings WEBSITES_ENABLE_APP_SERVICE_STORAGE=true
```

API disponível em: `https://livraria-api.azurewebsites.net`

---

## Estrutura do Projeto

```
livraria-api/
├── .github/
│   └── workflows/
│       └── azure-deploy.yml    # CI/CD para Azure App Service
├── entities/
│   ├── livro.py                # Entidade pura
│   └── livro_repository_interface.py  # Interface abstrata (DIP)
├── infra/
│   └── txt_livro_repository.py # Persistência em TXT
├── interface/
│   └── livro_controller.py     # Rotas da API
├── use_cases/
│   └── livro_use_cases.py      # Regras de negócio
├── .gitignore
├── README.md
├── app.py                      # Inicialização do Flask
├── livros.txt                  # Arquivo de dados
└── requirements.txt            # Dependências
```
