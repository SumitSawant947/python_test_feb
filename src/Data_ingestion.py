from errors_log import log_error
import pandas as pd
from pathlib import Path as path
def data_Ingestion(data):

    # read any format data and convert into DataFrame
    try:
        if path(data).suffix == '.csv':
            df = pd.read_csv(data)
        elif path(data).suffix == '.json':
            df = pd.read_json(data)
        elif path(data).suffix in ['.xml', '.xlsx']:
            df = pd.read_excel(data)
        return df
    except FileNotFoundError as e:
        log_error(f'ERROR001 ',e)
        exit(1)
    except pd.errors.ParserError as e:
        log_error("ERROR",e)
        exit(1)



if __name__=='__main__':
    sensor_data=data_Ingestion('sensor_data.csv')
    threshold_data=data_Ingestion('thresholds.csv')



