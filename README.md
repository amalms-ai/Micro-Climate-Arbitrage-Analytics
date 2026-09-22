# AtmoSync: Micro-Climate Arbitrage Analytics

AtmoSync is a data analytics project that monitors micro-climate conditions inside shipping containers and analyzes sensor data to identify potential spoilage risks and arbitrage opportunities.

## Project Overview

The project simulates IoT sensor data such as temperature, humidity, and vibration for containers. The data is streamed through Apache Kafka, stored in Snowflake, and visualized using Apache Superset.

The project pipeline is:

Python IoT Simulator → Apache Kafka → Snowflake → dbt → Apache Superset

## Technologies Used

- Python
- Apache Kafka
- dbt
- Docker
- Snowflake
- Apache Superset
- SQL
- Git & GitHub


## Sensor Data

The IoT simulator generates:

- Container ID
- Timestamp
- Temperature
- Humidity
- Vibration
- Container Status
- Data Validation Status

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

## Kafka Streaming

Apache Kafka is used to stream sensor records through the `sensor-data` topic.

The Kafka producer converts sensor records into JSON-compatible messages and sends them to the Kafka topic.

## Snowflake Data Warehouse

Sensor data from Kafka is inserted into Snowflake.

Database structure:

```text
ATMOSYNC_DB
└── RAW
    └── SENSOR_DATA


## dbt Transformation

dbt (data build tool) is used as the transformation layer between Snowflake and Apache Superset.

The first dbt staging model is:

`models/staging/stg_sensor_data.sql`

The staging model reads sensor data from:

`ATMOSYNC_DB.RAW.SENSOR_DATA`

and creates the following Snowflake view:

`ATMOSYNC_DB.RAW.STG_SENSOR_DATA`

The staging model:
- Selects the required sensor fields
- Removes records without a container ID
- Removes records without a timestamp
- Provides a clean dataset for future analytics models

The dbt model was successfully tested with:

`dbt run`

Result:

`PASS=1 WARN=0 ERROR=0`

The staged data was also verified using:

`dbt show --select stg_sensor_data --limit 5`