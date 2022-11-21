from django import forms
from django.db import models


from clone.models import Victims
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class createForm(forms.ModelForm):
   
    class Meta:
        model = Victims
        fields = [
           
            'title',
            'password',
       
           
            
        ]