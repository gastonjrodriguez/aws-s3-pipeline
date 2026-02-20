import os
from dotenv import load_dotenv

load_dotenv()

BUCKET = os.getenv("AWS_BUCKET")
RAW_PREFIX = os.getenv("RAW_PREFIX", "raw/")
PROCESSED_PREFIX = os.getenv("PROCESSED_PREFIX", "processed/")

