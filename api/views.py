from django.shortcuts import render, HttpResponse
import africastalking
import os
from api.models import Member
from decouple import config
from django.views.decorators.csrf import csrf_exempt

username = config('username')
api_key = config('api_key')

africastalking.initialize(username, api_key)
sms = africastalking.SMS

#django africastalking ussd_callback
@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        session_id = request.GET.get("sessionId")
        service_code = request.GET.get("serviceCode")
        phone_number = request.GET.get("phoneNumber")
        text = request.GET.get("text", "default")

        response=""

        if text == "":
            response = "Hello What would you like to check \n"
            response += "1. List all members \n"
            response += "2. Confirm if registered \n"

        elif text == "1":
            members = Member.objects.all()
            for member in members:
                response = member.name + "\n"
                response += member.adm_no + "\n"

        return HttpResponse(response)
        
   

        