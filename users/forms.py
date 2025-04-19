from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users import views as user_views


class additionalforms(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
