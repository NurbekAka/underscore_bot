from rest_framework import serializers
from underscore.models import Telegram_Post
from underscore import services as likes_services
from django.contrib.auth import get_user_model

User = get_user_model()


class TelegramSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Telegram_Post
        fields = ('id', 'title', 'category', 'image', 'longitude', 'altitude', 'total_likes', 'is_fan')

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()