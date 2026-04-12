# Cashback Analysis API

Um sistema fullstack para cálculo de cashback com regras de negócio personalizadas, registro por IP e histórico de consultas em tempo real.

Este projeto foi desenvolvido como um teste técnico para [Nome da Empresa/Vaga], focado em demonstrar habilidades em Data Engineering, MLOps e desenvolvimento Web moderno.

## Tecnologias Utilizadas

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.14)
* **Gerenciamento de Pacotes:** [uv](https://github.com/astral-sh/uv)
* **Banco de Dados:** [PostgreSQL](https://www.postgresql.org/)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **Frontend:** HTML5, CSS3 e JavaScript Puro (Vanilla JS)
* **Containerização:** Docker & Docker Compose

## Regras de Cashback

O sistema aplica as seguintes regras de cálculo:
1.  **Base:** 5% do valor da compra.
2.  **Bônus VIP:** Clientes do tipo "VIP" recebem um acréscimo de 10% sobre o valor do cashback base.
3.  **Promoção de Valor:** Compras acima de **R$ 500,00** têm o cashback final dobrado.

## Arquitetura do Projeto

O projeto segue uma estrutura modular para facilitar a manutenção e escalabilidade:

* `main.py`: Ponto de entrada da API e definição das rotas.
* `cash_back.py`: Lógica de negócio isolada (Cálculo de cashback).
* `database.py`: Configurações de conexão com o PostgreSQL.
* `models.py`: Definição das tabelas do banco de dados (SQLAlchemy).
* `schemas.py`: Modelos de validação de dados (Pydantic).
* `operacoes.py`: Camada de persistência (CRUD).
* `/static`: Frontend estático da aplicação.

## ⚙️ Como Executar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados.
* Python 3.14+ (opcional se usar apenas Docker).

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/API_teste_estagio.git
   cd API_teste_estagio

2. **Subir o Banco de Dados (Docker):**
   ```bash
   docker compose up -d

3. **Configurar o ambiente Python (com uv):**
    ```bash
    uv venv
    source .venv/bin/activate  # No Linux
    uv pip install -r requirements.txt

4. **Rodar a API:**
    ```Bash
    uvicorn main:app --reload

5. **Acesse o sistema:**
Abra o seu navegador em http://127.0.0.1:8000/static/index.html

Caso não funcione, a fastAPI gera um link no seu terminal

# Endpoints da API
POST /calcular: Recebe cliente e valor_compra, retorna o cashback e salva no banco.

GET /historico: Retorna todas as consultas feitas pelo IP do usuário atual.