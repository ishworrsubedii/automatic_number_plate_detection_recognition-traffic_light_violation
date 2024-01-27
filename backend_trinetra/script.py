import json
import random
from datetime import datetime, timedelta

# Initialize violation types and data list
violation_types = ['Red Light', 'Lane Violation', 'Traffic Rule Violation']
data = []

# Generate data for each day from December 2023 to February 2024
start_date = datetime(2023, 12, 1)
end_date = datetime(2024, 3, 1)
delta = timedelta(days=1)

while start_date < end_date:
    for violation_type in violation_types:
        data.append({
            'date': start_date.strftime('%Y-%m-%d'),
            'violation_type': violation_type,
            'count': random.randint(0, 100)  # Random number of violations
        })
    start_date += delta

# Write data to JSON file
with open('/home/ishwor/Desktop/alpr_speed_traffic/frontend-trinetra/src/data/traffic_violations.json', 'w') as f:
    json.dump(data, f)