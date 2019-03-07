from django.urls import path
from . import views

urlpatterns = [

	# /study/ or /study/home
	path('', views.tohome, name='tohome'),
	path('home/', views.home, name='home'),

	# /study/learn/
	path('learn/', views.learn, name='learn'),
]