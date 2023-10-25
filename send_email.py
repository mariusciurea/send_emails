"""This is a simple script that receives the following information as input

    - e-mail sender
    - e-mail receiver
    - e-mail subject
    - e-mail body

    It finally sends an e-mail from e-mail sender address (gmail) to e-mail receiver address (any email
    service)
"""
import ssl
import smtplib
from email.message import EmailMessage
from configparser import ConfigParser


def get_config_data():
    """Get the configuration data from config.ini file
    """

    cfg = ConfigParser()
    cfg.read('config.ini')
    return cfg['mail_details']['password']


def send_mail(message: EmailMessage, mail_from, mail_to, password, attachment=None):
    """Send an e-mail message from a gmail account to any other type of e-mail service
    """

    # adding security
    c = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=c) as email_smtp:
            email_smtp.login(mail_from, password)
            email_smtp.sendmail(mail_from, mail_to, message.as_string())
    except smtplib.SMTPException as e:
        print(e)
    except Exception:
        SystemExit(2)


if __name__ == '__main__':
    mail_sender = input('e-mail from: ')
    mail_receiver = input('e-mail to: ')
    subject = input('e-mail subject: ')
    body = input('e-mail body: ')

    # Create an instance of EmailMessage()
    msg = EmailMessage()
    msg['From'] = mail_sender
    msg['To'] = mail_receiver
    msg['Subject'] = subject
    msg.set_content(body)

    # Get the password from config.ini file
    password = get_config_data()

    # send the e-mail
    send_mail(msg, mail_sender, mail_receiver, password)
