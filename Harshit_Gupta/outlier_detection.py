def detect_outliers(sensor_data, thresholds):
    threshold_dict = {row['sensor_type']: {'min': float(row['min_threshold']), 'max': float(row['max_threshold'])} for row in thresholds}
    outliers = []
    for row in sensor_data:
        sensor_type = row['sensor_type']
        value = float(row['value'])
        
        if sensor_type in threshold_dict:
            min_threshold = threshold_dict[sensor_type]['min']
            max_threshold = threshold_dict[sensor_type]['max']

            if value < min_threshold:
                outliers.append({'date': row['date'],'sensor_type': sensor_type,'value': value,
                    'unit': row['unit'],'location_id': row['location_id'],'threshold_exceeded': 'Min'
                })
            elif value > max_threshold:
                outliers.append({'date': row['date'],'sensor_type': sensor_type,'value': value,
                    'unit': row['unit'],'location_id': row['location_id'],'threshold_exceeded': 'Max'
                })
    return outliers
