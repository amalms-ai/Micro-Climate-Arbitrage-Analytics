import random
from datetime import datetime


def check_container_status(temperature, humidity, vibration):
    if temperature > 8 or humidity > 85 or vibration > 0.8:
        return "Critical"

    elif temperature > 6 or humidity > 75 or vibration > 0.5:
        return "Warning"

    else:
        return "Normal"


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

    sensor_data = {
        "container_id": container_id,
        "timestamp": datetime.now().isoformat(),
        "temperature": temperature,
        "humidity": humidity,
        "vibration": vibration,
        "status": status
    }

    return sensor_data


if __name__ == "__main__":
    for _ in range(5):
        data = generate_sensor_data()
        print(data)