import pandas as pd

# Function to read the sensor and threshold data
def read_data(sensor_data_path, threshold_data_path):
    sensor_data = pd.read_csv(sensor_data_path)
    threshold = pd.read_csv(threshold_data_path)
    
    return sensor_data, threshold