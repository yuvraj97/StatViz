import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = "no-reply@quantml.org"

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
    EMAIL_ADDRESS = "no-reply@quantml.org"  # os.environ.get('QUANTMLSTATISTICSEMAILADDR')
    # noinspection SpellCheckingInspection
    EMAIL_PASSWORD = "DpPyfmmWa4gJ"  # os.environ.get('QUANTMLSTATISTICSEMAILPASS')

    message = EmailMessage()
    message['Subject'] = "Reset Statistics Guide Password"
    message['From'] = EMAIL_ADDRESS
    message['To'] = user_email
    message.set_content("""<!DOCTYPE HTML><html lang="en"><head><style>body{font-size:14px;line-height:24px;font-family:'Open Sans','Trebuchet MS',sans-serif}.otp{font-size:22px;margin-top:20px;font-weight:800;font-style:oblique}</style></head><body><a rel='noreferrer' target='_blank' href="https://www.quantml.org" class="logo image jump-big"><img src="https://www.quantml.org/data/img/cover.png" alt="QuantML.org" width="360px" height="75px"/></a> <br> We have received a request to reset your <b>Statistics Guide</b> password. <br> Please use the following one-time password to verify yourself.<div class="otp"> """ + str(OTP) + """</div><br> Regards, <br> <a href="https://www.quantml.org">QuantML</a></body></html>""", subtype='html')

    with smtplib.SMTP_SSL('smtp.zoho.in', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return smtp.send_message(message)
