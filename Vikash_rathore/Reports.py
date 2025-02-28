import pandas as pd

def save_reports(monthly_stats, outliers):
    # Save the monthly statistics report
    monthly_stats.to_csv(r'C:\Users\VikashRathore\Downloads\monthly_statistics.csv', index=False)
    print("Monthly statistics report saved to 'monthly_statistics.csv'.")

    # Save the outliers report if any
    if not outliers.empty:
        outliers.to_csv(r'C:\Users\VikashRathore\Downloads\outliers_report.csv', index=False)
        print("Outliers report saved to 'outliers_report.csv'.")
    else:
        print("No outliers to save.")
