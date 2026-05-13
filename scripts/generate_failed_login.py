from datetime import datetime, timedelta
import random

#simulate failed login attempts with a mix of successful logins and a brute-force attack pattern
start_time = datetime(2026, 5, 14, 8, 40, 0)

users = ["admin", "administrator", "root", "guest", "jdoe", "svc_backup"]
suspicious_ips = ["185.220.101.4", "45.83.64.1", "91.240.118.172"]
internal_ips = ["10.0.4.12", "10.0.4.18", "10.0.5.22"]

events = []

#successful logins
for i in range(8):
    timestamp = start_time + timedelta(minutes=i * 3)
    user = random.choice(["jdoe", "asmith", "mchen"])
    ip = random.choice(internal_ips)
    events.append(f"{timestamp} SUCCESSFUL LOGIN user={user} src_ip={ip}")

#brute-force attack pattern
attack_time = start_time + timedelta(minutes=20)
for i in range(18):
    timestamp = attack_time + timedelta(seconds=i * random.randint(4, 9))
    user = random.choice(["admin", "administrator", "root", "guest"])
    ip = random.choice(suspicious_ips)
    events.append(f"{timestamp} FAILED LOGIN user={user} src_ip={ip}")

#additional failed attempts from an internal IP
timestamp = start_time + timedelta(minutes=55)
events.append(f"{timestamp} FAILED LOGIN user=jdoe src_ip=10.0.4.12")

events.sort()

with open("../sample-logs/failed_logins.log", "w") as file:
    for event in events:
        file.write(event + "\n")

print("Generated sample-logs/failed_logins.log")