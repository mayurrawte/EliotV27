from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class UserInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    g_id = models.CharField(max_length=100)
    f_id = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=50, default="N/A")
    mob = models.CharField(max_length=15, default="N/A")
    address = models.CharField(max_length=200, default="N/A")


class Device(models.Model):
    device_c_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    usage = models.FloatField(default=0)
    status = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)


class DeviceLog(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    log_time = models.DateTimeField(auto_now_add=True)
    remaining_balance = models.FloatField(default=0)
    usage = models.FloatField(default=0)


class Recharge(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    gateway_name = models.CharField(max_length=100,default=0)
    transaction_id = models.CharField(max_length=100)




