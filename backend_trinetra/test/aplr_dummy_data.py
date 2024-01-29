import random
from datetime import datetime, timedelta
import json

def generate_violation_entry(index):
    violation_id = f"VIOL{index + 1}"
    speed = random.randint(50, 100)
    recognized_info = f"Plate-{random.randint(1000, 9999)}"
    accuracy = round(random.uniform(0.7, 1.0), 2)
    date = datetime.now() - timedelta(days=index, minutes=random.randint(0, 60), seconds=random.randint(0, 60))
    status = random.choice(["In Progress", "Completed", "Pending"])

    return {
        "violation_id": violation_id,
        "speed": speed,
        "recognized_info": recognized_info,
        "accuracy": accuracy,
        "date": date.strftime("%b %d, %Y %H:%M:%S"),
        "status": status
    }

def generate_violation_data(count):
    data = []
    for i in range(count):
        entry = generate_violation_entry(i)
        data.append(entry)
    return data

if __name__ == "__main__":
    total_violations = 1000  

    violations_data = generate_violation_data(total_violations)

    with open("/home/ishwor/Desktop/alpr_speed_traffic/frontend-trinetra/src/data/main service data/speedDummiesData.json", "w") as json_file:
        json.dump(violations_data, json_file, indent=2)

    print("Generated violations data saved to generated_violations_data.json")
