from django.shortcuts import render
from django.http import HttpResponse
from CustomerDash.models import Device
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def asyncupdation(request,device_id):
    if request.method == "POST":
        #device =  Device.objects.get(device_c_id=device_id)
        data = json.loads(request.body)
        print(data)
        return HttpResponse('Ok')

