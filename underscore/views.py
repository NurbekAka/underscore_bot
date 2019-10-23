from django.views.generic import ListView
from .models import Telegram_Post


class TelegramListView(ListView):
    model = Telegram_Post
    template_name = 'telegram_list.html'
