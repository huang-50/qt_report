import unittest
# from context import qt_report
from qt_report.report_config import get_report_config, ReportConfig, QueryConfig
# .report_config import ReportConfig, QueryConfig, get_report_config

class TestReportConfig(unittest.TestCase):
    def test_report_config(self):
        report = ReportConfig("./query/sample_report_1/report.yaml")
        assert report.subject == "Q-Tip Yearly sales summary"
        assert report.db == "sample_db"
        assert report.mailto == "albert_huang@qq.com"
    
    def test_query_config(self):
        query = QueryConfig("./query/sample_report_1/1_sales_summary.yaml")
        assert query.title == "Year 2022 Sales Summary"

    def test_get_report_config(self):
        report, queries = get_report_config("./query/sample_report_1")
        assert report.subject == "Q-Tip Yearly sales summary"
        assert report.db == "sample_db"
        assert queries[0].title == "Year 2022 Sales Summary"
    