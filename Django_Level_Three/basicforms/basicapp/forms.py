from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basicapp.models import Userprofileinfo



class Userform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username' , 'email' , 'password')

class Userprofileinfoforms(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('portfolio_site' , 'profile_pic')
