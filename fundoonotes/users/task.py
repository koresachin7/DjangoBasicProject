from users.models import User
from celery import shared_task
from email.message import EmailMessage
import smtplib
from django.conf import settings


@shared_task(bind=True)
def send_mail(self, email):
    users = User.objects.filter(email)
    for user in users:
        subject = 'welcome to Fundoonotes'
        message = f' {user.username}, Thanks you for joining our Fundoonotes'
        msg = EmailMessage()
        msg.set_content(message)
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = email
        print(msg['To'])
        msg['Subject'] = subject
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # # Authentication
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        # # sending the mail
        server.send_message(msg=msg)
        # # terminating the session
        server.quit()

    return "successfully registered"