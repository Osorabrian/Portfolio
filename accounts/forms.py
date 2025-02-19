from django import forms
from .models import Contact, Profile
from django.contrib.auth import get_user_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'example@gmail.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter Message'})
        }
 
User = get_user_model()       
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control rounded-0"}))
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(attrs={"placeholder":"Repeat Password","class":"form-control rounded-0"}))
    
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control rounded-0', 'placeholder': 'First Name', }),
            'last_name': forms.TextInput(attrs={'class':'form-control rounded-0', 'placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':"form-control rounded-0", 'placeholder':'username'}),
            'email': forms.EmailInput(attrs={"class":'form-control rounded-0', 'placeholder': 'Email'})
        }
        
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
        