from rest_framework import generics
from rest_framework import filters
from underscore.models import Telegram_Post
from .serializers import TelegramSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.mixins import LikedMixin


class TelegramAPIView(LikedMixin, generics.ListAPIView):
    queryset = Telegram_Post.objects.all()
    serializer_class = TelegramSerializer
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'status')
    search_fields = ('category', 'status')


class TelegramAPICreate(generics.CreateAPIView):
    queryset = Telegram_Post.objects.all()
    serializer_class = TelegramSerializer


class TelegramAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telegram_Post.objects.all()
    serializer_class = TelegramSerializer
