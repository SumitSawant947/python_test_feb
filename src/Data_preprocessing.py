from errors_log import log_error
import pandas as pd


def monthly_average(sensor_data):
    try:
        sensor_data=sensor_data.dropna()
        sensor_data["value"] = pd.to_numeric(sensor_data["value"], errors='coerce')

        # Processing Monthly Statistics and stored in this method.
        monthly_stats = sensor_data.groupby(["sensor_type", "month"]).agg(
            avg_value=("value", "mean"),
            max_value=("value", "max"),
            min_value=("value", "min")
        ).reset_index()
        return monthly_stats


    except Exception as e:
        log_error('column name not found',e)

if __name__=='__main__':
    monthly_average(sensor_data_Ingestion('sensor_data.csv'))

