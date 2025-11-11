readme_content = """
# 🧠 Microservicio de Ejecución de Notebooks ETL

Este microservicio permite ejecutar notebooks Jupyter (.ipynb) de manera controlada mediante una API REST desarrollada con FastAPI. 
Está diseñado para lanzar procesos ETL que residen en carpetas organizadas (como `Landing-Bronze`, `Bronze-Silver`) y requieren ejecución secuencial.

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


## El servidor minIO debe estar activo
con los buckets: yachay-landing, yachay-bronze, yachay-golden
y API en puerto 9000

En yachay-landing cuando las fuentes de datos sean cargadas se debe tomar en cuenta las siguientes consideraciones:
LABORATORIOS:
El archivo a procesar debe estar en la ruta /Laboratorios/carpeta_laboratorio/nombre_archivo
el nombre del archivo y su ruta deben ingresarse en los notebooks a ejecutar
DEFUNCIONES:
El archivo a procesar debe estar en la ruta /difuntos/nombre_archivo
Como la estrucutura de los archivos es unica, el script lee todos los archivos dentro de la ruta a la vez



## La conexión a la base de datos PostgreSQL debe estar activa

## Se debe crear la carpeta output dentro de la carpeta notebooks_etl

## EJECUCIÓN DE Microservicio
python -m uvicorn main:app --reload
Esto levantará el servidor en:
http://127.0.0.1:8000/docs

### CUERPO DEL JSON PARA EXTRACCION DE DATOS
{
  "notebooks": [
    "./notebooks_etl/Landing-Bronze/Landing-bronze-Citopat.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Fernando Sanzon.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Jimenez Ipiales.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Jimenez Pasto.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Monica Arcos.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio San Pedro.ipynb",

    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio HU Departamental.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio Patologos Asociados.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-laboratorio UD Hemato Oncologos.ipynb",
    "./notebooks_etl/Landing-Bronze/Landing-bronze-SYNLAB.ipynb.ipynb",
    
    "./notebooks_etl/Bronze-Silver/Bronze-silver-Citopat.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio FSanzon.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio Jimenez.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio Monica Arcos.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio San Pedro.ipynb",
    
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio HU Departamental.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio Patologos Asociados.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-laboratorio UD Hemato Oncologos.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-SYNLAB.ipynb"

  ]
}

## CUERPO DEL JSON PARA INTEGRACION A GOLDEN
{
  "notebooks": [
    "./notebooks_etl/Silver-golden/Silver-golden.ipynb",

  ]
}

## DIFUNTOS
para ejecutar la extracción de datos del reporte de difuntos solo se da la orden desde la API y realizará un recorrido por los archivos dentro de la ruta del bucket
 
## CUERPO DEL JSON PARA PROCESO DE LIMPIEZA
{
  "notebooks": [
    "./notebooks_etl/Bronze-Silver/Bronze-silver-Unique.ipynb",
    "./notebooks_etl/Bronze-Silver/Bronze-silver-Unique-difuntos.ipynb",
  ]
}


