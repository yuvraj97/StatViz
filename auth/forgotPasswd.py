import smtplib
import os

EMAIL_ADDRESS = "support@quantml.org"

# Replace send_hold() -> send()
def send_hold(email, OTP):
    # Replace smtp_username with your Amazon SES SMTP user name.
    # noinspection SpellCheckingInspection
    USERNAME_SMTP = os.environ.get('QUANTMLAWSSMTPUSERNAME')

    # Replace smtp_password with your Amazon SES SMTP password.
    # noinspection SpellCheckingInspection
    PASSWORD_SMTP = os.environ.get('QUANTMLAWSSMTPPASSWORD')

    # noinspection SpellCheckingInspection
    HOST = "email-smtp.us-east-2.amazonaws.com"
    PORT = 587

    subject = "One Time Password to reset your Password for Statistics App"
    body = f'OTP: {OTP}, This is your OTP(One Time Password) to reset your password.'
    msg = f'Subject: {subject}\n\n{body}'

    # noinspection PyBroadException
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        # stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(EMAIL_ADDRESS, email, msg)
        server.close()
        return True
    except Exception:
        return False

def send(user_email, OTP):
    # noinspection SpellCheckingInspection,PyShadowingNames
    EMAIL_ADDRESS = "quantml.app@gmail.com"  # os.environ.get('QUANTMLSTATISTICSEMAILADDR')
    # noinspection SpellCheckingInspection
    EMAIL_PASSWORD = "xmqlztccyguwvhax"  # os.environ.get('QUANTMLSTATISTICSEMAILPASS')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = "One Time Password to reset your Password for Statistics App"
        body    = f'OTP: {OTP}, This is your OTP(One Time Password) to reset your password.'
        msg     = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, user_email, msg)
