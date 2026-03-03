# S3 ETL Pipeline. CSV -> Transformacion -> Parquet

## Descripcion

Pipeline ETL en Python que lee archivos **CSV** desde un bucket de AWS S3 (`raw/`), aplica transformaciones simples y escribe el resultado en formato **Parquet** en `processed/`.

El proyecto está estructurado de forma modular para permitir ejecución batch (todos los archivos) o procesamiento puntual de archivos específicos.

## Tech stack

* Python 3.x
* boto3
* pandas
* pyarrow
* AWS S3

## Objetivo

* Leer uno o múltiples archivos CSV desde S3
* Aplicar transformaciones (ej: eliminación de duplicados)
* Guardar los datasets transformados en Parquet
* Mantener separación de responsabilidades y parametrización desde consola


## Arquitectura

```
src/
│
├── main.py            # Entry point
├── pipeline.py        # Orquestacion del pipeline
├── transform.py       # Transformaciones puras
├── input_output_s3.py # Lectura/escritura en S3
├── config.py          # Variables de entorno

.venv
requirements.txt
.gitignore
```

### Principios aplicados

* Modularización
* SoC (Separation of Concerns)
* Funciones puras para transformaciones
* Configuración desacoplada con variables de entorno
* Ejecución parametrizable


## Requisitos

Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```

## Configuración

Crear archivo `.env` (basado en .env.example):

```
AWS_BUCKET=mi-bucket
RAW_PREFIX=raw/
PROCESSED_PREFIX=processed/
```

Las credenciales de AWS se toman desde:

* AWS CLI configurado
* Variables de entorno
* Perfil de AWS

No se almacenan en el codigo.


## Ejemplo de Uso

### Procesar todos los archivos

```bash
python src/main.py
```

Resultado:
1. Lista CSV en `raw/`
2. Lee cada archivo
3. Aplica transformaciones
4. Guarda Parquet en `processed/`

### Procesar un archivo específico

```bash
python src/main.py raw/ecommerce_orders.csv
```
Resultado:
Permite la misma ejecución, pero puntual, sin modificar código.


## Flujo estandar del pipeline

1. Listado de archivos en S3
2. Lectura CSV → DataFrame
3. Transformaciones
4. Escritura Parquet en S3
5. Logging por archivo


## Decisiones de diseño

* Separar I/O de transformaciones para facilitar testing
* Parametrizar ejecución con argumentos de consola
* Evitar hardcodear configuración
* Mantener el pipeline reusable


## Próximos pasos posibles

* Manejo de errores más robusto
* Versionado de datasets
* Dockerización


## Autor

Gaston Rodriguez