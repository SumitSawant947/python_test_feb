# Outlier Detection Module: Identifies outliers based on threshold values.

import pandas as pd

def detect_outliers(sensor_data, thresholds):
    merged_data = pd.merge(sensor_data, thresholds, on='sensor_type', how='left')
    outliers = []
    
    for index, row in merged_data.iterrows():
        if pd.isnull(row['min_threshold']) or pd.isnull(row['max_threshold']):
            continue
        
        if row['value'] < row['min_threshold'] or row['value'] > row['max_threshold']:
            outliers.append({
                'date': row['date'],
                'sensor_type': row['sensor_type'],
                'value': row['value'],
                'unit': row['unit'],
                'location_id': row['location_id'],
                'threshold_exceeded': f"min_threshold: {row['min_threshold']}, max_threshold: {row['max_threshold']}"
            })
    
    return pd.DataFrame(outliers)
