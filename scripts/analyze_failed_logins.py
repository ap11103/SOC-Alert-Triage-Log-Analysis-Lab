from collections import Counter, defaultdict
from pathlib import Path

LOG_FILE = Path("../sample-logs/failed_logins.log")

FAILED_THRESHOLD = 5

failed_by_ip = Counter()
failed_by_user = Counter()
targeted_users_by_ip = defaultdict(set)
total_failed = 0
total_successful = 0

if not LOG_FILE.exists():
    raise FileNotFoundError(f"Log file not found: {LOG_FILE}")

with LOG_FILE.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if "FAILED LOGIN" in line:
            total_failed += 1

            parts = line.split()
            user = None
            src_ip = None

            for part in parts:
                if part.startswith("user="):
                    user = part.replace("user=", "")
                if part.startswith("src_ip="):
                    src_ip = part.replace("src_ip=", "")

            if user:
                failed_by_user[user] += 1

            if src_ip:
                failed_by_ip[src_ip] += 1
                if user:
                    targeted_users_by_ip[src_ip].add(user)

        elif "SUCCESSFUL LOGIN" in line:
            total_successful += 1

print("SOC Failed Login Analysis Summary")
print("=" * 40)
print(f"Total failed logins: {total_failed}")
print(f"Total successful logins: {total_successful}")
print()

print("Failed logins by source IP:")
for ip, count in failed_by_ip.most_common():
    status = "SUSPICIOUS" if count >= FAILED_THRESHOLD else "Normal/Review"
    print(f"- {ip}: {count} failed attempts [{status}]")

print()
print("Failed logins by targeted user:")
for user, count in failed_by_user.most_common():
    print(f"- {user}: {count} failed attempts")

print()
print("Potential brute force indicators:")
for ip, count in failed_by_ip.items():
    targeted_users = targeted_users_by_ip[ip]
    if count >= FAILED_THRESHOLD or len(targeted_users) >= 3:
        print(
            f"- {ip} targeted {len(targeted_users)} account(s): "
            f"{', '.join(sorted(targeted_users))}"
        )