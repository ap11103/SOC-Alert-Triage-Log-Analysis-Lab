# SOC-Alert-Triage-Log-Analysis-Lab
SOC alert triage and log analysis project focused on incident investigation, suspicious activity detection, and MITRE ATT&amp;CK mapping.

## Overview
This project demonstrates foundational SOC analyst workflows including:

- Alert triage
- Log analysis
- Incident investigation
- IOC identification
- MITRE ATT&CK mapping
- Security event documentation

The goal of this lab is to simulate common security incidents and document the analysis process used to investigate suspicious activity.

---

## Project Structure

### sample-logs/
Contains simulated security logs including:
- Failed authentication attempts
- Suspicious PowerShell execution
- Network connection anomalies

### incident-reports/
Contains documented incident investigations and findings.

### detection-notes/
Contains MITRE ATT&CK mappings, indicators of compromise (IOCs), and analysis notes.

### screenshots/
Contains screenshots related to analysis and investigation workflows.

---

## Simulated Scenarios

### Brute Force Authentication Investigation
- Simulated repeated failed login attempts targeting privileged accounts
- Identified suspicious external IP activity
- Documented findings and mitigation recommendations
- Mapped activity to MITRE ATT&CK techniques

### Planned Scenarios
- Suspicious PowerShell execution
- Suspicious outbound network traffic
- IOC investigation and detection analysis

---

## Automation

This project includes Python-based log generation and analysis scripts used to simulate and investigate security events.

### Current Automation
- Simulated failed login log generation
- Automated failed login analysis
- Suspicious IP identification
- Authentication event summarization

### Example Script Execution

```bash
python scripts/analyze_failed_logins.py
```

## Skills Demonstrated

- Security event triage
- Log correlation
- Threat analysis
- Incident documentation
- Security operations workflows
- Analytical problem solving

---

## Tools & Concepts

- Windows Event Logs
- PowerShell Analysis
- MITRE ATT&CK Framework
- IOC Investigation
- SOC Operations Concepts
