from outliers_Detection import Outliers_detection
from Data_ingestion import data_Ingestion
from Reporting import reporting_data
from src.errors_log import log_error

sensor_data=input('Please Enter the sensor_data_set name with extension:')
thresholds_data=input('Please Enter the thresholds_data_set name with extension:')
try:
    print(Outliers_detection(data_Ingestion(sensor_data),data_Ingestion(thresholds_data)))
    print(reporting_data(sensor_data,thresholds_data))
except Exception as e:
    log_error('ERROR002: please give proper name with extension ',e)
