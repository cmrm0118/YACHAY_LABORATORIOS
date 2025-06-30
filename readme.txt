readme_content = """
# 🧠 Microservicio de Ejecución de Notebooks ETL

Este microservicio permite ejecutar notebooks Jupyter (.ipynb) de manera controlada mediante una API REST desarrollada con FastAPI. Está diseñado para lanzar procesos ETL que residen en carpetas organizadas (como `Landing-Bronze`, `Bronze-Silver`) y requieren ejecución secuencial.

---

## 🚀 Características

- Ejecuta notebooks en orden definido.
- Envía parámetros a los notebooks (como `cliente`, `fecha`, etc.).
- Detiene la ejecución si algún notebook falla.
- Usa `papermill` para controlar la ejecución.
- Soporta módulos auxiliares (`Utils.ipynb` o `Utils.py`).
- Microservicio expuesto con FastAPI y Uvicorn.

---

## 🧱 Requisitos

- Python 3.8 o superior
- pip (instalador de paquetes)
- git (opcional)

---
### nota final

en las carpetas runner y el archivo notebook runner se debe actualziar el nombre del entorno virtual donde se va a ejecutar los notebooks. Para el caso del ejemplo de creacion en entrono virtual se llama venv.
en la carpeta donde se crea el entorno virtual se debe descargar este proyecto.
los archivos integrados labs y orquestador labs quedan para manejo interno y no se ejecutan en el procesamiento del microservicio
## ⚙️ Instalación

### 1. Clona el repositorio (si aplica)


### 2. ACTIVA ENTORNO VIRTUAL
2.1 crea entrono virtual 
python -m venv venv
source venv/bin/activate
2.2 activa entorno virtual
python -m venv venv
venv\\Scripts\\activate

### INSTALACION DE DEPENDENCIAS 
pip install -r requirements.txt


## EJECUCION DE Microservicio
python -m uvicorn main:app --reload
Esto levantará el servidor en:
http://127.0.0.1:8000

### CUERPO DEL JSON PARA EXTRACCION DE DATOS
{
  "notebooks": [
    "./notebooks_etl/Landing-Bronze/Landing-bronze-Citopat.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Fernando Sanzon.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Jimenez Ipiales.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Jimenez Pasto.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Monica Arcos.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio San Pedro.ipynb",

    "./notebooks_etl/Bronze-Silver/Bronze-silver-Citopat.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio FSanzon.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio Jimenez.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio Monica Arcos.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio San Pedro.ipynb"
  ]
}

## CUERPO DEL JSOPN PARA INTEGRACION A GOLDEN
{
  "notebooks": [
    "./notebooks_etl/Silver-golden/Silver-golden.ipynb",

  ]
}



