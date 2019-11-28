"""
Definition of urls for WildlifeWatcher.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from app import forms, views
from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls import include, url
import BirdBuddy.views


urlpatterns = [
    url(r'^about$', BirdBuddy.views.about, name='about'),
    url(r'^home$', BirdBuddy.views.home, name='home'),
    url(r'$', BirdBuddy.views.index, name='index'),
]
