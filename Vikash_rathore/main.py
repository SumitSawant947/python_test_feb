from Data_Ingestion import read_data
from Processing_Module import process_threshold_data, process_sensor_data, calculate_monthly_stats
from Outlier_Detection import merge_data, detect_outliers
from Reports import save_reports

def main():
    # File paths
    sensor_data_path = r'C:\Users\VikashRathore\Downloads\Feb_assessment\sensor_data.csv'
    threshold_data_path = r'C:\Users\VikashRathore\Downloads\Feb_assessment\thresholds.csv'

    sensor_data, threshold = read_data(sensor_data_path, threshold_data_path)
    threshold = process_threshold_data(threshold)
    sensor_data = process_sensor_data(sensor_data)

    monthly_stats = calculate_monthly_stats(sensor_data)
    print("Monthly Statistics:")
    print(monthly_stats.head()) 

    merged_data = merge_data(monthly_stats, threshold)

    outliers = detect_outliers(merged_data)
    
    # Step 7: Print outliers and save the reports
    if not outliers.empty:
        print("Outliers Detected:")
        print(outliers)
    else:
        print("No outliers detected.")

    # Step 8: Save the reports
    save_reports(monthly_stats, outliers)

if __name__ == '__main__':
    main()