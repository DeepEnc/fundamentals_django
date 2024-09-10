from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is the Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is the About Page")

def contact(request):
    return HttpResponse("This is the Contact Page")