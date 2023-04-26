from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
   first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   last_name= forms.CharField(
       widget=forms.TextInput(
           attrs={
               "class": "form-control"
           }
       )
   )
   image = forms.ImageField(
       widget=forms.FileInput(

       )
   )
   username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


   class Meta:
        model = User
        fields = ('first_name','last_name','image','username', 'email', 'password1', 'password2','address', 'is_patient', 'is_doctor')
