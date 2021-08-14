from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives


@shared_task()
def send_email(email):
    """
    Sends email
    """
    subject = 'Welcome on App'
    from_email = EMAIL_HOST_USER
    to_emails = [email]
    text_content = 'You have successfully logged on the App'
    email = EmailMultiAlternatives(subject, text_content, from_email, to_emails)
    email.send()
