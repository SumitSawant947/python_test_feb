from errors_log import log_error
import pandas as pd
def sensor_data_Ingestion(data):
    try:
        sensor_data=pd.read_csv(data)
        return sensor_data
    except FileNotFoundError as e:
        log_error(f'Unable to fetch the file ',e)
        exit(1)
    except pd.errors.ParserError as e:
        log_error("Invalid data format",e)
        exit(1)

def threshold_data_Ingestion(data):
    try:
        threshold_data=pd.read_csv(data)
        return threshold_data
    except FileNotFoundError as e:
        log_error(f'Unable to fetch the file ', e)
        exit(1)
    except pd.errors.ParserError as e:
        log_error("Invalid data format", e)
        exit(1)


if __name__=='__main__':
    sensor_data_Ingestion('sensor_data.csv')
    threshold_data_Ingestion('thresholds.csv')

