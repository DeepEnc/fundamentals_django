from django.shortcuts import render
from .models import AppVariety
from django.shortcuts import get_object_or_404

def app(request):
    apps = AppVariety.objects.all()
    return render(request, 'fundamental_app/app.html', {'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(AppVariety, pk=app_id)
    return render(request, 'fundamental_app/app_detail.html', {'app': app})

def app_store_view(request):
    return render(request, 'fundamental_app/app_store.html')