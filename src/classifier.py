class IncidentClassifier:
    def __init__(self):
        self.real_issue_keywords = [
            "timeout", "unavailable", "null pointer", "exception", "crash", "failure", "refused", "error"
        ]
        self.low_priority_keywords = [
            "slow", "latency", "retry", "threshold", "delay", "warn"
        ]

    def classify(self, row):
        message = f"{row.get('error_message', '')} {row.get('additional_info', '')}".lower()
        severity = row.get("severity", "").upper()

        # Rule-based logic
        if any(kw in message for kw in self.real_issue_keywords):
            return "Real Issue", 0.9
        elif any(kw in message for kw in self.low_priority_keywords) or severity == "WARN":
            return "Informational / Low Priority", 0.6
        elif severity in ["INFO", "DEBUG"]:
            return "False Positive", 0.5
        else:
            return "Real Issue", 0.7  # default fallback