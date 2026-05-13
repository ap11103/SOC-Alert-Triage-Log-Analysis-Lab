from datetime import datetime, timedelta
import random

start_time = datetime(2026, 5, 14, 16, 0, 0)

internal_hosts = [
    "10.0.4.12",
    "10.0.4.18",
    "10.0.5.22"
]

normal_destinations = [
    ("172.217.1.14", 443),
    ("8.8.8.8", 53),
    ("13.107.42.16", 443),
]

suspicious_destinations = [
    ("185.243.115.84", 4444),
    ("91.240.118.172", 8080),
    ("45.83.64.1", 1337),
]

events = []

# Normal traffic
for i in range(12):
    timestamp = start_time + timedelta(minutes=i)

    src = random.choice(internal_hosts)
    dst, port = random.choice(normal_destinations)

    events.append(
        f"{timestamp} ALLOW src={src} dst={dst} port={port} protocol=TCP"
    )

# Suspicious traffic
attack_time = start_time + timedelta(minutes=20)

for i in range(8):
    timestamp = attack_time + timedelta(seconds=i * 40)

    src = random.choice(internal_hosts)
    dst, port = random.choice(suspicious_destinations)

    events.append(
        f"{timestamp} ALERT src={src} dst={dst} port={port} protocol=TCP"
    )

events.sort()

with open("../sample-logs/suspicious_network.log", "w") as file:
    for event in events:
        file.write(event + "\n")

print("Generated suspicious_network.log")