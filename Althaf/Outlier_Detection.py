import pandas as pd

def detect_outliers(sensor_file, threshold_file, output_file="outliers.csv"):
    """Detects sensor readings that exceed thresholds and saves them to a CSV file."""
    try:
        sensor_data = pd.read_csv(sensor_file)
        thresholds = pd.read_csv(threshold_file).set_index("sensor_type")

        outliers = sensor_data.merge(thresholds, on="sensor_type", how="left")
        mask = (outliers["value"] < outliers["min_threshold"]) | (outliers["value"] > outliers["max_threshold"])
        outliers = outliers[mask][["date", "sensor_type", "value", "unit", "location_id"]]

        outliers.to_csv(output_file, index=False)
        return output_file
    except Exception:
        return None

if __name__ == "__main__":
    print(detect_outliers("sensor_data.csv", "thresholds.csv"))

