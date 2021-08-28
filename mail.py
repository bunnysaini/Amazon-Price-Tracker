import smtplib
from email.message import EmailMessage

my_email = "test@gmail.com"         # Add Email ID
password = "test"                   # Password

class NotificationManager:

    def __init__(self):
        self.email = my_email
        self.password = password

    def send_mail(self, user_address, body):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)

            msg = EmailMessage()
            msg['Subject'] = 'Alert : Low Rates !'
            msg['From'] = self.email
            msg['To'] = user_address

            msg.set_content('This is a plain text email')

            msg.add_alternative(body, subtype='html')

            connection.send_message(msg)