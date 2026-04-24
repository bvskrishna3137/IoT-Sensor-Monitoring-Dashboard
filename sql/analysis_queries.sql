-- 1. Total sensor readings
SELECT COUNT(*) AS total_sensor_readings
FROM fact_sensor_reading;

-- 2. Total alerts
SELECT COUNT(*) AS total_alerts
FROM fact_alert;

-- 3. Alerts by severity
SELECT
    severity,
    COUNT(*) AS alert_count
FROM fact_alert
GROUP BY severity
ORDER BY alert_count DESC;

-- 4. Alerts by sensor type
SELECT
    s.sensor_type,
    COUNT(*) AS alert_count
FROM fact_alert a
JOIN dim_sensor s
    ON a.sensor_id = s.sensor_id
GROUP BY s.sensor_type
ORDER BY alert_count DESC;

-- 5. Alerts by device
SELECT
    d.device_name,
    COUNT(*) AS alert_count
FROM fact_alert a
JOIN dim_device d
    ON a.device_id = d.device_id
GROUP BY d.device_name
ORDER BY alert_count DESC;

-- 6. Average reading by sensor type
SELECT
    s.sensor_type,
    ROUND(AVG(r.reading_value), 2) AS avg_reading
FROM fact_sensor_reading r
JOIN dim_sensor s
    ON r.sensor_id = s.sensor_id
GROUP BY s.sensor_type
ORDER BY s.sensor_type;

-- 7. Daily alert trend
SELECT
    DATE(alert_timestamp) AS alert_date,
    COUNT(*) AS total_alerts
FROM fact_alert
GROUP BY DATE(alert_timestamp)
ORDER BY alert_date;

-- 8. Daily average reading by sensor
SELECT
    DATE(r.reading_timestamp) AS reading_date,
    s.sensor_type,
    ROUND(AVG(r.reading_value), 2) AS avg_reading
FROM fact_sensor_reading r
JOIN dim_sensor s
    ON r.sensor_id = s.sensor_id
GROUP BY DATE(r.reading_timestamp), s.sensor_type
ORDER BY reading_date, s.sensor_type;