from django.db import models


class Phone(models.Model):
    manufacturer = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    os_version = models.CharField(max_length=255, blank=True)
    converted_os_version = models.CharField(max_length=255, blank=True)
    firmware = models.CharField(max_length=255, blank=True)
    sd_slots_count = models.PositiveSmallIntegerField()
    sdcard_serial_number = models.CharField(max_length=255, blank=True)
    sim_slots_count = models.PositiveSmallIntegerField()
    simcard1 = models.CharField(max_length=255, blank=True)
    simcard2 = models.CharField(max_length=255, blank=True)
    supported_arch = models.CharField(max_length=255, blank=True)
    user = models.CharField(max_length=255, blank=True)


class SDCard(models.Model):
    in_phone = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=True)
    serial_number = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=255, blank=True)


class SIMCard(models.Model):
    in_phone = models.BooleanField(default=False)
    locked = models.BooleanField(default=False)
    number = models.CharField(max_length=255, blank=True)
    operator_name = models.CharField(max_length=255, blank=True)


class Notification(models.Model):
    text = models.CharField(max_length=255, blank=True)
    package_name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
