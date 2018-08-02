# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Computer(models.Model):
    model = models.CharField(max_length=255, null=True)
    serial_number = models.CharField(max_length=255, null=True)
    brand_name = models.CharField( max_length=255, null=True)
    number_of_usb_ports = models.IntegerField( null=True)
    hard_drive = models.IntegerField( null=True)
    ram = models.IntegerField( null=True)
    is_wifi_enabled = models.BooleanField( default=False)
    sound_system = models.CharField(max_length=255, null=True)
    cpu_speed = models.FloatField( null=True)
