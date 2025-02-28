import pandas as pd
import os
from Processing import process_monthly_sensor_data
from Outlier_Detection import detect_outliers

class ReportingModule:
    def __init__(self, sensor_file, threshold_file):
        self.sensor_file = sensor_file
        self.threshold_file = threshold_file

    def generate_reports(self):
        print("\nGenerating Reports...")

        monthly_stats_file = process_monthly_sensor_data(self.sensor_file)
        outlier_file = detect_outliers(self.sensor_file, self.threshold_file)

        for file, name in [(monthly_stats_file, "Monthly Statistics"), (outlier_file, "Outliers")]:
            if file and os.path.exists(file):
                print(f"\n{name} Preview:")
                print(pd.read_csv(file).head())
            else:
                print(f"\n{name} report not generated.")

        print("\nReports Generated Successfully.")

if __name__ == "__main__":
    ReportingModule("sensor_data.csv", "thresholds.csv").generate_reports()

