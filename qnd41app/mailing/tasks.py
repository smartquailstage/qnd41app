from celery import shared_task
from .models import EmailCampaign
from django.utils import timezone

@shared_task
def send_scheduled_emails():
    emails = EmailCampaign.objects.filter(sent=False, send_date__lte=timezone.now())
    for email in emails:
        email.send_email()
