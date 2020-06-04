from django import forms
from .models import PhoneModel

class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['to']

class VerifyForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['code']
