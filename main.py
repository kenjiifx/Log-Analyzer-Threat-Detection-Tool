from analyzer import analyze_log
from report import generate_report


def main():
    log_file = "sample.log"
    results = analyze_log(log_file)
    generate_report(results)


if __name__ == "__main__":
    main()
