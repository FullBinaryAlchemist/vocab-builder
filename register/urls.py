from django.shortcuts import render,redirect
from .views import *
from django.urls import path
from register.views import register
# Create your views here.
urlpatterns = [
	path("",register_view,name="Register"),
	#path("info/<int:test_id>",info_redirect,name="info_redirect")
]
