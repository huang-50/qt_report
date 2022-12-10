import logging
import os
import unittest
import yaml

class ReportConfig:
    def __init__(self, filename):
        with open(filename, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)
        self.subject = self.config['subject']
        self.db = self.config['db']
        self.mailto = self.config['mailto']

class QueryConfig:
    def __init__(self, filename):
        with open(filename, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)
        self.title = self.config['title']
        self.sql = self.config['sql']
        self.note = self.config['note']

def get_report_config(report_path):
    report=None
    queries=[]
    for filename in os.listdir(report_path):
        if filename.endswith(".yaml"):
            if filename == "report.yaml":
                report = ReportConfig(os.path.join(report_path, filename))
            else:
                queries.append(QueryConfig(os.path.join(report_path, filename)))
    return report, queries    

class TestReportConfig(unittest.TestCase):
    def test_report_config(self):
        report = ReportConfig("../query/sample_report_1/report.yaml")
        assert report.subject == "Q-Tip Yearly sales summary"
        assert report.db == "sample_db"
        assert report.mailto == "albert_huang@qq.com"
    
    def test_query_config(self):
        query = QueryConfig("../query/sample_report_1/1_sales_summary.yaml")
        assert query.title == "Year 2022 Sales Summary"

    def test_get_report_config(self):
        report, queries = get_report_config("../query/sample_report_1")
        assert report.subject == "Q-Tip Yearly sales summary"
        assert report.db == "sample_db"
        assert queries[0].title == "Year 2022 Sales Summary"
    