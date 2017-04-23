from django.contrib import admin
from CustomerDash.models import Device, DeviceLog, UserInfo, Recharge
# Register your models here.
admin.site.register(Device)
admin.site.register(DeviceLog)
admin.site.register(UserInfo)
admin.site.register(Recharge)

