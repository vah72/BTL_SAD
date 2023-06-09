"""user_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_login.views import user_login
from user_info.views import user_info
from user_model.views import *
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('userregistration/', registration_req, name='user_registration'),
    path('userlogin/', user_login),
    path('userinfo/', user_info),
    path('getalluser/', getAllUser),

]
