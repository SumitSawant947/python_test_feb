from data_ingestion import read_sensor_data, read_thresholds
from processing import process_data
from outlier_detection import detect_outliers
from reporting import generate_report

def main():
    try:
        sensor_data = read_sensor_data()
        thresholds = read_thresholds()
        
        monthly_stats = process_data(sensor_data)

        outliers = detect_outliers(sensor_data, thresholds)

        generate_report(monthly_stats, 'monthly_stats.csv', ['sensor_type', 'month', 'avg_value', 'max_value', 'min_value'])
        generate_report(outliers, 'outliers.csv', ['date', 'sensor_type', 'value', 'unit', 'location_id', 'threshold_exceeded'])

    except FileNotFoundError as e:
        print(f"Error: {e} - Could not find CSV files.")
if __name__ == "__main__":
    main()
