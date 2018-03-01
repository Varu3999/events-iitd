from django.shortcuts import render
from .models import event , register ,sa
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def events(request):
    if request.method =="POST":
        if (request.POST.get('email')) and (request.POST.get('name') ):
            try:
                register_user = register()
                register_user.email = request.POST.get('email')
                register_user.name = request.POST.get('name')
                register_user.event = event.objects.filter(name= request.POST.get('event'))[0]
                register_user.save()

            except:
                messages.add_message(request, messages.SUCCESS,
                                     'This Email Id is already registered!')
        else:
            messages.add_message(request, messages.SUCCESS,
                                 'Please Fill all the details')
    events = event.objects.filter()
    return render(request,'event_handler/events.html',{'events':events,"register":False,"sa":sa.objects.filter()})



def redir(request):
    return HttpResponseRedirect('/events')
