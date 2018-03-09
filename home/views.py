from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_home_page(request):
  return render(request, 'home.html')

@login_required()
def get_secret_page(request):
  return render(request, 'secret.html')
  
def get_message_inbox(request):
  return render(request, 'inbox.html')
  
  