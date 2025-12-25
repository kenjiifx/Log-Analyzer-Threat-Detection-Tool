from datetime import datetime


def generate_report(results: dict, output_file: str = "report.txt") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_file, "w", encoding="utf-8") as report:
        report.write(f"Log Analysis Report\n")
        report.write(f"Generated at: {timestamp}\n")
        report.write("-" * 40 + "\n")

        if not results["alerts"]:
            report.write("No anomalies detected.\n")
            return

        for alert in results["alerts"]:
            report.write(
                f"IP: {alert['ip']} | "
                f"Failed Attempts: {alert['failed_attempts']} | "
                f"Severity: {alert['severity']}\n"
            )
