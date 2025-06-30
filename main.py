from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from runner.notebook_runner import ejecutar_notebooks

app = FastAPI()

class NotebookBatchRequest(BaseModel):
    notebooks: List[str]                # rutas relativas
    parameters: Dict = {}               # parámetros opcionales

@app.post("/run-notebooks/")
def run_multiple(req: NotebookBatchRequest):
    resultados = ejecutar_notebooks(req.notebooks, req.parameters)
    return {"resultados": resultados}
