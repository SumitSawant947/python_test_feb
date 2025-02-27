# Reporting Module: Generates two CSV reports: one for monthly statistics and one for outliers.

def generate_report(data, filename):
    data.to_csv(filename, index=False)
    print(f"Report saved as {filename}.")
