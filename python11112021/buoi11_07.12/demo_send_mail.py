import smtplib
import logging
from datetime import datetime

# Set name of log
logging.getLogger("PyNhatNghe")

# Setup log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d: %(message)s",
    filename='appsendmail_{:%Y_%m_%d}.log'.format(datetime.utcnow())
)

gmail_user = "pynhatnghe@gmail.com"
gmail_pass = "AAA"

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
