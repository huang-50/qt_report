import sys
import report

if __name__ == '__main__':
    try:
        report_path = sys.argv[1]
        report = report.ReportSystem(report_path)
        report.run()
    except Exception as e:
        sys.exit(e.msg)
    