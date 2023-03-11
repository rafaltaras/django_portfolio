from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def mainpage(request):
    return render(request, "infos/mainpage.html", {'navbar': 'mainpage'})

def me(request):
    return render(request, "infos/me.html", {'navbar': 'me'})

def contact(request):
    return render(request, "infos/contact.html", {'navbar': 'contact'})