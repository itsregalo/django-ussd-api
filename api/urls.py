from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('ussd-callback/', ussd_callback, name='ussd_callback'),
]
