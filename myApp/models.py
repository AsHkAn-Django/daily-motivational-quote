from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.utils.timezone import now


class Quote(models.Model):
    body = models.CharField(max_length=500)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=260)

    def __str__(self):
        return f"{self.author}: {self.body[:50]}..."

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})


class DailyMotivationalQuote(models.Model):
    """Use the Quote Model choose a new one every 30sec."""
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    # @classmethod
    # def get_quote(cls):
    #     latest_quote = cls.objects.order_by('-created_at').first()  # Call yourself with cls instead of DailyMotivationalQuote
    #     if not latest_quote:    # if there is no previous dailyMotivationQuote
    #         quotes = Quote.objects.all()
    #         if not quotes.exists():     # if there is no quotes
    #             return None
    #         random_quote = quotes.order_by('?').first()     # pick a random quote
    #         new_quote = cls.objects.create(quote=random_quote)
    #         return new_quote

    #     current_time = now()
    #     total_seconds = (current_time - latest_quote.created_at).total_seconds()
    #     if total_seconds > 10:
    #         quotes = Quote.objects.all()
    #         if not quotes.exists():     # If there is no quotes
    #             return latest_quote
    #         random_quote = quotes.order_by('?').first()
    #         latest_quote.quote = random_quote
    #         latest_quote.save()
    #         return latest_quote
    #     return latest_quote    # otherwise bring the older quote

    def __str__(self):
        return f"{self.quote.body[:35]} - {self.quote.author}"
