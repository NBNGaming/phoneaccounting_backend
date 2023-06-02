from rest_framework import viewsets
from rest_framework import generics

from . import models
from . import serializers


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer


class PhoneListByManufacturer(generics.ListAPIView):
    serializer_class = serializers.PhoneSerializer

    def get_queryset(self):
        manufacturer = self.kwargs['manufacturer']
        return models.Phone.objects.filter(manufacturer__iexact=manufacturer)


class NotificationList(generics.ListCreateAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer


class SIMCardViewSet(viewsets.ModelViewSet):
    queryset = models.SIMCard.objects.all()
    serializer_class = serializers.SIMCardSerializer


class SIMCardListByNumber(generics.ListAPIView):
    serializer_class = serializers.SIMCardSerializer

    def get_queryset(self):
        number = self.kwargs['number'].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')
        return models.SIMCard.objects.filter(number=number)


class SDCardViewSet(viewsets.ModelViewSet):
    queryset = models.SDCard.objects.all()
    serializer_class = serializers.SDCardSerializer


class SDCardListBySerial(generics.ListAPIView):
    serializer_class = serializers.SDCardSerializer

    def get_queryset(self):
        serial = self.kwargs['serial']
        return models.SDCard.objects.filter(serial_number=serial)
