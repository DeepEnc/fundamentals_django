from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is the Home Page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("This is the About Page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("This is the Contact Page")
    return render(request, 'website/contact.html')