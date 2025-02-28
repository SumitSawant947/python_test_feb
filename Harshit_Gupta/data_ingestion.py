import csv
ERR001 = "File not found"
ERR002 = "Invalid data format"
def read_sensor_data():
    data = []
    try:
        with open('data/sensor_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try: #Checking if value is an empty string or none, and if so, then skiping it
                    if row['value'] == '' or row['value'] is None:
                        print(f"Skipping row due to empty value: {row}")
                        continue  
                    row['value'] = float(row['value'])
                    data.append(row)  
                except ValueError as e:
                    print(f"Skipping row due to error : {row}, error: {e}")
                    continue  
    except FileNotFoundError:
        raise FileNotFoundError(ERR001)
    return data

def read_thresholds():
    data = []
    try:
        with open('data/thresholds.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try: #Checking if min or max is an empty string, and if so, skiping it
                    if row['min_threshold'] == '' or row['max_threshold'] == '':
                        print(f"Skipping threshold row due to empty threshold value: {row}")
                        continue 
                    row['min_threshold'] = float(row['min_threshold'])
                    row['max_threshold'] = float(row['max_threshold'])
                    data.append(row) 
                except ValueError as e:
                    print(f"Skipping threshold row due to error in conversion: {row}, error: {e}")
                    continue 
    except FileNotFoundError:
        raise FileNotFoundError(ERR001)   
    return data