from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={
        'placeholder':'Search for a Project', 
        'type':'search', 
        'class':'form-control rounded-0',
        'id':'search-input', 
        'style':'width: 300px; height: 40px; border-radius: 10%; border: 1px solid #00ffff; background-color: #ffffff; font-size: 16px; font-weight: 500; padding: 10px; margin-right: 10px;'}))
    
    