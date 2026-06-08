from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime

app = FastAPI(
    title="API de Ingestão de Dados",
    description="Sprint 01 — Diário de um Dev Jr",
    version="0.1.0"
)

# --- Modelo Pydantic ---
# Definindo o "contrato" dos dados que a API aceita
class DadoEntrada(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do dado")
    valor: float = Field(..., description="Valor numérico")
    categoria: str = Field(default="geral", description="Categoria do dado")

# --- GET raiz ---
@app.get("/")
def raiz():
    return {"mensagem": "API no ar!", "sprint": 1}

# --- GET com path parameter ---
@app.get("/dados/{item_id}")
def buscar_dado(item_id: int):
    return {
        "id": item_id,
        "descricao": f"Dado de número {item_id}",
        "status": "encontrado"
    }

# --- POST com validação Pydantic ---
@app.post("/dados", status_code=201)
def criar_dado(dado: DadoEntrada):
    return {
        "mensagem": "Dado recebido com sucesso",
        "recebido": dado,
        "criado_em": datetime.now().isoformat()
    }