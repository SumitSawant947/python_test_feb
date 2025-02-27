
import pandas as pd
import numpy as np

def detect_outliers(sensor_data, thresholds_data):
    # merge both data
    merged_data = pd.merge(sensor_data, thresholds_data, on='sensor_type', how='left')

    if merged_data['min_threshold'].isnull().any() or merged_data['max_threshold'].isnull().any():
        print("Warning: Some sensor types have missing thresholds.")

    # Identify outliers based on min and max thresholds
    outliers = merged_data[
        (merged_data['value'] < merged_data['min_threshold']) | 
        (merged_data['value'] > merged_data['max_threshold'])
    ]
    
    outliers['threshold_exceeded'] = np.where(outliers['value'] < outliers['min_threshold'], 'Min', 'Max')
    
    # Select relevant columns for outliers
    outliers = outliers[['date', 'sensor_type', 'value', 'unit', 'location_id', 'threshold_exceeded']]
    
    return outliers
