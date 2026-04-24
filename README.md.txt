# 📡 IoT Sensor Monitoring Dashboard
> A full-stack data analytics portfolio project by **Venkata Sai Krishna Baggu**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project delivers a complete, end-to-end IoT data analytics pipeline —
built to simulate how real industrial environments monitor connected sensor devices.
It processes high-frequency sensor readings (temperature, humidity, vibration,
and pressure), automatically detects threshold violations, and surfaces
actionable insights through a professional multi-page Power BI dashboard.

Built independently as a **portfolio project**, this solution demonstrates
applied skills across the full data stack: Python data engineering, PostgreSQL
database design, SQL transformation logic, and Power BI analytics.

---

## 🛠️ Tools & Technologies

| Tool | Component | Purpose |
|------|-----------|---------|
| Python | Pandas · NumPy · Faker | Synthetic data generation & preprocessing |
| PostgreSQL | v15 · Relational DB | Schema design & persistent data storage |
| SQL | DDL · DML · Views | Data modelling, transformation & alert logic |
| Power BI | Desktop · Service | Interactive dashboards & visual reporting |
| GitHub | Version Control | Source control & portfolio showcase |

---

## 🔄 Data Pipeline Architecture
[ Python Scripts ]
↓
Generate synthetic sensor data
(temperature, humidity, vibration, pressure)
↓
[ PostgreSQL Database ]
Store raw readings · Enforce schema integrity
↓
[ SQL Queries & Views ]
Transform data · Apply threshold alerting logic
↓
[ Power BI Dashboard ]
Visualise insights · Enable drill-through analysis

---

## 🧱 Data Model — Star Schema
              ┌─────────────┐
              │   Device    │
              └──────┬──────┘
                     │
┌──────────┐    ┌────────┴────────┐    ┌──────────┐
│  Sensor  ├────│ Sensor Readings ├────│ Location │
└──────────┘    │   (Fact Table)  │    └──────────┘
└────────┬────────┘
│
┌──────┴──────┐
│   Alerts    │
└─────────────┘

- **Fact Table** — Sensor Readings (reading value, timestamp, device ID)
- **Dim: Device** — device name, type, status, battery level, signal strength
- **Dim: Sensor** — sensor type, unit, min/max thresholds
- **Dim: Location** — facility, zone, geographical coordinates
- **Dim: Alerts** — alert type, severity (Critical / High / Medium / Low), status

---

## 📊 Dashboard Pages

### 1. 🏢 Executive Overview
- KPI scorecards — total devices, total alerts, critical alert count
- Alert distribution by severity (Critical / High / Medium / Low)
- Latest sensor readings snapshot across all active devices

### 2. 🖥️ Device Health Monitoring
- Device-level performance grid (status, uptime, battery, signal strength)
- Battery and signal strength health indicators
- Geographic distribution of devices by facility location

### 3. 📈 Trend & Anomaly Analysis
- Time-series sensor reading charts with rolling averages
- Alert frequency trends segmented by severity over time
- Anomaly detection based on deviation from device baseline

### 4. 🔍 Alert Deep Dive
- Ranked list of top alert-generating devices
- Alert distribution by sensor type and facility location
- Drill-through detail table for root cause investigation

---

## 📸 Dashboard Preview

### Executive Overview
![Page 1](screenshots/page1_overview.png)

### Device Health Monitoring
![Page 2](screenshots/page2_device.png)

### Trend & Anomaly Analysis
![Page 3](screenshots/page3_trend.png)

### Alert Deep Dive
![Page 4](screenshots/page4_alert.png)

---

## 🔍 Key Insights

- **Device-006** consistently generates the highest alert volume —
  indicating probable hardware degradation or miscalibration
- **Humidity sensors** account for the greatest share of alerts
  across all sensor types
- Alert frequency shows **cyclical day-to-day patterns**,
  suggesting operational or environmental cycles
- Certain **facility locations** show significantly higher alert
  concentrations, warranting targeted site-level review

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/bvskrishna3137/iot-sensor-dashboard.git
cd iot-sensor-dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure your database credentials**

Create a `.env` file in the root folder:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=iot_dashboard
DB_USER=your_username
DB_PASSWORD=your_password

**4. Generate the sensor data**
```bash
python data_generation/generate_sensor_data.py
```

**5. Set up the database**
- Open PostgreSQL and run `database/schema.sql`
- Run `sql/queries.sql` to create views and alert logic

**6. Open Power BI**
- Connect to your PostgreSQL database via ODBC
- Load and refresh the dashboard

---

## 📁 Project Structure
iot-sensor-dashboard/
│
├── requirements.txt
├── .env                    ← DB credentials (not pushed to GitHub)
├── .gitignore
├── README.md
│
├── data_generation/
│   └── generate_sensor_data.py
│
├── database/
│   └── schema.sql
│
├── sql/
│   └── queries.sql
│
└── screenshots/
├── page1_overview.png
├── page2_device.png
├── page3_trend.png
└── page4_alert.png

---

## 🔮 Future Enhancements

- [ ] Real-time streaming with Apache Kafka or Azure Event Hubs
- [ ] Predictive maintenance using Machine Learning (LSTM / Isolation Forest)
- [ ] Automated alert notifications via Email / SMS / Microsoft Teams
- [ ] Cloud deployment on Microsoft Azure (ADF + Azure PostgreSQL + Power BI Premium)

---

## 👤 Author

**Venkata Sai Krishna Baggu**  
Data Engineer & Analytics Developer

[![GitHub](https://img.shields.io/badge/GitHub-bvskrishna3137-black?logo=github)](https://github.com/bvskrishna3137)
[![Email](https://img.shields.io/badge/Email-bvskrishna3137@gmail.com-red?logo=gmail)](mailto:bvskrishna3137@gmail.com)

---

## 📄 License

This project is developed for **personal portfolio and non-commercial use only**.