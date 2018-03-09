from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^inbox/', inbox, name='inbox'),
    url(r'^mail/(\d+)', message, name='view_message'),
]