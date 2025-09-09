from celery import shared_task
from django.core.mail import send_mail
from .models import Quote, DailyMotivationalQuote, DailyEmailSubscription
import random


@shared_task
def update_motivational_quote():
    latest_quote = DailyMotivationalQuote.objects.order_by("-created_at").first()

    quotes_count = Quote.objects.count()
    if quotes_count == 0:
        return None

    # Pick random quote efficiently
    random_quote = Quote.objects.order_by("?").first()

    if not latest_quote:
        DailyMotivationalQuote.objects.create(quote=random_quote)
    else:
        latest_quote.quote = random_quote
        latest_quote.save()

    return None


@shared_task
def send_email_to_subscribers():
    latest_quote = DailyMotivationalQuote.objects.order_by("-created_at").first()
    if not latest_quote:
        return None

    subject = "Motivational Quote!"
    message = latest_quote.quote.text  # assuming Quote has a `text` field

    for item in DailyEmailSubscription.objects.all():
        send_mail(
            subject=subject,
            message=message,
            from_email=None,  # or settings.DEFAULT_FROM_EMAIL
            recipient_list=[item.user.email],
        )
