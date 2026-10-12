# File Handling and I/O - CSV to JSON Conversion
# Experiment 9: Based on the aim to read data from a CSV file, convert it into JSON format using Python's csv and json modules, and write it to an output file:

import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    json_array = []
    
    # Read the CSV file and load data using DictReader[cite: 69, 70]
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each CSV row into a Python dictionary and append to array[cite: 69, 70]
        for row in csv_reader:
            json_array.append(row)
            
    # Serialize the Python list to a JSON string with indentation and write to file[cite: 69, 70]
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)

# Main Program
if __name__ == "__main__":
    # Sample input CSV path and output JSON path
    csv_path = 'data.csv'
    json_path = 'data.json'
    
    # (Optional) Creating a dummy input.csv for demonstration if it doesn't exist
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        writer.writerow(['25', '84', 'com'])
        writer.writerow(['41', '52', 'org'])
        writer.writerow(['58', '79', 'io'])
        writer.writerow(['93', '21', 'co'])

    csv_to_json(csv_path, json_path)
    print(f"Successfully converted {csv_path} to {json_path}")
    
    # Display generated JSON content
    with open(json_path, 'r', encoding='utf-8') as jf:
        print("\nGenerated JSON Content:")
        print(jf.read())