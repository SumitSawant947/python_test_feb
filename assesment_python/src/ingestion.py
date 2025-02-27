import pandas as pd
import os
import logging

def read_csv(file_path: str) -> pd.DataFrame:
    """Reads a CSV file into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        logging.error(f"ERR001: File not found - {file_path}")
        return pd.DataFrame()
    try:
        return pd.read_csv(file_path)
    except pd.errors.ParserError as e:
        logging.error(f"ERR002: Invalid data format in {file_path} - {e}")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"ERR003: Unexpected error reading {file_path} - {e}")
        return pd.DataFrame()