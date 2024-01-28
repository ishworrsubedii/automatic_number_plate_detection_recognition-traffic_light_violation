import random
from datetime import datetime, timedelta
import json

def generate_data_entry(prefix, index):
    detection_id = f"{prefix}{index + 1}"
    recognized_info = f"{prefix} {random.randint(1, 999)} {prefix} {random.randint(1000, 9999)}"
    accuracy = round(random.uniform(0.7, 1.0), 2)
    date = datetime.now() - timedelta(days=index, minutes=random.randint(0, 60), seconds=random.randint(0, 60))
    status = random.choice(["In Progress", "Complete", "Pending", "Approved", "Rejected"])

    return {
        "id": index + 1,
        "Detection Id": detection_id,
        "Recognized Info": recognized_info,
        "Accuracy": accuracy,
        "Date": date.strftime("%b %d, %Y %H:%M:%S"),
        "Status": status
    }

def generate_data(prefix, count):
    data = []
    for i in range(count):
        entry = generate_data_entry(prefix, i)
        data.append(entry)
    return data

if __name__ == "__main__":
    plate_prefixes = ["BA", "PA", "JA"]
    total_entries = 3000

    full_data = []
    for prefix in plate_prefixes:
        plate_data = generate_data(prefix, total_entries // len(plate_prefixes))
        full_data.extend(plate_data)

    # Save the generated data to a JSON file
    with open("/home/ishwor/Desktop/alpr_speed_traffic/frontend-trinetra/src/data/alprDummiesData.json", "w") as json_file:
        json.dump(full_data, json_file, indent=2)

    print("Generated data saved to generated_data.json")
