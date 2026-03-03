import boto3
import pandas as pd
from io import StringIO, BytesIO
from botocore.exceptions import ClientError

s3 = boto3.client("s3")



def list_files(bucket: str, prefix: str, extension: str) -> list[str]:
    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

        return [
            obj['Key']
            for obj in response.get('Contents', [])
            if obj['Key'].endswith(extension)
        ]
    
    except ClientError as e:
        print(f'Error listing files: {e}')
        return []
    

# Read files (.csv) from S3 ----------------------------

def read_csv_from_s3 (bucket: str, key: str) -> pd.DataFrame | None:
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        csv_bytes = response['Body'].read()
        return pd.read_csv(StringIO(csv_bytes.decode('utf-8')))

    except ClientError as e:
        print(f'Error reading {key}: {e}') 
        return None


# Save to another format (.parquet) to S3 ----------------------------

def write_parquet_to_s3(df: pd.DataFrame, bucket: str, key: str) -> None:
    try:
        buffer = BytesIO()
        df.to_parquet(buffer, index=False)
        buffer.seek(0)

        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=buffer.getvalue()
        )
    
    except ClientError as e:
        print(f'Error writing {key}: {e}')