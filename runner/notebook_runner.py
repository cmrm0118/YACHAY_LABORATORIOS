import papermill as pm
import os

def ejecutar_notebooks(lista_notebooks: list, parameters: dict = {}):
    resultados = []
    original_cwd = os.getcwd()  # Guarda el cwd original

    for input_path in lista_notebooks:
        nombre = os.path.basename(input_path).replace('.ipynb', '')
        output_path = f"../output/{nombre}_executed.ipynb"
        notebook_dir = os.path.dirname(os.path.abspath(input_path))

        try:
            os.chdir(notebook_dir)  # Cambiar cwd al directorio del notebook

            print(f"🚀 Ejecutando: {input_path}")
            pm.execute_notebook(
                input_path=os.path.basename(input_path),
                output_path=os.path.abspath(output_path),
                parameters=parameters,
                kernel_name='python3',
                report_mode=False,
                raise_on_error=True
            )

            resultados.append({
                "notebook": input_path,
                "status": "success"
            })

        except Exception as e:
            resultados.append({
                "notebook": input_path,
                "status": "error",
                "message": str(e)
            })
            print(f"❌ Error ejecutando {input_path}: {e}")
            break  # ← Detiene la ejecución al primer error

        finally:
            os.chdir(original_cwd)

    return resultados
