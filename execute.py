import csv
import logging
from datetime import datetime


logging.basicConfig(
    filename="sensor_processing.log",
    level=logging.INFO,
    format="%(message)s",
    filemode="w"
)

class SensorDataProcessor:
    def __init__(self, sensor_file="sensor_data.csv", threshold_file="thresholds.csv"):
        self.sensor_file = sensor_file
        self.threshold_file = threshold_file
        self.sensor_data = []
        self.thresholds = {}
        self.monthly_stats_file = "monthly_stats.csv"
        self.outliers_file = "outliers.csv"

    def load_csv(self, file_path):
        data = []
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
            logging.info(f"Loaded {len(data)} records from {file_path}")
        except FileNotFoundError:
            logging.info(f"File not found: {file_path}")
        except Exception as e:
            logging.info(f"Error reading file {file_path}: {e}")
        return data

    def parse_sensor_data(self):
        raw_data = self.load_csv(self.sensor_file)
        for row in raw_data:
            try:
                if not row['date'].strip():
                    logging.info(f"Skipping row due to missing date: {row}")
                    continue
                row['date'] = datetime.strptime(row['date'].strip().split()[0], "%Y-%m-%d").date()
                row['value'] = float(row['value'].strip())
                self.sensor_data.append(row)
            except ValueError as e:
                logging.info(f"Skipping row due to error: {row} | Error: {e}")

    def parse_thresholds(self):
        raw_thresholds = self.load_csv(self.threshold_file)
        for row in raw_thresholds:
            try:
                sensor_type = row['sensor_type'].strip()
                self.thresholds[sensor_type] = {
                    'min_threshold': float(row['min_threshold'].strip()),
                    'max_threshold': float(row['max_threshold'].strip())
                }
            except ValueError as e:
                logging.info(f"Skipping threshold row due to error: {row} | Error: {e}")

    def calculate_monthly_statistics(self):
        stats = {}
        for row in self.sensor_data:
            sensor_type = row['sensor_type']
            month = row['date'].strftime('%Y-%m')
            key = (sensor_type, month)

            if key not in stats:
                stats[key] = {'values': []}
            stats[key]['values'].append(row['value'])

        try:
            with open(self.monthly_stats_file, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["sensor_type", "month", "avg_value", "max_value", "min_value"])

                for (sensor, month), data in stats.items():
                    values = data['values']
                    avg_value = sum(values) / len(values)
                    writer.writerow([sensor, month, avg_value, max(values), min(values)])
                    logging.info(f"Processed {sensor} - {month}: Avg={avg_value}, Max={max(values)}, Min={min(values)}")

            logging.info(f"Monthly statistics saved in '{self.monthly_stats_file}'")

        except Exception as e:
            logging.info(f"Error writing '{self.monthly_stats_file}': {e}")

    def detect_outliers(self):
        try:
            with open(self.outliers_file, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["date", "sensor_type", "value", "unit", "location_id", "threshold_exceeded"])

                for row in self.sensor_data:
                    sensor_type = row['sensor_type']
                    if sensor_type in self.thresholds:
                        min_t = self.thresholds[sensor_type]['min_threshold']
                        max_t = self.thresholds[sensor_type]['max_threshold']

                        if row['value'] < min_t:
                            writer.writerow([row['date'], sensor_type, row['value'], row['unit'], row['location_id'], "Min"])
                            logging.info(f"Outlier detected (Min): {row}")
                        elif row['value'] > max_t:
                            writer.writerow([row['date'], sensor_type, row['value'], row['unit'], row['location_id'], "Max"])
                            logging.info(f"Outlier detected (Max): {row}")

            logging.info(f"Outliers saved in '{self.outliers_file}'")

        except Exception as e:
            logging.info(f"Error writing '{self.outliers_file}': {e}")


processor = SensorDataProcessor()
processor.parse_sensor_data()
processor.parse_thresholds()
processor.calculate_monthly_statistics()
processor.detect_outliers()

