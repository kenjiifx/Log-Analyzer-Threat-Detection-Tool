from collections import defaultdict
from rules import SSH_FAILED_REGEX, SSH_ACCEPTED_REGEX

FAILED_THRESHOLD = 5  # brute-force threshold


def analyze_log(file_path: str) -> dict:
    failed_attempts = defaultdict(int)
    successful_logins = set()

    with open(file_path, "r", encoding="utf-8") as log_file:
        for line in log_file:
            failed_match = SSH_FAILED_REGEX.search(line)
            success_match = SSH_ACCEPTED_REGEX.search(line)

            if failed_match:
                ip = failed_match.group("ip")
                failed_attempts[ip] += 1

            if success_match:
                ip = success_match.group("ip")
                successful_logins.add(ip)

    alerts = []

    for ip, count in failed_attempts.items():
        if count >= FAILED_THRESHOLD:
            severity = "HIGH" if count >= 10 else "MEDIUM"
            alerts.append({
                "ip": ip,
                "failed_attempts": count,
                "severity": severity
            })

    for ip in successful_logins:
        if ip in failed_attempts:
            alerts.append({
                "ip": ip,
                "failed_attempts": failed_attempts[ip],
                "severity": "CRITICAL"
            })

    return {
        "alerts": alerts
    }
