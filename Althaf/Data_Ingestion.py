import pandas as pd


def load_and_print_data(file1, file2):
    """..Loads two CSV files, prints content, and saves them as CSV...."""

    sensor_data = pd.read_csv(file1)  # Load first CSV file
    print(sensor_data)  # Print first file content

    threshold_data = pd.read_csv(file2)  # Load second CSV file
    print(threshold_data)  # Print second file content

    sensor_data.to_csv("converted_sensor_data.csv", index=False)  # Save first file as CSV
    threshold_data.to_csv("converted_thresholds.csv", index=False)  # Save second file as CSV

    return "converted_sensor_data.csv", "converted_thresholds.csv"  # Return output


# Execute function
if __name__ == "__main__":
    load_and_print_data("sensor_data.csv", "thresholds.csv")
