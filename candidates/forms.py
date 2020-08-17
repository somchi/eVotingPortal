from django import forms
from .models import RegistrationForm

class Registration(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    image = forms.ImageField()
    class Meta:
        model = RegistrationForm
        fields = '__all__'



