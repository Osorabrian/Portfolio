from django.shortcuts import render
from .forms import ContactForm, UserRegistrationForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

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
 
def user_registration(request):
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(cd['password'])
            user.save()
            return render(
                request,
                'account/user_registration_done.html',
                {'user': user}
            )
    else:
        form = UserRegistrationForm()
            
    return render(
        request,
        'account/user_registration.html',
        {'form':form}
    )
    