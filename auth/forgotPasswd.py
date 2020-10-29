import smtplib
import os

EMAIL_ADDRESS  = "support@quantml.org"

def send(email, OTP):
    # Replace smtp_username with your Amazon SES SMTP user name.
    USERNAME_SMTP = os.environ.get('QUANTMLAWSSMTPUSERNAME')

    # Replace smtp_password with your Amazon SES SMTP password.
    PASSWORD_SMTP = os.environ.get('QUANTMLAWSSMTPPASSWORD')

    HOST = "email-smtp.us-east-2.amazonaws.com"
    PORT = 587

    subject = "One Time Password to reset your Password for Statistics App"
    body    = f'OTP: {OTP}, This is your OTP(One Time Password) to reset your password.'
    msg     = f'Subject: {subject}\n\n{body}'

    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(EMAIL_ADDRESS, email, msg)
        server.close()
        return True
    except Exception as e:
        return False
