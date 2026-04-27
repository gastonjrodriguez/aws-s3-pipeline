# S3 Pipeline. CSV -> Transformacion -> Parquet

## Description

Python-based ETL pipeline that reads *CSV* files from an AWS S3 bucket (`raw/`), applies transformations, and writes the results in *Parquet* format to `processed/`.
The project is architected in a modular way to support both batch execution (processing all files) and targeted processing of specific files.

## Tech stack

* Python 3.x
* boto3
* pandas
* pyarrow
* AWS S3

## Objectives

* Read one or more CSV files from S3
* Apply transformations (e.g., deduplication)
* Save transformed datasets in Parquet format
* Maintain separation of concerns and CLI-based parameterization

## Arquitecture

```
src/
│
├── main.py            # Entry point
├── pipeline.py        # Pipeline orchestration
├── transform.py       # Pure transformations
├── input_output_s3.py # Reading/Writing to S3
├── config.py          # Environment variables

.venv
requirements.txt
.gitignore
```

### Applied principles

* Modularization
* SoC (Separation of Concerns)
* Pure functions for transformation
* Decoupled configuration using environment variables
* Customizable execution

## Requirements

Create virtual environment and install dependencies:

```
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
```

## Configuration

Create `.env` file (based in .env.example):

```
AWS_BUCKET=mi-bucket
RAW_PREFIX=raw/
PROCESSED_PREFIX=processed/
```

AWS Credentials are managed through:

* Configured AWS CLI
* Environment variables
* AWS Profiles

## Usage example

### Process all the files

```
python src/main.py
```

Flow:
1. List CSV in `raw/`
2. Read each file
3. Apply transformations
4. Save Parquet to `processed/`

### Process a specific file

```
python src/main.py raw/ecommerce_orders.csv
```
Outcome: Runs the pipeline only for the specified file without code modifications.

## Standard Pipeline Flow

1. List files in S3
2. Read CSV -> DataFrame
3. Apply Transformations
4. Write Parquet back to S3
5. Logging per file

## Design Decisions

* Separation of I/O from transformation to simplify testing.
* Configure execution with command-line arguments.
* Build pipeline to follow reusability.

## Possible next steps

* Enhanced robust error handling.
* Dataset versioning.
* Dockerization.

## Author

Gaston Rodriguez