# 🔍 Incident Classification Agent (MCP Prototype)

### Google colab project link: https://colab.research.google.com/drive/1lt3pRwrFl0jZopTJuIKCYNZPq41A1NA_?usp=sharing

This project is a prototype of an MCP (Multi-capability Prompting) agent designed to classify incident alerts from observability platforms. It automatically categorizes incoming alerts based on severity and message context, helping reduce noise and focus attention on real operational issues.

### Supported classifications:
- ✅ Real Issue  
- ⚠️ Informational / Low Priority  
- ❌ False Positive  

The agent analyzes incident metadata and error messages from a JSON input file and outputs a structured report with classification labels and confidence scores.

---

## 🧠 Why This Exists

Modern observability tools (e.g., Dynatrace, Splunk, Datadog) generate huge volumes of alerts—many of which are either low priority or false positives. This tool automates the first step of incident triage using lightweight rule-based classification, helping reduce response fatigue and streamline incident response workflows.

---

## 📦 Input Format

The agent expects a JSON file with a list of incident objects. Each object should follow this structure:

```json
{
  "incident_id": "INC001",
  "timestamp": "2025-06-20T14:30:00Z",
  "severity": "ERROR",
  "service": "UserAuthService",
  "error_message": "Database connection timeout",
  "source": "Dynatrace",
  "additional_info": "TimeoutException at DBConnection.java line 42"
}
