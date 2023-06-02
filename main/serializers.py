from rest_framework import serializers

from . import models


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'


class SIMCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SIMCard
        fields = '__all__'


class SDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SDCard
        fields = '__all__'
