from django import forms
from .models import Contact, Profile
from django.contrib.auth import get_user_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
 
User = get_user_model()       
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match")
        return cd['password2']
    
    def clean_email(self):
        cd = self.cleaned_data
        email = User.objects.filter(email=cd['email']).exists()
        if email:
            raise forms.ValidationError("Email already exists.")
        return cd['email']
    
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        
class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        