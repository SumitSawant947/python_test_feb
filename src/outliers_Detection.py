from errors_log import log_error
def Outliers_detection(sensor_data,thresholds):
    try:
        # Outliers detecting using merge and lambda function. Without this it is taking to much of time to execute.
        outliers = sensor_data.merge(thresholds, on="sensor_type", how="left")
        outliers = outliers[
            (outliers["value"] < outliers["min_threshold"]) | (outliers["value"] > outliers["max_threshold"])]
        outliers["threshold_exceeded"] = outliers.apply(
            lambda row: "Min" if row["value"] < row["min_threshold"] else "Max", axis=1
        )


        outliers = outliers[["date", "sensor_type", "value", "unit", "location_id", "threshold_exceeded"]]

        return outliers
    except Exception as e:
        log_error('Please check the variable assinged ',e)

