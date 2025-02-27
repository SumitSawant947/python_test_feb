import logging
from ingestion import read_csv_file
from processing import calculate_monthly_statistics
from outlier_detection import detect_outliers
from reporting import save_csv

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs.log"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)

def main():
    """Main function to execute the data processing pipeline with exception handling."""
    try:
        logging.info("Starting sensor data processing...")
        
        sensor_data = read_csv_file("data/sensor_data.csv")
        thresholds = read_csv_file("data/thresholds.csv")
        
        monthly_stats = calculate_monthly_statistics(sensor_data)
        save_csv(monthly_stats, "reports/monthly_stats.csv")
        
        outliers = detect_outliers(sensor_data, thresholds)
        save_csv(outliers, "reports/outliers.csv")
        
        logging.info("Processing completed.")
    except Exception as e:
        logging.error(f"ERR007: Critical failure in main execution - {e}")

if __name__ == "__main__":
    main()