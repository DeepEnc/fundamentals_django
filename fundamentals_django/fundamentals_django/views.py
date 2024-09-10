from django.http import HttpResponse


def home(request):
    return HttpResponse("This is the Home Page")

def about(request):
    return HttpResponse("This is the About Page")

def contact(request):
    return HttpResponse("This is the Contact Page")