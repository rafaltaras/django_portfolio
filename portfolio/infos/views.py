from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def mainpage(request):
    return render(
    	    request=request,
    	    template_name="infos/mainpage.html",
    	    # context=c
	)

def me(request):
   return HttpResponse("about me")

def contact(request):
   return HttpResponse("my contact")