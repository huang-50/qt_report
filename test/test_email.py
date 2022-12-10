import unittest
from qt_report.mail import send_mail

class TestMail(unittest.TestCase):
    def test_send_mail(self):
        send_mail('albert_huang@gmail.com',
            '830223@qq.com',
            'test',
            '<h1>test</h1>'
        )
        
    

