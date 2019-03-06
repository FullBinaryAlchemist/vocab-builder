from django.urls import path
from . import views

urlpatterns = [

	#/study/learn/
	path('learn/', views.learn, name='learn'),
]