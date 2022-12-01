import configparser
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read('config.ini')


def send_email():
    server = smtplib.SMTP(config['SMTP']['smtp'], config['SMTP']['port'])
    server.starttls()
    server.login(config['SMTP']['email'], config['SMTP']['password'])

    message = MIMEMultipart("alternative")
    message["Subject"] = "Notices ETFBL"
    message["From"] = config['SMTP']['email']
    message["To"] = config['SMTP']['user_email']
    part = MIMEText("You can find ETFBL notices attached in a json file.", "plain")
    message.attach(part)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("notices.json", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Transfer-Encoding', 'base64')
    part.add_header('Content-Disposition', 'attachment; filename=notices-etfbl.json')
    message.attach(part)

    server.sendmail(from_addr=config['SMTP']['email'], to_addrs=config['SMTP']['user_email'], msg=message.as_string())
    server.quit()
