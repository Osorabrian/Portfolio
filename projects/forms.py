from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Search for a Project', 'type':'search', 'class':'form-control rounded-0','id':'search-input'}))