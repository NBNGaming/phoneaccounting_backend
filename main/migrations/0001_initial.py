# Generated by Django 4.2.1 on 2023-06-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=255)),
                ('package_name', models.CharField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='', max_length=255)),
                ('model', models.CharField(default='', max_length=255)),
                ('os_version', models.CharField(default='', max_length=255)),
                ('converted_os_version', models.CharField(default='', max_length=255)),
                ('firmware', models.CharField(default='', max_length=255)),
                ('sd_slots_count', models.PositiveSmallIntegerField()),
                ('sdcard_serial_number', models.CharField(default='', max_length=255)),
                ('sim_slots_count', models.PositiveSmallIntegerField()),
                ('simcard1', models.CharField(default='', max_length=255)),
                ('simcard2', models.CharField(default='', max_length=255)),
                ('supported_arch', models.CharField(default='', max_length=255)),
                ('user', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SDCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_phone', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('serial_number', models.CharField(default='', max_length=255)),
                ('size', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SIMCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_phone', models.BooleanField(default=False)),
                ('locked', models.BooleanField(default=False)),
                ('number', models.CharField(default='', max_length=255)),
                ('operator_name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]