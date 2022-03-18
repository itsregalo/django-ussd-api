from django.urls import path
from .views import *


urlpatterns = [
    path('ussd-callback/', ussd_callback, name='ussd_callback'),
]
