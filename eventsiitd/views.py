from django.shortcuts import HttpResponseRedirect
def redir(request):
    return HttpResponseRedirect('/events')