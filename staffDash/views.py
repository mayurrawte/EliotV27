from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from CustomerDash.models import Device, UserInfo
# Create your views here.


def staffDash(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return render(request,'staff.html',context={ "user":request.user })


def staffLogin(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            userObj = authenticate(username=username, password=password)
            if userObj is not None:
                login(request, userObj)
                responce = HttpResponse("OK")
            else:
                responce = HttpResponse("Something in Credentials is wrong")
        except User.DoesNotExist:
            responce = HttpResponse("User does not exist")
    else:
        responce = render(request, "stafflogin.html", context={})
    return responce

def addUser(request):
    if request.is_ajax():
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        userObj = User(username= email, email= email, first_name=firstname, last_name= lastname)
        userObj.set_password("Testing123")
        userObj.save()
        DeviceObj = Device(user_id=userObj)
        DeviceObj.save()
        UserInfoObj = UserInfo(user_id=userObj, address=address, aadhar= aadhar, mob= mobile)
        UserInfoObj.save()
        responce = HttpResponse("Ok" + str(DeviceObj.device_c_id))
    else:
        responce = HttpResponse("Not Ajax")
    return  responce


