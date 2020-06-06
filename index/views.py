from django.shortcuts import render
import requests
from django.contrib.auth.models import User
from django.http import JsonResponse
aloo_rate = 30
loki_rate = 20
mirch_rate = 40

def register(request) :
	return render(request,"register.html")



def send_otp(request) :
    response_data = {}
    if request.method =="POST" and request.is_ajax :
        user_phone = request.POST['phone_number']
        url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/" + user_phone + "/AUTOGEN/OTPSEND"
        response = requests.request("GET",url)
        data = response.json()
        request.session['otp_session_data'] = data['Details']
        response_data = {'Message':'Success'}
    else:
        response_data = {'Message':'Failed'}
    return JsonResponse(response_data)





def verify_otp(request):
    response_data = {}
    if request.method == "POST" and request.is_ajax:
        user_otp = request.POST['otp']
        url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + user_otp + ""
        response = requests.request("GET",url)
        data = response.json()
        if data['Status'] == "Success":
            logged_user.is_active = True
            response_data = {'Message':'Success'}
        else:
            response_data = {'Message':'Failed'}
            logout(request)
    return JsonResponse(response_data)



def BUY(request) :

    if int(request.POST["aloo_num"]) :
        aloo_num = 0
    if int(request.POST["loki_num"]) :
        loki_num = 0
    if int(request.POST["mirch_num"]) :
        mirch_num= 0
    aloo_num = int(request.POST["aloo_num"])
    if aloo_num==0 :
        aloo_num = 0
    loki_num = int(request.POST["loki_num"])
    if loki_num==0 :
         loki_num = 0
    mirch_num = int(request.POST["mirch_num"])
    if mirch_num==0 :
        mirch_num = 0
    total_aloo = aloo_num*aloo_rate
    total_loki = loki_num*loki_rate
    total_mirch = mirch_num*mirch_rate

    total = total_aloo + total_loki + total_mirch
    return render (request , "bill_format.html" , {"total":total,"total_aloo":total_aloo,"total_loki":total_loki,"total_mirch":total_mirch})

