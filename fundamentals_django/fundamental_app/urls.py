from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name="app"),
    path('<int:app_id>/', views.app_detail, name="app_detail"),
    path('app_store', views.app_store_view, name="app_store"),
]
