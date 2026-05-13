# Suspicious Network Traffic Investigation

## Incident Summary

Suspicious outbound network traffic was identified involving connections to uncommon external IP addresses and high-risk ports commonly associated with command-and-control (C2) communication.

---

## Detection Details

### Suspicious Indicators
- Outbound traffic to uncommon external IP addresses
- Connections over non-standard ports
- Repeated communication attempts
- ALERT-triggered network events

### Observed Destination IPs
- 185.243.115.84
- 91.240.118.172
- 45.83.64.1

### Suspicious Ports
- 4444
- 8080
- 1337

---

## Analysis

The observed outbound traffic patterns may indicate command-and-control activity or unauthorized external communications.

Several connections were initiated to suspicious external IP addresses over ports frequently associated with malware communications, remote access tools, or attacker-controlled infrastructure.

The repeated outbound communication attempts warrant further investigation into potentially compromised endpoints.

---

## MITRE ATT&CK Mapping

| Technique | Description |
|---|---|
| T1071 | Application Layer Protocol |
| T1095 | Non-Application Layer Protocol |
| T1571 | Non-Standard Port |

---

## Risk Assessment

### Risk Level
High

### Potential Impact
Potential attacker-controlled outbound communication could enable data exfiltration, malware staging, persistence, or remote command execution.

---

## Recommended Actions

- Investigate affected endpoints
- Block suspicious destination IPs
- Restrict unnecessary outbound traffic
- Review firewall and proxy logs
- Monitor unusual outbound connections

---

## Conclusion

The observed network activity demonstrates suspicious outbound communication behavior potentially consistent with command-and-control traffic or unauthorized external connections.