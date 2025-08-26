import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
gmail_server.ehlo()
gmail_server.starttls()

def login_to_gmail(email, password):
    gmail_server.login(email, password)

def send_email( myemail ,subject, body, to , file=None , image=None):
    msg = MIMEMultipart()
    msg['From'] = myemail
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    gmail_server.send_message(msg , MIMEImage(image) if image else None , file)
    del msg


def logout_from_gmail():
    gmail_server.quit()