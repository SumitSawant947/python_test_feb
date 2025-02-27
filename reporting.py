import pandas as pd

def save_monthly_stats(stats, filename='monthly_stats.csv'):
    if isinstance(stats, pd.DataFrame) and not stats.empty:
        stats.to_csv(filename, index=False)
        print(f"Monthly stats saved to {filename}")
    else:
        print("Error: No data to save for monthly stats.")

def save_outliers(outliers, filename='outliers.csv'):
    if isinstance(outliers, pd.DataFrame) and not outliers.empty:
        outliers.to_csv(filename, index=False)
        print(f"Outliers saved to {filename}")
    else:
        print("Error: No data to save for outliers.")
