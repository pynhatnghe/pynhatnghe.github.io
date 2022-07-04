import smtplib


def send_mail(to, subject, content):
    gmail_user = 'pynhatnghe@gmail.com'
    gmail_password = 'P@44w0rd'
    sent_from = gmail_user
    body = 'This is an email send by NhatNghe Python App'
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sent_from, ", ".join(to), subject, content)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except Exception as e:
        print(e)
        print('Something went wrong...')


# Gửi mail
send_mail(
    ['pynhatnghe@gmail.com', 'aspnhatnghe@gmail.com'],
    'Python 06-06-2022',
    "Chúc mừng bạn trúng thưởng"
)