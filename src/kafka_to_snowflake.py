import json
import getpass
from datetime import datetime

from kafka import KafkaConsumer
import snowflake.connector


password = getpass.getpass("Enter your Snowflake password: ")



consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="atmosync-snowflake",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)



conn = snowflake.connector.connect(
    account="DYUJPYV-OG68187",
    user="AMALMS",
    password=password,
    warehouse="COMPUTE_WH",
    database="ATMOSYNC_DB",
    schema="RAW"
)

cursor = conn.cursor()



insert_sql = """
INSERT INTO ATMOSYNC_DB.RAW.SENSOR_DATA
(
    CONTAINER_ID,
    TIMESTAMP,
    TEMPERATURE,
    HUMIDITY,
    VIBRATION,
    STATUS,
    DATA_VALID
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""


print("Kafka → Snowflake pipeline started...")
print("Waiting for sensor data...")



for message in consumer:

    data = message.value

    if isinstance(data, str):
        
        data = json.loads(data)

    sensor_timestamp = datetime.fromisoformat(
        data["timestamp"]
    )

    cursor.execute(
        insert_sql,
        (
            data["container_id"],
            sensor_timestamp,
            data["temperature"],
            data["humidity"],
            data["vibration"],
            data["status"],
            data["data_valid"]
        )
    )

    conn.commit()

    print("Inserted into Snowflake:", data)