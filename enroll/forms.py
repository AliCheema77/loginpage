from django import forms
from django.forms import fields, models, widgets
from .models import NewUser

class SignUpForm(models.ModelForm):
    class Meta:
        model = NewUser
        fields = ['first_name','last_name','password']
        widgets = {
            'password':forms.PasswordInput()
        }

class LoginForm(models.ModelForm):
    class Meta:
        model = NewUser
        fields = ['first_name','password']
        widgets ={
            'password':forms.PasswordInput()
        }