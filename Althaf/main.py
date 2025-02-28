import os
from Processing import process_monthly_sensor_data
from Outlier_Detection import detect_outliers
from Reporting import ReportingModule

def main():
    """Runs the Reporting Module and confirms CSV file generation."""

    report = ReportingModule("sensor_data.csv", "thresholds.csv")
    report.generate_reports()  # Generate reports

    # Define expected output files
    files = ["monthly_stats.csv", "outliers.csv", "output_files.csv"]

    # Create a summary file listing all generated reports
    with open("output_files.csv", "w") as f:
        f.write("Generated CSV Files\n")
        for file in files[:2]:  # Exclude output_files.csv itself
            if os.path.exists(file):
                f.write(f"{file}\n")

    # Print confirmation
    print("\nGenerated CSV Files:")
    for file in files:
        if os.path.exists(file):
            print(f"{file} is ready for download.")
        else:
            print(f"{file} was not generated.")


if __name__ == "__main__":
    main()

