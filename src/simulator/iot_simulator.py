import random
import csv
import os
import time
import json
from datetime import datetime
from kafka import KafkaProducer


def check_container_status(temperature, humidity, vibration):
    if temperature > 8 or humidity > 85 or vibration > 0.8:
        return "Critical"

    elif temperature > 6 or humidity > 75 or vibration > 0.5:
        return "Warning"

    else:
        return "Normal"

def validate_sensor_data(temperature, humidity, vibration):
    if (
        2 <= temperature <= 10
        and 60 <= humidity <= 90
        and 0 <= vibration <= 1
    ):
        return True

    return False


def generate_sensor_data():
    container_id = f"CONT_{random.randint(1, 10):03d}"

    temperature = round(random.uniform(2, 10), 2)
    humidity = round(random.uniform(60, 90), 2)
    vibration = round(random.uniform(0, 1), 2)

    status = check_container_status(
        temperature,
        humidity,
        vibration
    )

    data_valid = validate_sensor_data(
        temperature,
        humidity,
        vibration
    )

    sensor_data = {
        "container_id": container_id,
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "status": status,
        "data_valid": data_valid
    }

    sensor_data["data_valid"] = validate_sensor_record(sensor_data)

    return sensor_data
def validate_sensor_record(sensor_data):
    required_fields = [
        "container_id",
        "timestamp",
        "temperature",
        "humidity",
        "vibration",
        "status"
    ]

    for field in required_fields:
        if field not in sensor_data:
            return False

    if not isinstance(sensor_data["temperature"], (int, float)):
        return False

    if not isinstance(sensor_data["humidity"], (int, float)):
        return False

    if not isinstance(sensor_data["vibration"], (int, float)):
        return False

    if not 0 <= sensor_data["humidity"] <= 100:
        return False

    if sensor_data["vibration"] < 0:
        return False

    return True


def save_to_csv(sensor_data_list):
    os.makedirs("data", exist_ok=True)

    file_path = "data/sensor_data.csv"

    fieldnames = [
    "container_id",
    "timestamp",
    "temperature",
    "humidity",
    "vibration",
    "status",
    "data_valid"
]

    with open(file_path, "w", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(sensor_data_list)

    print(f"Sensor data saved to {file_path}")

def save_to_json(sensor_data_list):
    os.makedirs("data", exist_ok=True)

    file_path = "data/sensor_data.json"

    with open(file_path, "w") as json_file:
        json.dump(
            sensor_data_list,
            json_file,
            indent=4
        )

    print(f"Sensor data saved to {file_path}")

def prepare_kafka_message(sensor_data):
    return json.dumps(sensor_data)

def create_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    return producer

if __name__ == "__main__":
    producer = create_kafka_producer()
    topic_name = "sensor-data"

    sensor_data_list = []

    for _ in range(5):
        data = generate_sensor_data()
        sensor_data_list.append(data)

        kafka_message = prepare_kafka_message(data)

        producer.send(topic_name, value=data)
        producer.flush()

        print("Sensor Data:")
        print(data)

        print("Kafka Message:")
        print(kafka_message)

        print("-" * 50)

        time.sleep(2)

    save_to_csv(sensor_data_list)
    save_to_json(sensor_data_list)
    producer.close()