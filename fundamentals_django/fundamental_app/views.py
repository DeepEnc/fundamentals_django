from django.shortcuts import render
from .models import AppVariety

def app(request):
    apps = AppVariety.objects.all()
    return render(request, 'fundamental_app/app.html', {'apps': apps})