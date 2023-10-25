from django import forms
from app1.models import RegistrationModel

class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=20)
    education=forms.CharField(max_length=20)
    place=forms.CharField(max_length=15)
    
class RegistrationModelForm(forms.ModelForm):
    class Meta:
        model=RegistrationModel
        fields='__all__'
        # fields=['password','name']
        # exclude=['']