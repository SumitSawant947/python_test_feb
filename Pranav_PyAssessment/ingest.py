# Data Ingestion Module: Reads sensor data and threshold data from CSV files.

import pandas as pd

def load_data(sensor_data_path, thresholds_path):
    try:
        sensor_data = pd.read_csv(sensor_data_path)
        sensor_data['date'] = pd.to_datetime(sensor_data['date'], errors='coerce')
        sensor_data['date'] = pd.to_datetime(sensor_data['date'], format='%d-%m-%Y %H:%M')
        
        thresholds = pd.read_csv(thresholds_path)
        
        return sensor_data, thresholds
    except Exception as e:
        print(f"Error while loading data: {e}")
        return None, None
