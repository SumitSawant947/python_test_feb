import pandas as pd
 
def calculate_monthly_stats(sensor_data):
    # To check required columns
    if not all(col in sensor_data.columns for col in ['sensor_type', 'month', 'value']):
        print("Error: Missing required columns in sensor data.")
        return pd.DataFrame()
 
    # calculating stats
    stats = sensor_data.groupby(['sensor_type', 'month'])['value'].agg(['mean', 'max', 'min']).reset_index()
    stats.columns = ['sensor_type', 'month', 'avg_value', 'max_value', 'min_value']
   
    return stats
 