
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [

    path('',include('index.urls')),
    path('BUY',include('index.urls')),
    path('send_otp',include('index.urls')),
    path('verify_otp',include('index.urls')),
    path('admin/', admin.site.urls)
    
]
