from outliers_Detection import Outliers_detection
from Data_ingestion import sensor_data_Ingestion,threshold_data_Ingestion
from Reporting import reporting_data
from src.errors_log import log_error

sensor_data=input('Please Enter the sensor_data_set name [with .csv]:')
thresholds_data=input('Please Enter the thresholds_data_set name [with .csv]:')
try:
    print(Outliers_detection(sensor_data_Ingestion(sensor_data),threshold_data_Ingestion(thresholds_data)))
    print(reporting_data(sensor_data,thresholds_data))
except Exception as e:
    log_error('Please give proper data_set name with .csv at the end',e)
