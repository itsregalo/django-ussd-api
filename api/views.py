from django.shortcuts import render
import africastalking
import os
from decouple import config
from django.shortcuts import HttpResponse

username = config('username')
api_key = config('api_key')

africastalking.initialize(username, api_key)
sms = africastalking.SMS

#django africastalking ussd_callback
def ussd_callback(request):
    session_id = request.GET.get("sessionId", None)
    service_code = request.GET.get("serviceCode", None)
    phone_number = request.GET.get("phoneNumber", None)
    text = request.GET.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    if text == "":
        response = "Hello What would you like to check \n"
        response += "1. Register \n"
        response += "2. Confirm if registered \n"
    return HttpResponse(response)
        