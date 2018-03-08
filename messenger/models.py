from django.db import models

# Create your models here.
class Message(models.Model):
    subject = models.Charfield(max_length=50)
    body = models.Charfield(max_length=50)
    sender = models.ForeignKey('auth.User', blank=False)
    recipient = models.ForeignKey('auth.User', blank=False)
    read = models.BooleanField(default)