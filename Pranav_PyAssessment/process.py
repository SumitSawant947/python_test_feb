# Processing Module: Calculates monthly averages, maximum, and minimum values for each sensor.

def calculate_monthly_statistics(sensor_data):
    monthly_stats = sensor_data.groupby(['sensor_type', 'month'])['value'].agg(['mean', 'max', 'min']).reset_index()
    monthly_stats.columns = ['sensor_type', 'month', 'avg_value', 'max_value', 'min_value']
    return monthly_stats
