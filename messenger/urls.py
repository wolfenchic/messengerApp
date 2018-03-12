from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^inbox/', inbox, name='inbox'),
    url(r'^mail/(\d+)', message, name='view_message'),
    url(r'^sent/', sent, name='sent'),
    url(r'^message/compose', compose_message, name='compose_message'),
]
