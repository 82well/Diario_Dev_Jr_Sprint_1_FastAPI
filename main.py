from fastapi import FastAPI

# Criando a instância da aplicação
app = FastAPI(
    title="API de Ingestão de Dados",
    description="Sprint 01 — Diário de um Dev Jr",
    version="0.1.0"
)

# Endpoint raiz — só para confirmar que a API está viva
@app.get("/")
def raiz():
    return {"mensagem": "API no ar!", "sprint": 1}

# Endpoint GET para buscar um dado pelo ID
@app.get("/dados/{item_id}")
def buscar_dado(item_id: int):
    return {
        "id": item_id,
        "descricao": f"Dado de número {item_id}",
        "status": "encontrado"
    }