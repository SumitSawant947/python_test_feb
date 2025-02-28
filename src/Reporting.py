from errors_log import log_error
from src.Data_ingestion import data_Ingestion
from src.Data_preprocessing import monthly_average
from outliers_Detection import Outliers_detection


def reporting_data(data1,data2):
    try:
        monthly_average(data_Ingestion(data1)).to_csv(r'Reports\monthly_stats_file.csv',index=False)
        Outliers_detection(data_Ingestion(data1),data_Ingestion(data2)).to_csv(r'Reports\outliers_file.csv',index=False)
        print('Successfully reports created!!')
    except Exception as e:
        log_error('ERROR003 ',e)
