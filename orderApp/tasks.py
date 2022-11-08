from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_shipment_email(owner_name, order_name, owner_email):
    mail_subject = "Your order is ready"
    message = "Hello {0}, your order {1} is ready to be shipped\n Kindly have patience.\nregards.".format(
        owner_name, order_name)
    email = EmailMessage(mail_subject, message, to=[owner_email])
    email.send()