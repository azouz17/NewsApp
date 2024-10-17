# from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import *

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')

#     class Meta:
#         model = User
#         fields = ('name', 'email', 'password', 'dob')


from django import forms
from django.contrib.auth.forms import AuthenticationForm


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # profileImg = forms.ImageField()
    # email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['name', 'emai', 'password']

class CategoryForm(forms.Form):
    category = forms.CharField(max_length=200)
    categoryImg = forms.ImageField()

    # class Meta:
    #     model = User
    #     fields = ['userName', 'email', 'password']

class LogInForm(AuthenticationForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']