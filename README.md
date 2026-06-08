# Sprint 01 — API de Ingestão de Dados

Projeto desenvolvido como parte do Diário de um Dev Jr em recolocação.

## Objetivo
API REST construída com FastAPI e DynamoDB como exercício prático de
desenvolvimento back-end e integração com AWS.

## Tecnologias
- Python 3.x
- FastAPI
- AWS DynamoDB (boto3)
- Uvicorn
- pytest

## Como rodar localmente

```bash
# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
uvicorn main:app --reload
```

## Endpoints

|
 Método 
|
 Rota 
|
 Descrição 
|
|
--------
|
------
|
-----------
|
|
 GET 
|
 / 
|
 Health check 
|
|
 GET 
|
 /dados/{item_id} 
|
 Busca dado por ID 
|
|
 POST 
|
 /dados 
|
 Cria novo dado 
|

## Status
🚧 Em desenvolvimento — Sprint 01 (01/06 a 15/06)