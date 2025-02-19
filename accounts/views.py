from django.shortcuts import render
from .forms import ContactForm, UserRegistrationForm, EditProfileForm, EditUserForm, CustomLoginForm, CustomPasswordResetForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .models import Profile
from django.contrib import messages
from django.contrib.auth.views import LoginView,PasswordResetView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm
    
class CustomPasswordResetFormView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    form_class = CustomPasswordResetForm

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
            messages.success(request, "Your message has been sent successfully")
            send_mail(
                f"Contact from {cd['name']}",
                cd['message'],
                cd['email'],
                ['osorabrian@gmail.com']
            )
        else:
            messages.error(request, "Sorry! There was an error sending your message.")
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
            Profile.objects.create(user = user)
            messages.success(request, "Account created successfully.")
            return render(
                request,
                'account/user_registration_done.html',
                {'user': user}
            )
        else:
            messages.error(request, "Sorry! There is an error creating an account.")
    else:
        form = UserRegistrationForm()
            
    return render(
        request,
        'account/user_registration.html',
        {'form':form}
    )
    
def profile(request):
    if request.method == "POST":
        user_form = EditUserForm(instance = request.user, data = request.POST)
        profile_form = EditProfileForm(instance = request.user.profile ,data = request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile has been updated successfully.")
            return render(
                request,
                'account/profile_edited.html'
            )
        else:
            messages.error(request, "Error in updating your profile.")
    else:
        user_form = EditUserForm(instance = request.user)
        profile_form = EditProfileForm(instance = request.user.profile)
        
    return render(
        request,
        'account/edit_profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
    )