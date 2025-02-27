import pandas as pd
import logging
def detect_outliers(sensor_data: pd.DataFrame, thresholds: pd.DataFrame) -> pd.DataFrame:
    """Identifies sensor readings that exceed predefined threshols with exeception handling ."""
    try:
        if sensor_data.empty or thresholds.empty:
            return pd.DataFrame
    
        merged = pd.merge(sensor_data, thresholds, on='sensor_type', how='left')
        merged['threshold_exceeded'] = ((merged['value'] < merged['min_threshold']) | 
                                        (merged['value'] > merged['max_threshold']))
        outliers = merged[merged['threshold_exceeded']]
        return outliers[['date', 'sensor_type', 'value', 'unit', 'location_id', 'threshold_exceeded']]
    except Exception as e:
        logging.error(f"Error detecting outliers - {e}")
        return pd.DataFrame()