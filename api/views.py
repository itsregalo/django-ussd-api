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
        session_id = request.POST.get("sessionId"),
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST.get("text", "default")

        response=""

        if text == "":
            response = "CON Hello What would you like to check \n"
            response += "1. List all members \n"
            response += "2. Confirm if registered \n"

        elif text == "1":
            members = Member.objects.all()
            for member in members:

                response = f"END {member.name} - {member.adm_no}\n"

        return HttpResponse(response)
        
   

        