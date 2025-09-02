from django.contrib import admin
from .models import Quote, DailyMotivationalQuote

# Register your models here.
admin.site.register(Quote)
admin.site.register(DailyMotivationalQuote)
