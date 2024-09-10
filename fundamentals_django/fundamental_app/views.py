from django.shortcuts import render

def app(request):
    return render(request, 'fundamental_app/app.html')