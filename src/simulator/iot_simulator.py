import random
from datetime import datetime


def generate_sensor_data():
    container_id = f"CONT_{random.randint(1, 10):03d}"

    temperature = round(random.uniform(2, 10), 2)
    humidity = round(random.uniform(60, 90), 2)
    vibration = round(random.uniform(0, 1), 2)

    sensor_data = {
        "container_id": container_id,
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration
    }

    return sensor_data


if __name__ == "__main__":
    for i in range(5):
        data = generate_sensor_data()
        print(data)