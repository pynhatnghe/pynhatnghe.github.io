import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from datetime import datetime

gmail_user = "python@gmail.com"
gmail_password = "Nh@tNghe"

# Set name of log
logging.getLogger("PyNhatNghe")

# Setup log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d: %(message)s",
    filename='appsendmail_{:%Y_%m_%d}.log'.format(datetime.utcnow())
)


# Define hàm send mail


def send_mail(receive_list, content):
    """Send mail to receive list with content."""
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, receive_list, content)
        server.close()
        print("SEND MAIL SUCCESS")
        logging.info('SEND MAIL SUCCESS')
    except Exception as ex:
        logging.error(ex)
        print(ex)


def send_mail_html_format(receive_list, subject, content):
    """Send mail to receive list with content."""
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = gmail_user
        message["To"] = ",".join(receive_list)

        # Set format email plain/html MIMEText objects
        part = MIMEText(content, "html")
        message.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(
                gmail_user,  ",".join(receive_list), message.as_string()
            )
        print("SEND MAIL HTML SUCCESS")
        logging.info('SEND MAIL SUCCESS')
    except Exception as ex:
        logging.error(ex)
        print(ex)


if __name__ == "__main__":
    message = """\
Subject: Send test mail,

This message is sent from Python."""
    #send_mail(["pynhatnghe@gmail.com", "hyhien@gmail.com"], message)

    # Demo send mail with html format
    html = """\
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>

        <h1>Hello <span style='color:red'>PyNhatNghe</span></h1>
        <p>Day la email test gui tu <b>agilehcmue@gmail.com</b>.</p>

        </body>
        </html>
        """
    send_mail_html_format(
        ["pynhatnghe@gmail.com", "hyhien@gmail.com"], "SEND MAIL GROUP", html)
