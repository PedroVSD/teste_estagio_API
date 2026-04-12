from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models, schemas, operacoes, cash_back
from database import SessionLocal, engine

# 1. Cria as tabelas no banco
models.Base.metadata.create_all(bind=engine)

# 2. Inicializa a API
app = FastAPI(title="Sistema de Cashback")

# 3. Configura o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Libera a pasta "static" (onde estão seu CSS e JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 5. Função injetora de dependência (Garante que cada requisição tenha sua própria sessão no banco)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#ROTAS DA API

@app.get("/")
def exibir_site():
    return FileResponse("templates/index.html")


@app.post("/calcular")
def calcular(consulta: schemas.ConsultaCashBack, request: Request, db: Session = Depends(get_db)):
    ip_usuario = request.client.host

    # Na rota /calcular:
    cashback_gerado = cash_back.calcular_cash_back(consulta.valor_compra, consulta.cliente)
    operacoes.criar_registro_historico(db, consulta, ip_usuario, cashback_gerado)

    # Na rota /historico:
    registros = operacoes.buscar_historico_por_ip(db, ip_usuario)

    return {"cashback": cashback_gerado}

# Rota para buscar o histórico (GET)
@app.get("/historico", response_model=List[schemas.HistoricoResponse])
def historico(request: Request, db: Session = Depends(get_db)):
    ip_usuario = request.client.host

    # Manda o operário buscar as linhas desse IP no banco
    registros = operacoes.buscar_historico_por_ip(db, ip_usuario)

    return registros

#haduken
