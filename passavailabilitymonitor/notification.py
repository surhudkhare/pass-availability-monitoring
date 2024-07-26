import smtplib
from email.mime.text import MIMEText
import os
import subprocess
from passavailabilitymonitor.utils import get_time

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

def send_desktop_notification(title, message):
    # TODO: Add sound
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(['osascript', '-e', script])


def notify(mode="desktop"):
    subject = 'GO GO GO'
    message = f'{get_time()}\nThe passes are now available! Check the website'
    if mode == 'email':
        send_email_notifications(os.getenv('TO_EMAIL'), subject, message)
    elif mode == "desktop":
        send_desktop_notification(subject, message)
    else:
        raise ValueError("Invalid notification mode")


if __name__ == "__main__":
    notify()