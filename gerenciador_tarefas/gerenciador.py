from fastapi import FastAPI


app = FastAPI()

TAREFAS = []


@app.get("/tarefas")
def listar():
    return TAREFAS
