import configparser
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')


def send_email():
    if os.path.exists(config['SCRAPER']['notices']):
        server = smtplib.SMTP(config['SMTP']['smtp'], config['SMTP']['port'])
        server.starttls()
        server.login(config['SMTP']['email'], config['SMTP']['password'])

        message = MIMEMultipart("alternative")
        message["Subject"] = config['SMTP']['subject']
        message["From"] = config['SMTP']['email']
        message["To"] = config['SMTP']['user_email']
        part = MIMEText(config['SMTP']['text'], "plain")
        message.attach(part)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(config['SCRAPER']['notices'], "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Transfer-Encoding', 'base64')
        part.add_header('Content-Disposition', f"'attachment; filename={config['SCRAPER']['notices']}")
        message.attach(part)

        server.sendmail(from_addr=config['SMTP']['email'], to_addrs=config['SMTP']['user_email'],
                        msg=message.as_string())
        server.quit()
