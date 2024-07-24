import smtplib
from email.mime.text import MIMEText
import os

def send_email_notifications(to_email, subject, message):
    from_email = os.getenv('SENDER_USERNAME')
    password = os.getenv('SENDER_PASSWORD')

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

def notify():
    subject = 'GO GO GO'
    message = 'The passes are now available! Check the website.'
    send_email_notifications(os.getenv('TO_EMAIL'), subject, message)