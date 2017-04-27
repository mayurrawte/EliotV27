"""EliotV27 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CustomerDash import views as CustomerViews
from staffDash import views as StaffViews
from EliotV27 import views as EliotViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',CustomerViews.index, name="index"),
    url(r'^dashboard',CustomerViews.dashboard, name="dashboard"),
    url(r'^staff/', StaffViews.staffDash, name="StaffView"),
    url(r'^stafflogin/',StaffViews.staffLogin, name="Staff Login"),
    url(r'^adduser/',StaffViews.addUser, name="Add User"),
    url(r'^userlogin/',CustomerViews.userlogin, name="User Login"),
    url(r'^userlogout/', CustomerViews.userlogout, name="User Logout"),
    url(r'^mqttclient/',CustomerViews.mqttclient, name="mqtt client"),
    url(r'^asyncmeter/update/(?P<device_id>\d+)/', EliotViews.asyncupdation, name="Aysncmeter"),
    url(r'^update/', CustomerViews.updatestatus,name="Update"),
    url(r'^recharge/',CustomerViews.recharge,name="Recharge"),
    url(r'^recharge-proceed/',CustomerViews.rechargeProceed,name="Recharge Proceed"),
    url(r'^graphvalues/',CustomerViews.graphvalues,name="graphvalues")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
