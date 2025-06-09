import os
from .readers.csv_reader import CSVReader
from .readers.json_reader import JSONReader
from .validators.validator import Validator
from .database.db_connector import init_db, Session
from .models.archivo_modelo import ArchivoCSV, ArchivoJSON

def cargar_archivos():
    init_db()
    session = Session()
    carpeta = os.path.join(os.path.dirname(__file__), "files")

    for archivo in os.listdir(carpeta):
        path = os.path.join(carpeta, archivo)

        if archivo.endswith(".csv"):
            reader = CSVReader(path)
            model_class = ArchivoCSV
        elif archivo.endswith(".json"):
            reader = JSONReader(path)
            model_class = ArchivoJSON
        else:
            print(f"[!] Formato no soportado: {archivo}")
            continue

        try:
            datos = reader.leer_datos()
            validador = Validator(datos)
            datos_limpios = validador.validar()

            for fila in datos_limpios:
                registro = model_class(**fila)
                session.add(registro)

            session.commit()
            print(f"[✔] {archivo} cargado correctamente.")
        except Exception as e:
            print(f"[✘] Falló la carga de {archivo}: {e}")
            session.rollback()

if __name__ == "__main__":
    cargar_archivos()