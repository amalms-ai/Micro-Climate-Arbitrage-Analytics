# AtmoSync: Micro-Climate Arbitrage Analytics

AtmoSync is a data analytics project that monitors micro-climate conditions inside shipping containers and analyzes sensor data to identify potential spoilage risks and arbitrage opportunities.

## Project Overview

The project simulates IoT sensor data such as temperature, humidity, and vibration for containers. The data is streamed through Apache Kafka, stored in Snowflake, and visualized using Apache Superset.

The project pipeline is:

Python IoT Simulator → Apache Kafka → Snowflake → Apache Superset

## Technologies Used

- Python
- Apache Kafka
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