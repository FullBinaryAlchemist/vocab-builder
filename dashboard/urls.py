from django.shortcuts import render
from .views import dashboard_view
from django.urls import path

# Create your views here.
urlpatterns = [
	path("",dashboard_view,name="dashboard")
]
