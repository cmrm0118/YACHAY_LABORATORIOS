from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from runner.notebook_runner import ejecutar_notebooks
from runner.difuntos_runner import ejecutar_difuntos

app = FastAPI()

class NotebookBatchRequest(BaseModel):
    notebooks: List[str]                # rutas relativas
    parameters: Dict = {}               # parámetros opcionales

@app.post("/run-notebooks/")
def run_multiple(req: NotebookBatchRequest):
    resultados = ejecutar_notebooks(req.notebooks, req.parameters)
    return {"resultados": resultados}

@app.post("/process-difuntos/")
def process_difuntos_endpoint():
    try:
        resultados = ejecutar_difuntos()
        return {"resultados": resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando difuntos: {str(e)}")
