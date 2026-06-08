from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from database import get_table
import uuid

app = FastAPI(
    title="API de Ingestão de Dados",
    description="Sprint 01 — Diário de um Dev Jr",
    version="0.1.0"
)

class DadoEntrada(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do dado")
    valor: float = Field(..., description="Valor numérico")
    categoria: str = Field(default="geral", description="Categoria do dado")

@app.get("/")
def raiz():
    return {"mensagem": "API no ar!", "sprint": 1}

@app.post("/dados", status_code=201)
def criar_dado(dado: DadoEntrada):
    tabela = get_table()

    item = {
        "id": str(uuid.uuid4()),
        "nome": dado.nome,
        "valor": str(dado.valor),  # DynamoDB não aceita float nativo
        "categoria": dado.categoria,
        "criado_em": datetime.now().isoformat()
    }

    tabela.put_item(Item=item)

    return {"mensagem": "Dado salvo com sucesso", "id": item["id"]}

@app.get("/dados/{item_id}")
def buscar_dado(item_id: str):
    tabela = get_table()

    resposta = tabela.get_item(Key={"id": item_id})
    item = resposta.get("Item")

    if not item:
        raise HTTPException(status_code=404, detail="Dado não encontrado")

    return item