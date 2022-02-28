from django import forms
from django.forms import fields
from .models import Entry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryCreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['first_name', 'second_name', 'matric_no', 'lecture_1', 'lecture_2', 'lecture_3', 'lecture_4', 'lecture_5', 'lecture_6']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']