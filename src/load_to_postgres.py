import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# PostgreSQL connection details
username = "postgres"
password = "Kittu@3137"
host = "localhost"
port = 5432
database = "iot_monitoring_db"

# CSV file path
csv_file = "data/raw/sensor_readings.csv"

# Read CSV file
df = pd.read_csv(csv_file)

# Convert timestamp column
df["reading_timestamp"] = pd.to_datetime(df["reading_timestamp"])

# Safe database connection
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

# Load data into PostgreSQL
df.to_sql(
    "fact_sensor_reading",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully into PostgreSQL!")
print(f"Rows inserted: {len(df)}")