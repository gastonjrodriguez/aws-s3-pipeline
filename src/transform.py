import pandas as pd

# TRANSFORM ----------------------------

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    return df