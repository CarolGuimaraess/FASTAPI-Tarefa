from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool

# Banco de dados temporário para armazenar as tarefas
db: Dict[int, Tarefa] = {}

id_tarefa = 1

@app.get("/tarefas/", response_model=List[Tarefa])
def obter_tarefas():
    return list(db.values())

@app.post("/tarefas/", response_model=Tarefa)
def adicionar_tarefa(tarefa: Tarefa):
    if not tarefa.titulo or tarefa.concluida is None:
        raise HTTPException(status_code=400, detail="O título e o status de conclusão são obrigatórios")
    
    global id_tarefa
    tarefa.id = id_tarefa
    db[id_tarefa] = tarefa
    id_tarefa += 1
    return tarefa

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def editar_tarefa(tarefa_id: int, tarefa: Tarefa):
    if tarefa_id not in db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa_antiga = db[tarefa_id]
    tarefa.id = tarefa_antiga.id
    db[tarefa_id] = tarefa
    return tarefa

@app.delete("/tarefas/{tarefa_id}")
def excluir_tarefa(tarefa_id: int):
    if tarefa_id not in db:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del db[tarefa_id]
    return {"mensagem": "Tarefa excluída"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
