import logging
import pandas as pd
def save_csv(data: pd.DataFrame, file_path: str):
    """Saves a DataFrame to a CSV file"""
    try:
        if not data.empty:
            data.to_csv(file_path, index=False)
            logging.info(f"Report saved Successfully: {file_path}")
        else:
            logging.warning(f"No data to save for {file_path}")
    except Exception as e:
        logging.error(f"ERR006: Error saving CSV file {file_path} - {e}")