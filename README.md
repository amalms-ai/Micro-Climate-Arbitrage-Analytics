# AtmoSync: Micro-Climate Arbitrage Analytics

AtmoSync is a data analytics project that monitors micro-climate conditions inside shipping containers and analyzes sensor data to identify potential spoilage risks and arbitrage opportunities.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Sensor Data](#sensor-data)
- [Data Validation](#data-validation)
- [Kafka Streaming](#kafka-streaming)
- [Snowflake Data Warehouse](#snowflake-data-warehouse)
- [dbt Transformation](#dbt-transformation)
- [Superset Analytics Dashboard](#superset-analytics-dashboard)
- [Spoilage Risk Analytics](#spoilage-risk-analytics)
- [Business Insights](#business-insights)
- [dbt Models](#dbt-models)
- [Data Quality Testing](#data-quality-testing)
- [Project Architecture](#project-architecture)
- [Final Project Flow](#final-project-flow)

---

## Project Overview

The project simulates IoT sensor data such as temperature, humidity, and vibration for containers. The data is streamed through Apache Kafka, stored in Snowflake, transformed with dbt, and visualized using Apache Superset.

The project pipeline is:

```text
Python IoT Simulator → Apache Kafka → Snowflake → dbt → Apache Superset
```

---

## Technologies Used

- Python
- Apache Kafka
- dbt
- Docker
- Snowflake
- Apache Superset
- SQL
- Git & GitHub

---

## Sensor Data

The IoT simulator generates:

- Container ID
- Timestamp
- Temperature
- Humidity
- Vibration
- Container Status
- Data Validation Status

---

## Data Validation

The system validates sensor records by checking:

- Required fields
- Numeric data types
- Humidity range
- Vibration values
- Overall record validity

Container conditions are classified as:

- Normal
- Warning
- Critical

---

## Kafka Streaming

Apache Kafka is used to stream sensor records through the `sensor-data` topic.

The Kafka producer converts sensor records into JSON-compatible messages and sends them to the Kafka topic.

---

## Snowflake Data Warehouse

Sensor data from Kafka is inserted into Snowflake.

Database structure:

```text
ATMOSYNC_DB
└── RAW
    └── SENSOR_DATA
```

---

## dbt Transformation

dbt (data build tool) is used as the transformation layer between Snowflake and Apache Superset.

The first dbt staging model is:

```text
models/staging/stg_sensor_data.sql
```

The staging model reads sensor data from:

```text
ATMOSYNC_DB.RAW.SENSOR_DATA
```

and creates the following Snowflake view:

```text
ATMOSYNC_DB.RAW.STG_SENSOR_DATA
```

The staging model:

- Selects the required sensor fields
- Removes records without a container ID
- Removes records without a timestamp
- Provides a clean dataset for future analytics models

The dbt model was successfully tested with:

```bash
dbt run
```

Result:

```text
PASS=1 WARN=0 ERROR=0
```

The staged data was also verified using:

```bash
dbt show --select stg_sensor_data --limit 5
```

---

## Superset Analytics Dashboard

The AtmoSync Superset dashboard provides interactive analytics for sensor conditions, spoilage risk, and market arbitrage.

The dashboard is connected to the Snowflake `RAW.SPOILAGE_RISK` dataset created through the dbt analytics layer.

---

## Spoilage Risk Analytics

The dashboard includes:

- Spoilage Risk Distribution
- Average Spoilage Risk Score
- Arbitrage by Commodity
- Origin vs Secondary Market Price
- Average Spoilage Arbitrage per KG
- Risk Score by Container
- Risk and Arbitrage Details

---

## Business Insights

The dashboard helps identify containers with different levels of spoilage risk and provides a clear view of environmental conditions such as temperature, humidity, and vibration.

By combining spoilage risk with commodity market prices, the system identifies potential arbitrage opportunities between the origin market and secondary market.

The dashboard also provides potential arbitrage value, rerouting recommendations, and business priority to help understand which containers may require attention.

---

## dbt Models

The project contains the following dbt models:

| Model | Description |
|---|---|
| `stg_sensor_data` | Prepares and cleans raw sensor data. |
| `stg_commodity_prices` | Prepares commodity market-price data. |
| `stg_sensor_commodity` | Combines sensor and commodity information. |
| `spoilage_risk` | Calculates spoilage risk score and risk level. |
| `spoilage_arbitrage` | Calculates arbitrage value, rerouting recommendation, and business priority. |

---

## Data Quality Testing

The complete dbt pipeline was tested using:

```bash
dbt test
```

Final result:

```text
19/19 Tests Passed
0 Warnings
0 Errors
```

This confirms that the defined data-quality checks are passing successfully.

---

## Project Architecture

The complete AtmoSync architecture is:

```text
Python IoT Simulator
        ↓
Sensor Data Generation
        ↓
JSON Data
        ↓
Apache Kafka
        ↓
Snowflake RAW
        ↓
dbt Staging Models
        ↓
Spoilage Risk
        ↓
Spoilage Arbitrage
        ↓
Superset Dashboard
```

---

## Final Project Flow

The complete AtmoSync workflow is:

```text
Generate
   ↓
Stream
   ↓
Store
   ↓
Transform
   ↓
Analyze
   ↓
Test
   ↓
Visualize
```