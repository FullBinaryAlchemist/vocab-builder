from django.urls import path
from . import views

urlpatterns = [

	# /study/ or /study/home
	path('', views.tostudy, name='tostudy'),
	path('study/', views.study, name='study'),

	# /study/learn/
	path('learn/', views.learn, name='learn'),
]