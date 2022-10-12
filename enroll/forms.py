from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name here....'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'enter your email here....'}),
            'password' : forms.PasswordInput(render_value=True ,attrs={'class':'form-control','placeholder':'enter your password here....'}),
        }
        labels = {
            'name' : 'NAME',
            'email' : 'EMAIL',
            'password' : 'PASSWORD'
        }
        error_messages = {
            'name' : {'required':'PLEASE ENTER YOUR NAME'},
            'email' : {'required':'PLEASE ENTER YOUR EMAIL'},
            'password':{'required':'PLEASE ENTER YOUR PASSWORD'}
        }