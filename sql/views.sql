CREATE OR REPLACE VIEW vw_latest_sensor_readings AS
SELECT
    r.device_id,
    d.device_name,
    d.device_type,
    l.location_name,
    l.city,
    l.plant_section,
    r.sensor_id,
    s.sensor_type,
    s.unit,
    r.reading_timestamp,
    r.reading_value,
    r.battery_level,
    r.signal_strength
FROM fact_sensor_reading r
JOIN dim_device d
    ON r.device_id = d.device_id
JOIN dim_location l
    ON d.location_id = l.location_id
JOIN dim_sensor s
    ON r.sensor_id = s.sensor_id
WHERE r.reading_timestamp = (
    SELECT MAX(r2.reading_timestamp)
    FROM fact_sensor_reading r2
    WHERE r2.device_id = r.device_id
      AND r2.sensor_id = r.sensor_id
);

CREATE OR REPLACE VIEW vw_alert_summary AS
SELECT
    a.alert_id,
    a.alert_timestamp,
    a.alert_type,
    a.severity,
    a.reading_value,
    a.threshold_value,
    a.alert_status,
    d.device_name,
    d.device_type,
    l.location_name,
    l.city,
    l.plant_section,
    s.sensor_type,
    s.unit
FROM fact_alert a
JOIN dim_device d
    ON a.device_id = d.device_id
JOIN dim_location l
    ON d.location_id = l.location_id
JOIN dim_sensor s
    ON a.sensor_id = s.sensor_id;

CREATE OR REPLACE VIEW vw_device_status_summary AS
SELECT
    d.device_id,
    d.device_name,
    d.device_type,
    d.status AS device_status,
    l.location_name,
    l.city,
    l.plant_section,
    COUNT(r.reading_id) AS total_readings,
    COUNT(a.alert_id) AS total_alerts,
    SUM(CASE WHEN a.severity = 'Critical' THEN 1 ELSE 0 END) AS critical_alerts,
    AVG(r.battery_level) AS avg_battery_level,
    AVG(r.signal_strength) AS avg_signal_strength
FROM dim_device d
LEFT JOIN dim_location l
    ON d.location_id = l.location_id
LEFT JOIN fact_sensor_reading r
    ON d.device_id = r.device_id
LEFT JOIN fact_alert a
    ON d.device_id = a.device_id
GROUP BY
    d.device_id,
    d.device_name,
    d.device_type,
    d.status,
    l.location_name,
    l.city,
    l.plant_section;