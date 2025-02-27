from errors_log import log_error
from src.Data_ingestion import sensor_data_Ingestion,threshold_data_Ingestion
from src.Data_preprocessing import monthly_average
from outliers_Detection import Outliers_detection


def reporting_data(data1,data2):
    try:
        monthly_average(sensor_data_Ingestion(data1)).to_csv(r'Reports\monthly_stats_file.csv',index=False)
        Outliers_detection(sensor_data_Ingestion(data1),threshold_data_Ingestion(data2)).to_csv(r'Reports\outliers_file.csv',index=False)
        print('Successfully reports created!!')
    except Exception as e:
        log_error('Check the path ',e)