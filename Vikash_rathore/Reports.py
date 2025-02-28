# import pandas as pd

# # Read the sensor and threshold data
# sensor_data = pd.read_csv(r'C:\Users\VikashRathore\Downloads\Feb_assessment\sensor_data.csv')
# threshold = pd.read_csv(r'C:\Users\VikashRathore\Downloads\Feb_assessment\thresholds.csv')

# if 'threshold_value' not in threshold.columns:
#     threshold.rename(columns={'threshold_limit': 'threshold_value'}, inplace=True)  
#     threshold['threshold_value'] = 100

# sensor_data['date'] = pd.to_datetime(sensor_data['date'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

# if sensor_data['date'].isna().any():
#     print("Warning: There are invalid date values in the dataset!")
#     print(sensor_data[sensor_data['date'].isna()])

# # Extract month from the 'date' column
# sensor_data['month'] = sensor_data['date'].dt.to_period('M')

# # Calculate monthly averages, max, and min
# monthly_stats = sensor_data.groupby(['month', 'sensor_type']).agg(
#     average_value=('value', 'mean'),
#     max_value=('value', 'max'),
#     min_value=('value', 'min')
# ).reset_index()

# print("Monthly Statistics:")
# print(monthly_stats.head())

# # Merge monthly statistics
# merged_data = pd.merge(monthly_stats, threshold, on='sensor_type', how='left')

# if merged_data.isna().any().any():
#     print("Warning: There are some missing threshold values after the merge.")

# merged_data['outlier'] = (merged_data['average_value'] > merged_data['threshold_value']) | \
#                          (merged_data['max_value'] > merged_data['threshold_value']) | \
#                          (merged_data['min_value'] > merged_data['threshold_value'])

# # Print outliers
# outliers = merged_data[merged_data['outlier'] == True]
# if not outliers.empty:
#     print("Outliers Detected:")
#     print(outliers)
# else:
#     print("No outliers detected.")

# # Save the monthly statistics file
# monthly_stats.to_csv(r'C:\Users\VikashRathore\Downloads\monthly_statistics.csv', index=False)
# print("Monthly statistics report saved to 'monthly_statistics.csv'.")

# # Save the outliers file
# if not outliers.empty:
#     outliers.to_csv(r'C:\Users\VikashRathore\Downloads\outliers_report.csv', index=False)
#     print("Outliers report saved to 'outliers_report.csv'.")
# else:
#     print("No outliers to save.")


def save_reports(monthly_stats, outliers):
    # Save the monthly statistics report
    monthly_stats.to_csv(r'C:\Users\VikashRathore\Downloads\monthly_statistics.csv', index=False)
    print("Monthly statistics report saved to 'monthly_statistics.csv'.")

    # Save the outliers report if any
    if not outliers.empty:
        outliers.to_csv(r'C:\Users\VikashRathore\Downloads\outliers_report.csv', index=False)
        print("Outliers report saved to 'outliers_report.csv'.")
    else:
        print("No outliers to save.")