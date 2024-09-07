import sys
import csv
import json
import re

if len(sys.argv) < 2:
    print("Usage: python processor.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
name = csv_file.rsplit('.', 1)[0]

clean_domain = lambda domain: re.sub(r'^https?://', '', domain).split('/')[0]

with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    allowlist = [
        f"*.{clean_domain(row['identifier'])}" 
        for row in csv_reader 
        if row['identifier'] and row['asset_type'] == "URL"
    ]

scope_data = {"id": "1", "name": name, "allowlist": allowlist, "denylist": []}
json_filename = f"{name}.json"
with open(json_filename, 'w') as jsonf:
    json.dump(scope_data, jsonf, indent=4)

print(f"'{name}' scope created and saved in {json_filename}.")
