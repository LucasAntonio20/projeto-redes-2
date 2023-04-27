from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nome: str
    telefone: str

class Agendamento(BaseModel):
    id: int
    cliente_id: int
    data_hora: str
    servico: str

clientes = []
agendamentos = []

@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.post("/clientes", response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def atualizar_cliente(cliente_id: int, cliente: Cliente):
    for index, c in enumerate(clientes):
        if c.id == cliente_id:
            clientes[index] = cliente
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.delete("/clientes/{cliente_id}")
def excluir_cliente(cliente_id: int):
    for index, c in enumerate(clientes):
        if c.id == cliente_id:
            del clientes[index]
            return {"message": "Cliente excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.get("/agendamentos", response_model=List[Agendamento])
def listar_agendamentos():
    return agendamentos

@app.post("/agendamentos", response_model=Agendamento)
def adicionar_agendamento(agendamento: Agendamento):
    agendamentos.append(agendamento)
    return agendamento

@app.put("/agendamentos/{agendamento_id}", response_model=Agendamento)
def atualizar_agendamento(agendamento_id: int, agendamento: Agendamento):
    for index, a in enumerate(agendamentos):
        if a.id == agendamento_id:
            agendamentos[index] = agendamento
            return agendamento
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")

@app.delete("/agendamentos/{agendamento_id}")
def excluir_agendamento(agendamento_id: int):
    for index, a in enumerate(agendamentos):
        if a.id == agendamento_id:
            del agendamentos[index]
            return {"message": "Agendamento excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Agendamento não encontrado")