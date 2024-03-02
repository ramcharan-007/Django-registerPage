from django import forms
from .models import UserData

class DataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['firstName', 'lastName', 'userName', 'emailId', 'password']
