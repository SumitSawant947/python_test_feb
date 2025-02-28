import pandas as pd
# Function to merge sensor data and threshold data
def merge_data(monthly_stats, threshold):
    merged_data = pd.merge(monthly_stats, threshold, on='sensor_type', how='left')

    if merged_data.isna().any().any():
        print("Warning: There are some missing threshold values after the merge.")
    
    return merged_data

def detect_outliers(merged_data):
    merged_data['outlier'] = (merged_data['average_value'] > merged_data['threshold_value']) | \
                             (merged_data['max_value'] > merged_data['threshold_value']) | \
                             (merged_data['min_value'] > merged_data['threshold_value'])

    outliers = merged_data[merged_data['outlier'] == True]
    
    return outliers