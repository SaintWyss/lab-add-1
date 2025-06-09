# Aplicación de Carga de Archivos con POO en Python

## Estructura del Proyecto

Este proyecto consiste en una aplicación modular desarrollada en Python que permite cargar archivos de diferentes formatos, validarlos y almacenarlos en una base de datos relacional utilizando SQLAlchemy. A continuación, se detalla la estructura de carpetas y archivos del proyecto, junto con su funcionalidad.

### 1. `main.py` - Punto de entrada de la aplicación

Archivo principal que se ejecuta con `python -m data_loader_app.main`. Esto es necesario porque los imports son relativos al paquete. Realiza las siguientes acciones:

- Inicializa la base de datos.
- Escanea los archivos en el directorio `files/`.
- Determina qué clase de lector utilizar (`CSVReader`, `JSONReader`, etc.).
- Llama al validador para limpiar los datos.
- Crea objetos de los modelos (uno por fila).
- Guarda los datos en la base de datos.

Este archivo conecta todos los componentes: lectura → validación → almacenamiento.

### 2. `files/` - Carpeta de archivos de datos

Contiene los archivos a cargar en la base de datos. Ejemplos:
- `clientes.csv`
- `productos.json`

### 3. `models/` - Modelos de base de datos

- `base_model.py`: Define una clase base abstracta con `declarative_base()` de SQLAlchemy.
- `archivo_modelo.py`: Define dos modelos:
  - `ArchivoCSV`: tabla para datos de archivos CSV.
  - `ArchivoJSON`: tabla para datos de archivos JSON.

Cada clase representa una tabla con campos personalizables como `id`, `nombre`, `valor`, etc.

### 4. `readers/` - Lectores de archivos

- `base_reader.py`: Clase abstracta `BaseReader` que define el método `leer_datos()`.
- `csv_reader.py`: Hereda de `BaseReader`, implementa lectura con `pandas.read_csv()`.
- `json_reader.py`: Hereda de `BaseReader`, implementa lectura con `pandas.read_json()`.

Ambas clases aplican polimorfismo, redefiniendo el método `leer_datos()` según el formato.

### 5. `validators/validator.py` - Limpieza y validación de datos

- Recibe datos en forma de lista de diccionarios.
- Los convierte a un `DataFrame`.
- Aplica validaciones:
  - Elimina valores nulos.
  - Elimina duplicados.
- Devuelve los datos limpios listos para persistencia.

### 6. `database/db_connector.py` - Conexión a base de datos

- Crea un `engine` de SQLAlchemy conectado a `archivos.db`.
- Define una `Session` para operaciones con la base.
- Implementa `init_db()` que crea las tablas definidas en los modelos.

Encapsula toda la lógica de conexión y creación de esquema.

### 7. `requirements.txt` - Dependencias

Contiene las librerías necesarias para ejecutar la aplicación:

```
pandas==2.2.1
openpyxl==3.1.2
sqlalchemy==2.0.30
requests==2.31.0
pyodbc==4.0.39
```

---

## Objetivo del Proyecto

Desarrollar una aplicación modular en Python que permita:

- Cargar al menos dos tipos de archivos de datos (.csv, .xlsx, .json, .txt, etc.).
- Realizar validaciones básicas:
  - Verificación de tipos de datos (número, texto, fecha).
  - Validación de campos obligatorios (no nulos).
  - Eliminación de registros duplicados.
  - Eliminación de valores nulos.
- Persistir los datos en una base de datos relacional utilizando SQLAlchemy.
- Aplicar los cuatro pilares de la Programación Orientada a Objetos (POO).
- Ejecutar la aplicación desde consola mediante una clase principal.

---

## Requisitos Técnicos

### Lenguaje y Paradigma

- Python 3.10 o superior.
- Paradigma: Programación Orientada a Objetos.

### Manejo de Archivos

- Soporte para formatos: `.csv`, `.xlsx`, `.json`, `.txt`.
- Carga automática desde el directorio `files/`.

### Validaciones Mínimas

- Verificación de tipos de datos.
- Validación de campos obligatorios.
- Eliminación de duplicados.
- Eliminación de valores nulos.

### Persistencia

- SQLAlchemy como ORM.
- Una tabla por tipo de archivo.

### Flujo de ejecución

1. Ejecutar `python -m data_loader_app.main`.
2. Escaneo automático de archivos en `files/`.
3. Validación de cada archivo.
4. Inserción en tablas correspondientes.
5. Reporte final de carga exitosa o fallida.

---

## Requisitos de Programación Orientada a Objetos

| Pilar           | Evaluación esperada                                                                    |
|-----------------|-----------------------------------------------------------------------------------------|
| Abstracción     | Separación clara entre lectura, validación y persistencia.                             |
| Encapsulamiento | Uso adecuado de atributos y métodos privados o protegidos.                             |
| Herencia        | Modelos heredan de una clase base común (`Base`).                                      |
| Polimorfismo    | Métodos especializados como `leer_csv()` y `leer_json()` implementan la misma interfaz.|

---

## Forma de Entrega

- Repositorio público en GitHub que contenga:
  - Código fuente completo.
  - Archivos de datos en `files/`.
  - Archivo `requirements.txt` para instalación de dependencias.
