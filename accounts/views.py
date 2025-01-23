from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

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
            send_mail(
                f"Contact from {cd['name']}",
                cd['message'],
                cd['email'],
                ['osorabrian@gmail.com']
            )
            
    else:
        form = ContactForm()
    
    return render(
        request,
        'account/contact.html',
        {'form':form, 'message':message}
    )