from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class DonateFood(forms.ModelForm):
    Type = forms.ChoiceField(choices=Types, widget=forms.RadioSelect())
    class Meta:
        model=models.FoodDiscription
        fields=('name','cooking_date','expiry_date','Type')
