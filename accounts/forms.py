from django import forms
from .models import Contact
from django.contrib.auth import get_user_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'usernam', 'email']
        password = forms.PasswordInput()
        password2 = forms.PasswordInput()