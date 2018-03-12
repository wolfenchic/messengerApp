from django.shortcuts import render, get_object_or_404
from .models import Message

# Create your views here.
def inbox(request):
    return render(request, 'messenger/inbox.html')
    
def message(request, id): 
    message = get_object_or_404(Message, pk=id)
    return render(request, 'messenger/mail.html', {'message': message})
    