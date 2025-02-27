from ingest import load_data
from process import calculate_monthly_statistics
from detect import detect_outliers
from report import generate_report

def run_system(sensor_data_path, thresholds_path):
    sensor_data, thresholds = load_data(sensor_data_path, thresholds_path)
    
    if sensor_data is None or thresholds is None:
        print("Error loading data. Exiting...")
        return
    
    # Process Monthly Stats
    sensor_data['month'] = sensor_data['date'].dt.to_period('M')
    monthly_stats = calculate_monthly_statistics(sensor_data)
    
    # Detect Outliers
    outliers = detect_outliers(sensor_data, thresholds)
    
    # Generate Reports
    generate_report(monthly_stats, 'monthly_stats.csv')
    generate_report(outliers, 'outliers.csv')

    print("\nTop 5 entries from monthly_stats.csv:")
    print(monthly_stats.head())

    print("\nTop 5 entries from outliers.csv:")
    print(outliers.head())

def main():
    sensor_data_path = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\PyAssessment\sensor_data.csv"
    thresholds_path = r"C:\Users\PranavChothave\OneDrive - Atyeti Inc\Desktop\PyAssessment\thresholds.csv"
    run_system(sensor_data_path, thresholds_path)

if __name__ == "__main__":
    main()
