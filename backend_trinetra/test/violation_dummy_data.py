import random
from datetime import datetime, timedelta
import json

class TrafficViolationGenerator:
    def __init__(self, total_violations):
        self.total_violations = total_violations

    def generate_violation_entry(self, index):
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

    def generate_extended_violation_entry(self, index):
        base_entry = self.generate_violation_entry(index)
        violation_types = ["Traffic Light", "Lane Violation"]
        violation_type = random.choice(violation_types)

        base_entry["violation_type"] = violation_type
        return base_entry

    def generate_violation_data(self, extended=False):
        data = []
        generator_function = self.generate_extended_violation_entry if extended else self.generate_violation_entry

        for i in range(self.total_violations):
            entry = generator_function(i)
            data.append(entry)
        return data

    def save_to_json(self, extended=False):
        violations_data = self.generate_violation_data(extended)

        filename = "/home/ishwor/Desktop/alpr_speed_traffic/frontend-trinetra/src/data/main service data/trafficDummiesData.json" if extended else "generated_violations_data.json"
        with open(filename, "w") as json_file:
            json.dump(violations_data, json_file, indent=2)

        print(f"Generated {'extended ' if extended else ''}violations data saved to {filename}")

if __name__ == "__main__":
    total_violations = 1000

    generator = TrafficViolationGenerator(total_violations)

    generator.save_to_json()

    generator.save_to_json(extended=True)
