import pandas as pd

# TRANSFORMAR ----------------------------

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    return df