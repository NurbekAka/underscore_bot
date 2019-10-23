from django.urls import path
from .views import TelegramListView

urlpatterns = [
    path('', TelegramListView.as_view(), name='home'),
]
