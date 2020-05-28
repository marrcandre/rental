from rest_framework import serializers

from . import models


class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Friend
        fields = ("id", "name", "owner")


class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ("id", "name", "owner")


class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ("id", "what", "to_who", "when", "returned")
