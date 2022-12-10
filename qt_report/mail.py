import os
try:
    import w32com.client as win32
except ImportError:
    win32 = None

#send mail via outlook
def send_mail_outlook(sender, receiver, subject, body, attachment=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = receiver
    mail.Subject = subject
    mail.HTMLBody = body
    # flag as automation email
    mail.FlagRequest = 'automation:do-not-reply'
    # attachment
    if attachment:
        mail.Attachments.Add(attachment)
    mail.Send()

#send mail via smtp
def send_mail_smtp(sender, receiver, subject, body, attachment=None):
    import smtplib
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # create message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    # attachment
    if attachment:
        filename = os.path.basename(attachment)
        attachment = open(attachment, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
        msg.attach(part)
    # send mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, 'password')
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

def send_mail(sender, receiver, subject, body, attachment=None):
    #check if outlook is installed
    if os.path.exists('C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'):
        send_mail_outlook(sender, receiver, subject, body, attachment)
    else:
        send_mail_smtp(sender, receiver, subject, body, attachment)
