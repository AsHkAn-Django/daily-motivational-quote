from celery import shared_task
from django.core.mail import send_mail
from .models import Quote, DailyMotivationalQuote



@shared_task
def update_motivational_quote():
    latest_quote = DailyMotivationalQuote.objects.order_by(
        '-created_at'
        ).first()
    if not latest_quote:    # if there is no previous dailyMotivationQuote
        quotes = Quote.objects.all()
        if not quotes.exists():     # if there is no quotes
            return None
        random_quote = quotes.order_by('?').first()     # pick a random quote
        new_quote = DailyMotivationalQuote.objects.create(quote=random_quote)
        return new_quote

    quotes = Quote.objects.all()
    if not quotes.exists():     # If there is no quotes
        return latest_quote
    random_quote = quotes.order_by('?').first()
    latest_quote.quote = random_quote
    latest_quote.save()
    return latest_quote    # otherwise bring the older quote
