from datetime import datetime
def process_data(sensor_data):
    monthly_data = {}
    for row in sensor_data:
        try:
            month = datetime.strptime(row['date'], '%Y-%m-%d').strftime('%Y-%m')
            sensor_type = row['sensor_type']
            value = float(row['value'])  
            if sensor_type not in monthly_data:
                monthly_data[sensor_type] = {}
            if month not in monthly_data[sensor_type]:
                monthly_data[sensor_type][month] = []
            monthly_data[sensor_type][month].append(value)
        except ValueError:
            continue 

    stats = []
    for sensor_type, months in monthly_data.items():
        for month, values in months.items():
            stats.append({'sensor_type': sensor_type,'month': month,
                'avg_value': sum(values) / len(values),
                'max_value': max(values),
                'min_value': min(values)
            })
    return stats