import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Configuration
NUM_DEVICES = 6
DAYS_OF_DATA = 7   # start small (we can increase later)
READING_INTERVAL_MINUTES = 60

SENSOR_TYPES = {
    1: {"name": "Temperature", "min": 20, "max": 80},
    2: {"name": "Humidity", "min": 30, "max": 70},
    3: {"name": "Vibration", "min": 0, "max": 5},
    4: {"name": "Pressure", "min": 30, "max": 120},
}

# Time range
end_time = datetime.now()
start_time = end_time - timedelta(days=DAYS_OF_DATA)

timestamps = pd.date_range(
    start=start_time,
    end=end_time,
    freq=f"{READING_INTERVAL_MINUTES}min"
)

rows = []

# Generate data
for device_id in range(1, NUM_DEVICES + 1):
    for timestamp in timestamps:
        battery_level = round(np.random.uniform(60, 100), 2)
        signal_strength = round(np.random.uniform(70, 100), 2)

        for sensor_id, sensor_info in SENSOR_TYPES.items():
            normal_min = sensor_info["min"]
            normal_max = sensor_info["max"]

            reading_value = np.random.uniform(normal_min, normal_max)

            # 5% abnormal values
            if np.random.rand() < 0.05:
                if np.random.rand() < 0.5:
                    reading_value = normal_min - np.random.uniform(5, 15)
                else:
                    reading_value = normal_max + np.random.uniform(5, 15)

            rows.append({
                "device_id": device_id,
                "sensor_id": sensor_id,
                "reading_timestamp": timestamp,
                "reading_value": round(reading_value, 2),
                "battery_level": battery_level,
                "signal_strength": signal_strength
            })

# Create DataFrame
df = pd.DataFrame(rows)

# Save file
output_folder = os.path.join("data", "raw")
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "sensor_readings.csv")
df.to_csv(output_file, index=False)

print("Data generated successfully!")
print(f"Rows created: {len(df)}")
print(f"Saved to: {output_file}")

