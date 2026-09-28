# AtmoSync: Micro-Climate Arbitrage Analytics

## Mid-Project Review — Week 1 & Week 2

### 1. Project Overview

AtmoSync: Micro-Climate Arbitrage Analytics is a data analytics and data engineering project that monitors simulated micro-climate conditions inside shipping containers.

The project uses simulated IoT sensor data such as:

- Temperature
- Humidity
- Vibration
- Container ID
- Timestamp

The pipeline processes the sensor data through streaming, cloud storage, transformation, analytics, and visualization layers.

### 2. Project Objective

The objective of AtmoSync is to analyze container environmental conditions, identify container status and spoilage risk, and combine sensor information with mock commodity pricing data to calculate potential market arbitrage.

### 3. Technology Stack

- Python
- Apache Kafka
- Docker
- Snowflake
- dbt
- Apache Superset
- SQL
- Git
- GitHub

### 4. Project Architecture

Python IoT Simulator
        ↓
Kafka Producer
        ↓
Kafka Topic: sensor-data
        ↓
Snowflake RAW.SENSOR_DATA
        ↓
dbt Transformation
        ↓
Spoilage Risk Analytics
        ↓
Apache Superset
        ↓
AtmoSync Analytics Dashboard

### 5. Week 1 Implementation

During Week 1, the following work was completed:

- Created a Python IoT simulator.
- Generated simulated container sensor data.
- Added container ID and timestamp.
- Generated temperature, humidity and vibration values.
- Added Normal, Warning and Critical container status.
- Added sensor data validation.
- Added CSV and JSON data storage.
- Initialized Git and GitHub repository.
- Configured Apache Kafka using Docker.
- Created the `sensor-data` Kafka topic.
- Implemented the Kafka producer.
- Verified sensor messages through Kafka.

### 6. Week 2 Implementation

During Week 2, the following work was completed:

- Connected the Kafka pipeline to Snowflake.
- Created `ATMOSYNC_DB`.
- Created the `RAW` schema.
- Created `RAW.SENSOR_DATA`.
- Implemented Kafka-to-Snowflake data ingestion.
- Configured Apache Superset.
- Connected Superset to Snowflake.
- Created the AtmoSync analytics dashboard.
- Configured dbt Core with Snowflake.
- Created sensor staging models.
- Added mock commodity pricing data.
- Created commodity pricing staging model.
- Created combined sensor and commodity staging model.
- Created the `spoilage_risk` analytics model.
- Added dbt data-quality tests.
- Added project documentation to GitHub.

### 7. Data Validation

Two types of checks are used in the project:

**STATUS**

Represents the condition of the container:

- NORMAL
- WARNING
- CRITICAL

**DATA_VALID**

Represents whether the sensor record is technically valid and usable.

A record can therefore have:

`STATUS = CRITICAL`

and

`DATA_VALID = TRUE`

because a critical environmental condition can still be a valid sensor reading.

### 8. dbt Transformation Models

The project currently contains four main dbt models:

1. `stg_sensor_data`
   - Cleans and validates raw sensor data.
   - Removes duplicate records in the staging layer.

2. `stg_commodity_prices`
   - Cleans the mock commodity pricing data.

3. `stg_sensor_commodity`
   - Combines sensor data with commodity pricing scenarios.

4. `spoilage_risk`
   - Calculates spoilage risk level.
   - Calculates spoilage risk score.
   - Calculates potential spoilage arbitrage per kilogram.

### 9. Spoilage Risk Logic

The current project logic is:

| Container Status | Risk Level | Risk Score |
|---|---|---:|
| CRITICAL | High | 90 |
| WARNING | Medium | 60 |
| NORMAL | Low | 20 |

### 10. Spoilage Arbitrage

The project calculates:

`Spoilage Arbitrage per KG = Secondary Market Price - Origin Market Price`

The commodity pricing data used in this project is mock/project data for analytics demonstration.

### 11. dbt Validation Result

The latest dbt validation was successful.

- Data-quality tests: **15/15 passed**
- Warnings: **0**
- Errors: **0**
- dbt models executed successfully: **4/4**

### 12. Superset Dashboard

The AtmoSync Superset dashboard contains 16 visualizations covering:

- Temperature trend
- Humidity trend
- Vibration trend
- Total sensor records
- Average temperature
- Average humidity
- Average vibration
- Critical containers
- Warning containers
- Spoilage risk distribution
- Average spoilage risk score
- Arbitrage by commodity
- Origin vs secondary market price
- Average spoilage arbitrage per KG
- Risk score by container
- Risk and arbitrage details

### 13. Live Demonstration Sequence

The Mid Review demonstration will follow this order:

1. Show the VS Code project structure.
2. Show the Python IoT simulator.
3. Show Kafka running through Docker.
4. Show the `sensor-data` Kafka topic and sensor messages.
5. Show Snowflake `RAW.SENSOR_DATA`.
6. Show dbt models.
7. Run/show `dbt test` with 15/15 tests passed.
8. Show the `spoilage_risk` model output.
9. Open the Superset dashboard.
10. Explain the main risk and arbitrage visualizations.
11. Show the GitHub repository and commit history.

### 14. Project Explanation

“My project is AtmoSync: Micro-Climate Arbitrage Analytics. It monitors simulated temperature, humidity and vibration data from shipping containers. Python generates the sensor data, Kafka streams it through the sensor-data topic, and Snowflake stores the raw records. I use dbt to clean and transform the data and combine it with mock commodity pricing data. The transformed data is visualized in Apache Superset through an interactive analytics dashboard. The overall pipeline is Python → Kafka → Snowflake → dbt → Superset.”

### 15. Individual Contribution

I worked individually on the AtmoSync implementation and handled the project pipeline including:

- Python IoT simulator
- Sensor validation
- Kafka producer and streaming setup
- Docker Kafka configuration
- Snowflake database and raw table
- Kafka-to-Snowflake ingestion
- dbt staging models
- Commodity pricing integration
- Spoilage risk analytics
- dbt data-quality tests
- Superset dashboard
- GitHub version control
- Project documentation

### 16. Mid-Review Readiness Checklist

- [x] Python IoT simulator
- [x] Sensor validation
- [x] Kafka streaming
- [x] Snowflake storage
- [x] dbt transformation
- [x] dbt data-quality tests
- [x] Spoilage risk model
- [x] Superset dashboard
- [x] GitHub repository
- [x] Project README
- [x] Week 1 and Week 2 implementation
- [x] Live demonstration preparation
- [x] Project explanation preparation

## Overall Pipeline

**Generate → Stream → Store → Transform → Test → Visualize**

**Python → Kafka → Snowflake → dbt → Superset**