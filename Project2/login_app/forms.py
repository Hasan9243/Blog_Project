from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    password = forms.CharField(max_length=50, widget = forms.PasswordInput())


    class Meta:
        model=User
        fields=('username','first_name', 'last_name','password', 'email')

class UserInfo(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('facebook_id', 'profile_pic')
        
        