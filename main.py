# main.py
from data_ingection import load_data, validate_data
from data_processing import calculate_monthly_stats
from outiler_detection import detect_outliers
from reporting import save_monthly_stats, save_outliers

def main():
    # Load the data
    sensor_data, thresholds_data = load_data('sensor_data.csv', 'thresholds.csv')
    
    if sensor_data is None or thresholds_data is None:
        print("Error loading data. Exiting...")
        return

    # Validate the data
    if validate_data(sensor_data, thresholds_data):
        print("Data validation successful.")
    else:
        print("Data validation failed.")
        return
    
    # Calculate monthly stats
    stats = calculate_monthly_stats(sensor_data)
    
    # Detect outliers
    outliers = detect_outliers(sensor_data, thresholds_data)
    
    # Save the results
    save_monthly_stats(stats)
    save_outliers(outliers)
    
    print("Processing complete. Output files generated.")

# Main function
if __name__ == "__main__":
    main()
