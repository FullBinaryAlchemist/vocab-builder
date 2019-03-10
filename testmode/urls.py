from django.contrib import admin
from django.urls import path
from django.urls import include
from study import urls as study_urls
from dashboard import urls as dashboard_urls
from .views import *
urlpatterns = [
    path('info/<int:test_id>', info,name="info"),


]
