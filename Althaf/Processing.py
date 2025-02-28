import pandas as pd

def process_monthly_sensor_data(sensor_file):
    try:
        sensor_data = pd.read_csv(sensor_file)

        # Extract month from date if not provided
        if "month" not in sensor_data.columns:
            sensor_data["date"] = pd.to_datetime(sensor_data["date"], errors="coerce")
            sensor_data["month"] = sensor_data["date"].dt.strftime('%Y-%m')

        # Validate required columns
        required_columns = {"month", "sensor_type", "value"}
        if not required_columns.issubset(sensor_data.columns):
            print("Error: Missing required columns in sensor data.")
            return None

        # Calculate monthly statistics
        monthly_data = sensor_data.groupby(["month", "sensor_type"])["value"].agg(["mean", "min", "max"]).reset_index()
        monthly_data.rename(columns={"mean": "avg_value", "min": "min_value", "max": "max_value"}, inplace=True)

        # Save to CSV
        output_file = "monthly_stats.csv"
        monthly_data.to_csv(output_file, index=False)

        return output_file

    except Exception as e:
        print(f"Error processing monthly statistics: {e}")
        return None

if __name__ == "__main__":
    csv_file = process_monthly_sensor_data("sensor_data.csv")
    print(f"CSV file saved at: {csv_file}" if csv_file else "Processing failed.")


