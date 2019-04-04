from django.urls import path
from . import views

urlpatterns = [

    # vocabuilder/ or vocabuilder/study

    path('', views.landing, name='landing'),
    path('study/learn/', views.tostudy, name='tostudy'),
    path('study/review/', views.tostudy, name='tostudy'),
    path('study/', views.study, name='study'),

    # vocabuilder/study/learn/l_word_num/
    path('study/learn/<int:l_word_num>/', views.learn, name='learn'),

    # vocabuilder/study/review/r_word_num/
    path('study/review/<int:r_word_num>/', views.review, name='review'),
]
