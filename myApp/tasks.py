from celery import shared_task
from django.core.mail import send_mail
from .models import Quote, DailyMotivationalQuote
import random



@shared_task
def update_motivational_quote():
    latest_quote = DailyMotivationalQuote.objects.order_by("-created_at").first()

    quotes_count = Quote.objects.count()
    if quotes_count == 0:
        return None

    random_index = random.randint(0, quotes_count - 1)
    random_quote = Quote.objects.all()[random_index]

    if not latest_quote:
        DailyMotivationalQuote.objects.create(quote=random_quote)
        return None

    latest_quote.quote = random_quote
    latest_quote.save()
    return None

