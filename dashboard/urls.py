from django.shortcuts import render,redirect
from .views import *
from django.urls import path
from testmode.views import info
# Create your views here.
urlpatterns = [
	path("", dashboard_view, name="dashboard"),
	path("info/<int:test_id>", info_redirect, name="info_redirect")
]
