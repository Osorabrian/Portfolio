from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(
        request,
        "account/home.html",
        { 'section':'dashboard'}
    )
    
def message(request):
    
    message = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = form.save(commit=False)
            message.body = cd['message']
            message.save()
            
    else:
        form = ContactForm()
    
    return render(
        request,
        'account/contact.html',
        {'form':form, 'message':message}
    )