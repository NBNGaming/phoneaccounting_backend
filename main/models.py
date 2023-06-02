from django.db import models


class Phone(models.Model):
    manufacturer = models.CharField(max_length=255, default='')
    model = models.CharField(max_length=255, default='')
    os_version = models.CharField(max_length=255, default='')
    converted_os_version = models.CharField(max_length=255, default='')
    firmware = models.CharField(max_length=255, default='')
    sd_slots_count = models.PositiveSmallIntegerField()
    sdcard_serial_number = models.CharField(max_length=255, default='')
    sim_slots_count = models.PositiveSmallIntegerField()
    simcard1 = models.CharField(max_length=255, default='')
    simcard2 = models.CharField(max_length=255, default='')
    supported_arch = models.CharField(max_length=255, default='')
    user = models.CharField(max_length=255, default='')


class SDCard(models.Model):
    in_phone = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default='')
    serial_number = models.CharField(max_length=255, default='')
    size = models.CharField(max_length=255, default='')


class SIMCard(models.Model):
    in_phone = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    number = models.CharField(max_length=255, default='')
    operator_name = models.CharField(max_length=255, default='')


class Notification(models.Model):
    text = models.CharField(max_length=255, default='')
    package_name = models.CharField(max_length=255, default='')
    title = models.CharField(max_length=255, default='')
