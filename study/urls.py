from django.urls import path
from . import views

urlpatterns = [

	# vocabuilder/ or vocabuilder/study
	path('', views.tostudy, name='tostudy'),
	path('study/', views.study, name='study'),

	# vocabuilder/study/learn/
	path('learn/', views.learn, name='learn'),
]