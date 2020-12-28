from typing import Dict, Union
import json
import smtplib
import os
import numpy as np
from hashlib import sha256
from auth.forgotPasswd import send

def hashPasswd(passwd: str) -> str:
    h = sha256()
    h.update(passwd.encode())
    H = h.hexdigest()
    return H

def read_JSON(path: str) -> Union[Dict[str, Dict[str, Union[str, int, Dict[str, int]]]], Dict[str, str]]:
    with open(path) as f:
        data = f.read()
    f.close()
    return json.loads(data)

def write_JSON(json_file: dict, path: str) -> None:
    with open(path, 'w+') as f:
        json.dump(json_file, indent=4, sort_keys=False, fp=f)
    f.close()

def sendOTP(state, email: str) -> int:
    state.experimental_rerun = True
    # noinspection PyArgumentList
    np.random.seed()
    OTP = np.random.randint(100001, 999999)
    send(email, OTP)
    return OTP

# Replace send_hold() -> send()
# noinspection SpellCheckingInspection
def send_email_hold(email, subject, msg):
    EMAIL_ADDRESS = "support@quantml.org"
    if email is None: email = EMAIL_ADDRESS
    # Replace smtp_username with your Amazon SES SMTP user name.
    USERNAME_SMTP = os.environ.get('QUANTMLAWSSMTPUSERNAME')

    # Replace smtp_password with your Amazon SES SMTP password.
    PASSWORD_SMTP = os.environ.get('QUANTMLAWSSMTPPASSWORD')

    HOST = "email-smtp.us-east-2.amazonaws.com"
    PORT = 587

    # noinspection PyBroadException
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        # stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(EMAIL_ADDRESS, email, f'Subject: {subject}\n\n{msg}')
        server.close()
        return True
    except Exception:
        return False


# noinspection SpellCheckingInspection
def send_email(user_email, subject, msg):
    EMAIL_ADDRESS = "quantml.app@gmail.com"  # os.environ.get('QUANTMLSTATISTICSEMAILADDR')
    EMAIL_PASSWORD = "gqmaaogffbgamhkp"  # os.environ.get('QUANTMLSTATISTICSEMAILPASS')
    if user_email is None: user_email = EMAIL_ADDRESS
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return smtp.sendmail(EMAIL_ADDRESS, user_email, f'Subject: {subject}\n\n{msg}')
