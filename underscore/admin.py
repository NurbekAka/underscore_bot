from django.contrib import admin
from .models import Telegram_Post, Category

admin.site.register(Telegram_Post),
admin.site.register(Category)