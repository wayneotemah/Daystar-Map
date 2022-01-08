from django import forms
from django.db.models import fields
from .models import *

class buildingForm(forms.ModelForm):
    class Meta:
        model = building
        fields = ['alias']