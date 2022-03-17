from django.urls import path
from .views import *


urlpatterns = [
    path('account/', ussd_callback, name='account'),
]
