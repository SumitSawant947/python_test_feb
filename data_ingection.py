import pandas as pd
import os

# Function to load the input files
def load_data(sensor_file, thresholds_file):
    try:
        sensor_data = pd.read_csv(sensor_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None
    except pd.errors.ParserError:
        print("Error: ERR002 - Invalid data format in sensor file")
        return None, None

    try:
        thresholds_data = pd.read_csv(thresholds_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None
    except pd.errors.ParserError:
        print("Error: ERR002 - Invalid data format in thresholds file")
        return None, None

    return sensor_data, thresholds_data

# Function to validate the sensor data
def validate_data(sensor_data, thresholds_data):
    required_sensor_columns = ['date', 'sensor_type', 'value', 'unit', 'location_id']
    assert all(col in sensor_data.columns for col in required_sensor_columns), "Sensor data is missing required columns."

    required_threshold_columns = ['sensor_type', 'min_threshold', 'max_threshold']
    assert all(col in thresholds_data.columns for col in required_threshold_columns), "Threshold data is missing required columns."

    return True
