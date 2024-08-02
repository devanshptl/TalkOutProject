from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def task_email(email):
    subject = 'Welcome to Our Site'
    message = 'Thank you for signing up for our site!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)