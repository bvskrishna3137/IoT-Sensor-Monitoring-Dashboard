import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# PostgreSQL connection details
username = "postgres"
password = "Kittu@3137"
host = "localhost"
port = 5432
database = "iot_monitoring_db"

# Create database connection
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

# Read sensor readings joined with sensor thresholds
query = """
SELECT
    r.device_id,
    r.sensor_id,
    r.reading_timestamp,
    r.reading_value,
    s.threshold_min,
    s.threshold_max
FROM fact_sensor_reading r
JOIN dim_sensor s
    ON r.sensor_id = s.sensor_id
"""

df = pd.read_sql(query, engine)

# Function to determine alert type and severity
def classify_alert(row):
    if row["reading_value"] < row["threshold_min"]:
        difference = row["threshold_min"] - row["reading_value"]
        if difference >= 10:
            return "Below Minimum", "Critical", row["threshold_min"]
        else:
            return "Below Minimum", "Warning", row["threshold_min"]
    elif row["reading_value"] > row["threshold_max"]:
        difference = row["reading_value"] - row["threshold_max"]
        if difference >= 10:
            return "Above Maximum", "Critical", row["threshold_max"]
        else:
            return "Above Maximum", "Warning", row["threshold_max"]
    return None, None, None

# Create alert rows
alert_rows = []

for _, row in df.iterrows():
    alert_type, severity, threshold_value = classify_alert(row)

    if alert_type is not None:
        alert_rows.append({
            "device_id": row["device_id"],
            "sensor_id": row["sensor_id"],
            "alert_timestamp": row["reading_timestamp"],
            "alert_type": alert_type,
            "severity": severity,
            "reading_value": row["reading_value"],
            "threshold_value": threshold_value,
            "alert_status": "Open"
        })

alerts_df = pd.DataFrame(alert_rows)

# Insert alerts into PostgreSQL
if not alerts_df.empty:
    alerts_df.to_sql(
        "fact_alert",
        engine,
        if_exists="append",
        index=False
    )
    print("Alerts generated successfully!")
    print(f"Total alerts inserted: {len(alerts_df)}")
else:
    print("No alerts found.")