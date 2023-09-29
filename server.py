from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint


def generate_id() -> int:
    return int(randint(10000, 99999))


def take_key(value: str):
    with open('key.env', 'r') as file:
        for string in file:
            key_value = string.split('=')
            if key_value[0].replace(" ", '') == value:
                if key_value[1].isdigit():
                    return int(key_value[1])
                return key_value[1].rstrip()


def verify_server(to_email, text_message):
    id_msg = generate_id()
    email = take_key('EMAIL_LOGIN')
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = ', '.join([email, to_email])
    message['Subject'] = f'[Ticket #{id_msg}] Mailer'
    message.attach(MIMEText(text_message, 'plain'))

    try:
        with SMTP(take_key('SMTP_HOST'), take_key('SMTP_PORT')) as server:
            server.starttls()
            server.login(email, take_key('EMAIL_PASSWORD'))
            server.send_message(message)
        return 'OK'
    except Exception as e:
        print(e)
        return e
