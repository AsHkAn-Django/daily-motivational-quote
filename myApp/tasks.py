from celery import shared_task
from django.core.mail import send_mail
from .models import Quote, DailyMotivationalQuote
import random
import tweepy



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


# TODO: It was cancelled because it needed real domain
# @shared_task
# def post_daily_quote_to_twitter():
#     auth = tweepy.OAuth1UserHandler(
#     settings.TWITTER_API_KEY,
#     settings.TWITTER_API_SECRET,
#     settings.TWITTER_ACCESS_TOKEN,
#     settings.TWITTER_ACCESS_SECRET,
#     )
#     api = tweepy.API(auth)

#     api.update_status("Daily motivation 🌞")
#     quote = DailyMotivationalQuote.objects.order_by("-created_at").first()
#     if not quote:
#         return "No quote found"


