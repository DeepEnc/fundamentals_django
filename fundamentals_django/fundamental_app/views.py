from django.shortcuts import render
from .models import AppVariety, AppStore
from django.shortcuts import get_object_or_404
from .forms import AppVarietyForm

def app(request):
    apps = AppVariety.objects.all()
    return render(request, 'fundamental_app/app.html', {'apps': apps})

def app_detail(request, app_id):
    app = get_object_or_404(AppVariety, pk=app_id)
    return render(request, 'fundamental_app/app_detail.html', {'app': app})

def app_store_view(request):
    stores = None
    if request.method == 'POST':
     form = AppVarietyForm(request.POST)
     if form.is_valid():
         app_variety = form.cleaned_data['app_variety']
         stores = AppStore.objects.filter(app_varieties=app_variety)   
    else:
       form = AppVarietyForm()
    return render(request, 'fundamental_app/app_store.html', {'stores': stores, 'form': form})