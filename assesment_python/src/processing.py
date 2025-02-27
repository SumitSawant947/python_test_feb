import logging
import pandas as pd
def calculate_monthly_statistics(sensor_data: pd.DataFrame) -> pd.DataFrame:
    
    try:
        if sensor_data.empty:
            return pd.DataFrame()
        
        sensor_data['date'] = pd.to_datetime(sensor_data['date'], errors='coerce')
        sensor_data.dropna(subset=['date'], inplace=True)
        sensor_data['month'] = sensor_data['date'].dt.to_period('M')
        
        stats = (sensor_data.groupby(['sensor_type', 'month'])
                 .agg(avg_value=('value', 'mean'),
                      max_value=('value', 'max'),
                      min_value=('value', 'min'))
                 .reset_index())
        return stats
    except Exception as e:
        logging.error(f"ERR004: Error processing monthly stastics - {e}")
        return pd.DataFrame()