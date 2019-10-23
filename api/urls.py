from django.urls import path
from .views import TelegramAPIView, TelegramAPIDetail, TelegramAPICreate

urlpatterns = [
    path('', TelegramAPIView.as_view()),
    path('create/', TelegramAPICreate.as_view()),
    path('<int:pk>/', TelegramAPIDetail.as_view()),
]
