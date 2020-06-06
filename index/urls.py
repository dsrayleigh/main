from django.urls import path
from index.views import register , send_otp , verify_otp , BUY

urlpatterns = [

    path('',views.register,name = "register"),
    path('send_otp',views.send_otp,name="send_otp"),
    path('verify_otp',views.verify_otp,name="verify_otp"),
    path('BUY',views.BUY , name = "BUY")
]
