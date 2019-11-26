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
    url(r'^$', BirdBuddy.views.index, name='index'),
    url(r'^home$', BirdBuddy.views.index, name='home'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
