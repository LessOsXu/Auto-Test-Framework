from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(html_file):
    with open(html_file, 'rb') as f:
        mail_body = f.read()

    sender = 'zzz@zzz.com'
    mail_host = "xxx.com"
    mail_user = "xxx@xxx.com"
    mail_pass = "xxxxxx"
    receivers = ['aaa@aaa.com']
    
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(";".join(receivers))

    subject = 'UnitTest Test Result'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        # 25 为 SMTP 端口号
        smtpObj.connect(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("Send email to %s succeed" % email_address)
    except smtplib.SMTPException as e:
        print("Error: send email to %s failed" % email_address)
        print(e)
