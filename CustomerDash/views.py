from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from CustomerDash.models import Device, DeviceLog, Recharge
import paho.mqtt.client as mqtt
import json
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth.models import User
import paho.mqtt.publish as publish

# Create your views here.


def index(request):
    return  render(request,'index.html',{})


def dashboard(request):
    if request.user.is_authenticated():
        DeviceObj = Device.objects.get(user_id=request.user)
        responce =  render(request,'dash.html',context={"user":request.user, "Device" : DeviceObj})
    else:
        responce = redirect('/')
    return responce


def userlogin(request):
    if request.is_ajax():
        email = request.POST.get('email')
        password = request.POST.get('password')
        userObj = authenticate(username = email, password = password)
        if userObj is not None:
            login(request,userObj)
            responce = HttpResponse("OK")
        else:
            responce = HttpResponse("Something is wrong")
    else:
        responce = HttpResponse("Not Ajax")
    return responce


def userlogout(request):
    logout(request)
    return HttpResponse("OK")


def mqttclient(request):
    if request.is_ajax():
        pin = request.POST.get('pin')
        status = request.POST.get('status')
        dic = {}
        dic[pin] = status
        tem = json.dumps(dic)
        def on_connect(client, userdata, flag, rc):
            print("Connected with userdata" +str(rc))
            client.subscribe("topic/shambhu/testing")
        def on_message(client, userdata, msg):
            print(msg.topic + " "+ msg.payload)
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("iot.eclipse.org",1883,60)
        msg = pin + "-" + status
        return HttpResponse("Wah wah kya baat hai")

@csrf_exempt
def updatestatus(request):
    try:
        if request.method == "POST":
            device = request.POST.get("device_id")
            unit = float(request.POST.get("counter"))
            balance = float(request.POST.get("balance"))
            print request.POST.get("counter")
            deviceObj = Device.objects.get(device_c_id=device)
            deviceObj.usage += unit
            deviceObj.save()
            devicelogObj = DeviceLog.objects.create(device_id=deviceObj,remaining_balance=balance,usage=unit)
            devicelogObj.save()
            responce = {'status': 'ok'}
        else:
            responce = {'status': 'error'}
    except Device.DoesNotExist:
        responce = {'status':'device does not exist'}
    return JsonResponse(responce)

def recharge(request):
    return render(request,"recharge.html",context={})


def rechargeProceed(request):
    device = request.POST.get("device")
    username = request.POST.get("username")
    amount = float(request.POST.get("amount"))
    userObj = User.objects.get(email = username)
    deviceObj = Device.objects.get(device_c_id=device)
    deviceObj.balance  = amount + deviceObj.balance
    deviceObj.status = 1
    deviceObj.save()
    rechargeObj = Recharge.objects.create(device_id=deviceObj,user_id=userObj,amount= amount)
    rechargeObj.transaction_id = uuid.uuid4()
    rechargeObj.save()
    responce = {}
    responce['transection_id'] = str(rechargeObj.transaction_id)
    responce['status'] = 'ok'
    responce['amount'] = deviceObj.balance
    topic = "eliot/recharge/"+device
    publish.single(topic,json.dumps(responce),hostname="iot.eclipse.org")
    return JsonResponse(responce)


def graphvalues(request):
    device = request.POST.get("device_id")
    deviceObj = Device.objects.get(device_c_id=device)
    deviceLogObj = DeviceLog.objects.filter(device_id=deviceObj)
    for i in deviceLogObj:
        print i.usage
    return HttpResponse('great')


