# Detection Logic Notes

## Brute Force Detection Logic

Trigger alert when:
- More than 5 failed logins occur from the same IP within a short timeframe
- Multiple privileged accounts are targeted
- Authentication attempts originate from external IP ranges

---

## Suspicious PowerShell Detection Logic

Trigger alert when:
- PowerShell uses EncodedCommand
- ExecutionPolicy Bypass is detected
- Outbound web requests are initiated from PowerShell

---

## Alert Severity Levels

| Severity | Description |
|---|---|
| Low | Suspicious but low-confidence activity |
| Medium | Potential malicious behavior requiring review |
| High | Likely malicious activity requiring escalation |

---

# Suspicious Network Traffic Detection Logic

Trigger alert when:

- Outbound traffic targets uncommon external IP addresses
- Connections occur over high-risk or non-standard ports
- Repeated outbound connection attempts are observed
- Traffic patterns deviate from normal baseline behavior