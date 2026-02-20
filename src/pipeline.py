from config import PROCESSED_PREFIX
from input_output_s3 import list_files, read_csv_from_s3, write_parquet_to_s3
from transform import transform


def run_pipeline(bucket: str, prefix: str | None = None, files: list[str] | None = None) -> None:

    if files is not None: # en caso de querer archivos puntuales
        keys = files
    else:
        keys = list_files(bucket, prefix, '.csv')

    print(f'{len(keys)} files to process.')

    for key in keys:

        df = read_csv_from_s3(bucket, key)

        if df is None:
            continue

        df = transform(df)

        processed_key = (
            key.replace('raw/', 'processed/').replace('.csv', '.parquet')
        )

        write_parquet_to_s3(df, bucket, processed_key)

        print(f'{key} processed successfully')