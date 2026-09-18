import json
import time

from kafka import KafkaProducer
from simulator.iot_simulator import generate_sensor_data


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)


if __name__ == "__main__":

    for i in range(5):
        sensor_data = generate_sensor_data()

        producer.send(
            "sensor-data",
            value=sensor_data
        )

        print("Sent to Kafka:", sensor_data)

        time.sleep(1)

    producer.flush()
    producer.close()

    print("All sensor data sent successfully.")