import csv
import os
from datetime import datetime

class Process_sensor_data:
    def __init__(self, directory="."):
        self.directory = directory  # Directory where the files are stored
        self.sensor_data = []
        self.thresholds = {}
        self.error_log = os.path.join(self.directory, "error_log.txt")


#Logs errors to a file with a timestamp
    def log_error(self, error_code, message):
        with open(self.error_log, "a") as log_file:
            log_file.write(f"{datetime.now()} | {error_code} | {message}\n")


#Finds the specified file in the given directory
    def find_file(self, filename):
        file_path = os.path.join(self.directory, filename)
        return file_path if os.path.exists(file_path) else None
    

#Reads sensor data and threshold data from CSV files found in the directory
    def load_data(self):
        sensor_file = self.find_file("sensor_data.csv")
        threshold_file = self.find_file("thresholds.csv")

        if not sensor_file:
            self.log_error("ERR001", "File not found: sensor_data.csv")
            return
        if not threshold_file:
            self.log_error("ERR001", "File not found: thresholds.csv")
            return

        # Load sensor data
        try:
            with open(sensor_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        if not row.get('date', '').strip():
                            self.log_error("ERR002", f"Missing date: {row}")
                            continue

                        row['date'] = datetime.strptime(row['date'].strip().split()[0], "%Y-%m-%d").date()
                        row['value'] = float(row['value'].strip())  
                        self.sensor_data.append(row)
                    except ValueError as e:
                        self.log_error("ERR002", f"Invalid data format: {row} | Error: {e}")
        except Exception as e:
            self.log_error("ERR003", f"Error processing sensor_data.csv: {e}")

        # Load threshold data
        try:
            with open(threshold_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        sensor_type = row['sensor_type'].strip()
                        self.thresholds[sensor_type] = {
                            'min_threshold': float(row['min_threshold'].strip()),
                            'max_threshold': float(row['max_threshold'].strip())
                        }
                    except ValueError as e:
                        self.log_error("ERR002", f"Invalid threshold format: {row} | Error: {e}")
        except Exception as e:
            self.log_error("ERR003", f"Error processing thresholds.csv: {e}")

#Calculates monthly statistics (avg, min, max) for each sensor.
    def calculate_monthly_statistics(self):
        stats = {}
        for row in self.sensor_data:
            sensor_type = row['sensor_type']
            month = row['date'].strftime('%Y-%m')
            key = (sensor_type, month)

            if key not in stats:
                stats[key] = {'values': []}
            stats[key]['values'].append(row['value'])

        # Write results to CSV
        try:
            with open(os.path.join(self.directory, "monthly_stats.csv"), "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["sensor_type", "month", "avg_value", "max_value", "min_value"])

                for (sensor, month), data in stats.items():
                    values = data['values']
                    writer.writerow([sensor, month, sum(values)/len(values), max(values), min(values)])
        except Exception as e:
            self.log_error("ERR003", f"Error writing monthly_stats.csv: {e}")

#Identifies sensor readings that exceed thresholds.
    def detect_outliers(self):
        try:
            with open(os.path.join(self.directory, "outliers.csv"), "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["date", "sensor_type", "value", "unit", "location_id", "threshold_exceeded"])

                for row in self.sensor_data:
                    sensor_type = row['sensor_type']
                    if sensor_type not in self.thresholds:
                        self.log_error("ERR004", f"Thresholds not defined for sensor: {sensor_type}")
                        continue

                    min_t = self.thresholds[sensor_type]['min_threshold']
                    max_t = self.thresholds[sensor_type]['max_threshold']

                    if row['value'] < min_t:
                        writer.writerow([row['date'], sensor_type, row['value'], row['unit'], row['location_id'], "Min"])
                    elif row['value'] > max_t:
                        writer.writerow([row['date'], sensor_type, row['value'], row['unit'], row['location_id'], "Max"])
        except Exception as e:
            self.log_error("ERR003", f"Error writing outliers.csv: {e}")

# Run the program
processor = Process_sensor_data()
processor.load_data()
processor.calculate_monthly_statistics()
processor.detect_outliers()