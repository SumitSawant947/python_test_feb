import pandas as pd 
def process_threshold_data(threshold):
    # Check if 'threshold_limit' exists and rename it to 'threshold_value'
    if 'threshold_limit' in threshold.columns:
        threshold.rename(columns={'threshold_limit': 'threshold_value'}, inplace=True)
    
    # Ensure the column 'threshold_value' exists, then fill missing values with 100
    if 'threshold_value' not in threshold.columns:
        print("Warning: 'threshold_value' column is missing!")
        threshold['threshold_value'] = 100  # Default value if column is missing

    threshold['threshold_value'] = threshold['threshold_value'].fillna(100)  # Ensure no NaN values remain
    return threshold

# Function to process the 'sensor_data' and convert 'date' to datetime format
def process_sensor_data(sensor_data):
    # Convert 'date' to datetime format
    sensor_data['date'] = pd.to_datetime(sensor_data['date'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    # Check for any invalid dates
    if sensor_data['date'].isna().any():
        print("Warning: There are invalid date values in the dataset!")
        print(sensor_data[sensor_data['date'].isna()])

    # Extract month from 'date'
    sensor_data['month'] = sensor_data['date'].dt.to_period('M')
    
    return sensor_data

# Function to calculate monthly statistics (avg, max, min)
def calculate_monthly_stats(sensor_data):
    monthly_stats = sensor_data.groupby(['month', 'sensor_type']).agg(
        average_value=('value', 'mean'),
        max_value=('value', 'max'),
        min_value=('value', 'min')
    ).reset_index()
    
    return monthly_stats

