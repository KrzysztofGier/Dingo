from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

def hello_name(request, name):
    name = str(name)
    return HttpResponse(f"Hello {name.capitalize()}!")

def welcome(request):
    return render(
        request=request,
        template_name="greetings/welcome.html",
        context={} 
    )

def about(request):
    return render(
        request=request,
        template_name="greetings/about.html",
        context={} 
    )

def contact(request):
    return render(
        request=request,
        template_name="greetings/contact.html",
        context={} 
    )   