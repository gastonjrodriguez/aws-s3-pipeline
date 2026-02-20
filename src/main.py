from config import BUCKET, RAW_PREFIX
from pipeline import run_pipeline
import sys


# ENTRY POINT ----------------------------


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        file_key = sys.argv[1]
        run_pipeline(BUCKET, RAW_PREFIX, files=[file_key])
    else:
        run_pipeline(BUCKET, RAW_PREFIX)
    
