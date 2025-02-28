import csv

def generate_report(data, file_name, fieldnames):
    try:
        with open(f'output/{file_name}', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error generating {file_name}: {e}")