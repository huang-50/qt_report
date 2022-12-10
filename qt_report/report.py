import pandas as pd

from app_config import AppConfig
from email import send_mail
from report_config import get_report_config
from db import get_db_connection
from view import View

class ReportSystem:
    def __init__(self, report_path):
        self.report_path = report_path
        self.app_config = AppConfig()
        self.report, self.Queries = get_report_config(report_path)
        self.db_connection = get_db_connection(self.report.db, self.app_config.Databases)
        self.view = View(self.app_config)

    def _exec_query(self, sql):
        df = pd.read_sql(sql, self.db_connection)
        # formating the data
        df.fillna('', inplace=True)
        # number format
        pd.options.display.float_format = '{:,.2f}'.format
        # set index start from 1
        df.index = df.index + 1
        return df

    def generate_report(self):
        self.view.set_html_header(self.report.subject)
        for query in self.Queries:
            df = self._exec_query(query.sql)
            self.view.add_section(query.title, df, query.note)
        self.view.set_html_footer(self.report.footer)
        return self.view.get_html()

    def run(self):
        html = self.generate_report()
        send_mail(self.app_config.mail_from, self.app_config.mail_to, self.report.subject, html, self.report.attachment)